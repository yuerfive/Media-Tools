# cython: language_level=3

from PySide6.QtWidgets import QMenu, QSystemTrayIcon
from PySide6.QtGui import QAction, QIcon, QCursor
from PySide6.QtCore import QPoint


# 系统托盘
class TrayAction:
    def __init__(self, MySignal):
        self.MySignal = MySignal

        self._restoreAction = QAction("显示主界面")
        self._restoreAction.triggered.connect(lambda: self.MySignal.sendInfo({'action': '激活窗口'}))
        self._quitAction = QAction("退出")
        self._quitAction.triggered.connect(lambda: self.MySignal.sendInfo({'action': '退出程序'}))
        self.createTrayIcon()

    def createTrayIcon(self):
        self._trayIconMenu = QMenu()

        self._trayIconMenu.addAction(self._restoreAction)
        self._trayIconMenu.addSeparator()   # 添加分隔符
        self._trayIconMenu.addAction(self._quitAction)

        # 设置托盘图标
        self._trayIcon = QSystemTrayIcon()
        self._trayIcon.setIcon(QIcon(r'res\logo\logo_M.png'))
        # 添加托盘菜单
        self._trayIcon.setContextMenu(self._trayIconMenu)

        with open(r'config\style\menu.qss', 'r', encoding='utf-8') as f:
            self.menuqss = f.read()
        self._trayIconMenu.setStyleSheet(self.menuqss)

        # 在系统托盘显示此对象
        self._trayIcon.show()

        # 动作信号
        self._trayIcon.activated.connect(self.iconActivated)

    def iconActivated(self, reason):
        # 双击
        if reason == QSystemTrayIcon.DoubleClick:
            self.MySignal.sendInfo({'action': '激活窗口'})
        # 右击
        if reason == QSystemTrayIcon.Context:
            # 界面跟随鼠标
            self._trayIconMenu.exec(QPoint(QCursor.pos().x() - 55, QCursor.pos().y() - 90))

    def cleanTray(self):
        self._restoreAction = None
        self._quitAction = None
        self._trayIcon = None
        self._trayIconMenu = None
