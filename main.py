# cython: language_level=3

import sys
import win32event
import win32api
from multiprocessing import freeze_support, Process, Queue
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from threading import Thread

from signal_slot import Signal, Slot
from server_process import ServerProcess

# 定义唯一的互斥锁名称
MUTEX_NAME = "Global\\MediaTools-ApplicationInstance"


def listen_messages(queue, mysignal):
    """
    后台线程：监听消息队列
    """
    while True:
        try:
            message = queue.get()  # 阻塞等待消息
            if message == "激活窗口":
                # 发送激活窗口信号
                print("收到激活窗口的请求")
                mysignal.send_info({'action': '激活窗口'})
        except Exception as e:
            print(f"消息监听出错: {e}")
            break


if __name__ == '__main__':
    freeze_support()

    # 创建互斥锁
    mutex = win32event.CreateMutex(None, False, MUTEX_NAME)
    last_error = win32api.GetLastError()

    # 如果互斥锁已存在，说明已有程序实例运行
    if last_error == 183:  # ERROR_ALREADY_EXISTS
        try:
            # 获取共享队列并发送激活消息
            queue = ServerProcess.connect_client()
            queue.put("激活窗口")
        except Exception as e:
            print(f"无法连接到共享队列: {e}")
        sys.exit(0)

    # 创建共享队列并启动服务器
    shared_queue = Queue()
    server_process = Process(
        target=ServerProcess.start_server, args=(shared_queue,), daemon=True
    )
    server_process.start()

    # 连接到共享队列
    queue = ServerProcess.connect_client()

    # 连接信号和槽
    mysignal = Signal()
    myslot = Slot()
    mysignal.Signal.connect(myslot.receive_info)

    # 创建应用
    app = QApplication([])
    app.setWindowIcon(QIcon(r'res\logo\logo_M.png'))
    QApplication.setQuitOnLastWindowClosed(False)

    # 启动消息监听线程
    Thread(target=listen_messages, args=(queue, mysignal), daemon=True).start()

    # 发送信号创建主窗口和托盘
    mysignal.send_info({'action': '打开窗口', 'info': '打开主窗口', 'mysignal': mysignal, 'mutex': mutex, 'server_process': server_process})
    mysignal.send_info({'action': '创建托盘', 'mysignal': mysignal})

    sys.exit(app.exec())
