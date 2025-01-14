# cython: language_level=3

import os
import shutil
import win32api

from PySide6.QtCore import QObject, Signal
from multiprocessing import Process, Queue
from threading import Thread

import video_tools
from main_win import MainWin
from tray_action import TrayAction


# 自定义信号
class Signal(QObject):

    Signal = Signal(dict)

    def send_info(self, value: dict):
        self.Signal.emit(value)

# 自定义槽
class Slot(QObject):

    def __init__(self):
        self.mysignal = None
        self.file_names = []
        self.output_info_dict = {}
        self.isalldone_flag = False

    # 接收信号
    def receive_info(self, value: dict):
        # print(value)
        branch = {
            '打开窗口': lambda: self.open_window(value),
            '退出程序': lambda: self.exit_program(value),
            '创建托盘': lambda: self.create_tray(value),
            '激活窗口': lambda: self.activate_window(value),
            '输出信息': lambda: self.show_output_Info(value),
            '开始转换': lambda: Thread(target=self.start_convert, args=(value,)).start(),
        }
        branch.get(value['action'], lambda: print(f'未知命令：{value}'))()

    # 打开窗口
    def open_window(self, value):

        if value['info'] == '打开主窗口':
            self.server_process = value['server_process']
            self.mutex = value['mutex']
            self.mysignal = value['mysignal']
            self.main_win = MainWin(self.mysignal)
            self.main_win.show()

    # 退出程序
    def exit_program(self, value):
        # 清理托盘资源
        self.tray_action.clean_tray()
        # 终止服务器进程
        win32api.CloseHandle(self.mutex)
        self.server_process.terminate()
        os._exit(0)

    # 创建托盘
    def create_tray(self, value):
        self.mysignal = value['mysignal']
        self.tray_action = TrayAction(self.mysignal)

    # 激活窗口
    def activate_window(self, value):
        if self.main_win:
            self.main_win.show()
            self.main_win.activateWindow()

    # 开始转换
    def start_convert(self, value):
        value = value['info']
        self.file_names = [os.path.basename(i) for i in value['选择文件路径']]

        # 检查输入参数
        if not value['选择文件路径'] or not value['输出文件路径'] or not value['转换大小'] or not value['使用算法'] or not value['转换质量'] or not value['编码预设']:
            return
        if value['锐化'] is not False and value['锐化'] is not True:
            return

        # 检查输出目录是否存在
        if os.path.exists(value['输出文件路径']):
            shutil.rmtree(value['输出文件路径'])
            os.makedirs(value['输出文件路径'])
        else:
            os.makedirs(value['输出文件路径'])

        queue = Queue()  # 主进程管道
        task_list = []  # 任务列表
        for input_video in value['选择文件路径']:
            file_name = os.path.basename(input_video)
            output_video = os.path.join(value['输出文件路径'], f"{file_name.split('.')[0]}_resized.mp4")
            target_width, target_height = value['转换大小'].split(' * ')
            task_list.append((
                input_video,
                output_video,
                int(target_width),
                int(target_height),
                value['使用算法'],
                value['锐化'],
                value['转换质量'],
                value['编码预设'],
                queue
            ))

        # 由于cpu的超线程的原因，导致实际核心数量仅为其一半，因此进程数也只能设置为一半
        # 不然会导致超出实际核心数的进程直接跳出，导致任务无法完成
        max_workers = max(os.cpu_count() // 2 - 1, 1)

        # 任务索引
        current_index = 0

        # 已完成任务计数
        completed_tasks = 0

        # 多进程处理
        for _ in range(min(max_workers, len(task_list))):
            task = task_list[current_index]
            Process(target=video_tools.process_task, args=(task,)).start()
            current_index += 1

        # 监听子进程消息, 并提交新任务
        while completed_tasks < len(task_list):
            message = queue.get()
            if message:
                print(message)
                self.mysignal.send_info({'action': '输出信息', 'info': message})

                if "已完成" in message:
                    completed_tasks += 1    # 更新已完成任务计数

                    # 提交新任务（如果有未提交任务）
                    if current_index < len(task_list):
                        task = task_list[current_index]
                        Process(target=video_tools.process_task, args=(task,)).start()
                        current_index += 1

        # 所有任务完成
        self.isalldone_flag = True

    # 输出信息
    def show_output_Info(self, value):

        value = value['info']

        filename = value.split()[0]
        if filename not in self.file_names:
            return

        if '已完成' in value:
            value = self.output_info_dict[filename]
            value = value.replace('进行中', '已完成')
            self.output_info_dict[filename] = value
            self.main_win.ui.output_info.setPlainText('\n\n'.join(info for _, info in self.output_info_dict.items()).strip())
            if self.isalldone_flag:
                self.output_info_dict = {}
                self.isalldone_flag = False
        else:
            self.output_info_dict[filename] = value
            self.main_win.ui.output_info.setPlainText('\n\n'.join(info for _, info in self.output_info_dict.items()).strip())