# cython: language_level=3

import sys
import win32event
import win32api
import multiprocessing
from multiprocessing.managers import BaseManager
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from threading import Thread
from signalAslot import Signal, Slot

# 定义唯一的互斥锁名称
MUTEX_NAME = "Global\\MyUniqueApplicationInstance"

# 定义全局队列（供所有实例共享）
shared_queue = None


class QueueManager(BaseManager):
    """队列管理器，用于进程间共享队列"""
    pass


def start_queue_server():
    """
    启动共享队列的服务器进程
    """
    global shared_queue

    QueueManager.register('get_queue', callable=lambda: shared_queue)
    manager = QueueManager(address=('127.0.0.1', 50000), authkey=b'secret')
    shared_queue = multiprocessing.Queue()
    server = manager.get_server()
    server.serve_forever()


def get_shared_queue():
    """
    获取共享队列
    """
    QueueManager.register('get_queue')
    manager = QueueManager(address=('127.0.0.1', 50000), authkey=b'secret')
    manager.connect()
    return manager.get_queue()


def listen_for_messages(queue, MySignal):
    """
    后台线程：监听消息队列
    """
    while True:
        try:
            message = queue.get()  # 阻塞等待消息
            if message == "激活窗口":
                # 发送激活窗口信号
                MySignal.sendInfo({'action': '激活窗口'})
        except Exception as e:
            print(f"消息监听出错: {e}")
            break


if __name__ == '__main__':
    multiprocessing.freeze_support()

    # 创建互斥锁
    mutex = win32event.CreateMutex(None, False, MUTEX_NAME)
    last_error = win32api.GetLastError()

    # 如果互斥锁已存在，说明已有程序实例运行
    if last_error == 183:  # ERROR_ALREADY_EXISTS
        try:
            # 获取共享队列并发送激活消息
            queue = get_shared_queue()
            queue.put("激活窗口")
            sys.exit(0)
        except Exception as e:
            print(f"无法连接到共享队列: {e}")
            sys.exit(0)

    # 主实例启动共享队列服务器
    server_process = multiprocessing.Process(target=start_queue_server, daemon=True)
    server_process.start()

    # 获取共享队列
    queue = get_shared_queue()

    # 连接信号和槽
    MySignal = Signal()
    MySlot = Slot()
    MySignal.Signal.connect(MySlot.receiveInfo)

    # 创建应用
    app = QApplication([])
    app.setWindowIcon(QIcon(r'res\logo\logo_M.png'))
    QApplication.setQuitOnLastWindowClosed(False)

    # 启动消息监听线程
    Thread(target=listen_for_messages, args=(queue, MySignal), daemon=True).start()

    # 发送信号创建主窗口和托盘
    MySignal.sendInfo({'action': '打开窗口', 'info': '打开主窗口', 'MySignal': MySignal, 'mutex': mutex, 'server_process': server_process})
    MySignal.sendInfo({'action': '创建托盘', 'MySignal': MySignal})

    sys.exit(app.exec())
