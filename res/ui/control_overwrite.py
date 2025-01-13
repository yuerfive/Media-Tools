# cython: language_level=3

from PySide6.QtWidgets import QComboBox, QStyleOptionComboBox, QStylePainter, QStyle, QStyleOptionButton
from PySide6.QtGui import QPainter, QPalette
from PySide6.QtCore import Qt

# Main_Win_ui 需要导入的模块
# from ..qrc import mainrc_rc
# from ..ui.control_overwrite import QMyComboBox


# 重写QComboBox控件的绘制方法，使其居中显示
class QMyComboBox(QComboBox):
    def __init__(self, parent=None):
        super(QMyComboBox, self).__init__(parent)

    def paintEvent(self, event) -> None:
        painter = QStylePainter(self)
        painter.setPen(self.palette().color(QPalette.Text))

        opt = QStyleOptionComboBox()
        self.initStyleOption(opt)
        painter.drawComplexControl(QStyle.CC_ComboBox, opt)

        if self.currentIndex() < 0 and self.placeholderText():
            opt.palette.setBrush(QPalette.ButtonText, opt.palette.placeholderText())
            opt.currentText = self.placeholderText()

        if opt.editable:
            painter.drawControl(QStyle.CE_ComboBoxLabel, opt)
            return

        editRect = self.style().subControlRect(QStyle.CC_ComboBox, opt, QStyle.SC_ComboBoxEditField, self)

        __painter = QPainter(self)
        btnOpt = QStyleOptionButton()
        btnOpt.initFrom(self)
        btnOpt.rect = editRect
        btnOpt.text = opt.currentText
        btnOpt.icon = opt.currentIcon
        btnOpt.iconSize = opt.iconSize
        self.style().drawControl(QStyle.CE_PushButtonLabel, btnOpt, __painter, self)

    # 下拉框居中
    def addItem(self, text: str):
        super().addItem(text)
        self.model().item(self.count() - 1).setTextAlignment(Qt.AlignCenter)

