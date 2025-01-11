# cython: language_level=3

import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from multiprocessing import freeze_support

from signalAslot import Signal, Slot


if __name__ == '__main__':
    freeze_support()

    # 连接信号和槽
    MySignal = Signal()
    MySlot = Slot()
    MySignal.Signal.connect(MySlot.receiveInfo)

    # 创建应用
    app = QApplication([])
    # 设置logo
    app.setWindowIcon(QIcon(r'res\logo\logo_M.png'))
    # 设置关闭最后一个窗口也不退出程序
    QApplication.setQuitOnLastWindowClosed(False)

    MySignal.sendInfo({'action': '打开窗口', 'info': '打开主窗口', 'MySignal': MySignal})
    MySignal.sendInfo({'action': '创建托盘', 'MySignal': MySignal})
    sys.exit(app.exec())


