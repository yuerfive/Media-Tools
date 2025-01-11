# cython: language_level=3

import os
import shutil

from PySide6.QtCore import QObject, Signal
from multiprocessing import Pool, cpu_count, Pipe
from threading import Thread

import videotools
from main_win import Main_Win
from trayaction import TrayAction


# 自定义信号
class Signal(QObject):

    Signal = Signal(dict)

    def sendInfo(self, value: dict):
        self.Signal.emit(value)

# 自定义槽
class Slot(QObject):

    def __init__(self):
        self.MySiganl = None
        self.filenames = []
        self.OutputInfo_dict = {}
        self.isAllDone_flag = False

    # 接收信号
    def receiveInfo(self, value: dict):
        # print(value)
        branch = {
            '打开窗口': lambda: self.openWindow(value),
            '退出程序': lambda: self.exitProgram(value),
            '创建托盘': lambda: self.createTray(value),
            '激活窗口': lambda: self.activateWindow(value),
            '输出信息': lambda: self.showOutputInfo(value),
            '开始转换': lambda: Thread(target=self.startConvert, args=(value,)).start(),
        }
        branch.get(value['action'], lambda: print(f'未知命令：{value}'))()

    # 打开窗口
    def openWindow(self, value):

        if value['info'] == '打开主窗口':
            self.MySiganl = value['MySignal']
            self.Main_UI = Main_Win(self.MySiganl)
            self.Main_UI.show()

    # 退出程序
    def exitProgram(self, value):
        self.TrayAction.cleanTray()
        os._exit(0)

    # 创建托盘
    def createTray(self, value):
        self.MySiganl = value['MySignal']
        self.TrayAction = TrayAction(self.MySiganl)

    # 激活窗口
    def activateWindow(self, value):
        if self.Main_UI:
            self.Main_UI.show()
            self.Main_UI.activateWindow()

    # 开始转换
    def startConvert(self, value):
        value = value['info']
        self.filenames = [os.path.basename(i) for i in value['选择文件路径']]

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

        task_list = []  # 任务列表
        pipe_list = []  # 管道列表
        for input_video in value['选择文件路径']:

            Main_pige, Child_pige = Pipe()
            pipe_list.append(Main_pige)  # 记录主进程的管道

            filename = os.path.basename(input_video)
            output_video = os.path.join(value['输出文件路径'], f"{filename.split('.')[0]}_resized.mp4")
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
                Child_pige
            ))

        # 多进程处理
        with Pool(cpu_count()) as pool:
            pool.map_async(videotools.process_task, task_list)

            # 主进程接收消息
            completed = 0
            while completed < len(pipe_list):
                for pipe in pipe_list:
                    if pipe.poll():
                        message = pipe.recv()
                        self.MySiganl.sendInfo({'action': '输出信息', 'info': message})
                        if "已完成" in message:
                            completed += 1
            self.isAllDone_flag = True

    # 输出信息
    def showOutputInfo(self, value):

        def show_info():
            self.Main_UI.ui.outputInfo.setText('\n' + '\n\n'.join(info for _, info in self.OutputInfo_dict.items()).strip())

        value = value['info']

        filename = value.split()[0]
        if filename not in self.filenames:
            return

        if '已完成' in value:
            value = self.OutputInfo_dict[filename]
            value = value.replace('进行中', '已完成')
            self.OutputInfo_dict[filename] = value
            Thread(target=show_info).start()
            if self.isAllDone_flag:
                self.OutputInfo_dict = {}
                self.isAllDone_flag = False
        else:
            self.OutputInfo_dict[filename] = value
            Thread(target=show_info).start()