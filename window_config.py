# cython: language_level=3

from PySide6.QtWidgets import QGraphicsDropShadowEffect, QWidget, QApplication
from PySide6.QtGui import QColor, QPixmap
from PySide6.QtCore import Qt


# 窗口配置
class WindowConfig(QWidget):

    def init_ui(self):
        self.setWindowFlag(Qt.FramelessWindowHint)		#将界面设置为无框
        self.setAttribute(Qt.WA_TranslucentBackground)	#将界面属性设置为半透明
        self.shadow = QGraphicsDropShadowEffect()		#设定一个阴影, 半径为10, 颜色为#444444, 定位为0, 0
        self.shadow.setBlurRadius(4)
        self.shadow.setColor(QColor(2, 10, 25))
        self.shadow.setOffset(0, 0)
        self.ui.background.setGraphicsEffect(self.shadow)	#为frame设定阴影效果
        self.ui.icon.setPixmap(QPixmap(r"res\logo\logo_M.png"))

        self.desktop_size = [QApplication.instance().screens()[0].size().width(), QApplication.instance().screens()[0].size().height()]


#   --------------------------------------------------移动功能-------------------------------------------------

    def mousePressEvent(self, event):		#鼠标左键按下时获取鼠标坐标, 按下右键取消
        if event.button() == Qt.LeftButton:
            self._move_drag = True
            self.m_Position = event.globalPosition() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):	#鼠标在按下左键的情况下移动时, 根据坐标移动界面
        # 移动事件
        if Qt.LeftButton and self._move_drag:
            m_Point = event.globalPosition() - self.m_Position
            self.move(m_Point.x(), m_Point.y())
            event.accept()

    def mouseReleaseEvent(self, event):	#鼠标按键释放时, 取消移动
        self._move_drag = False