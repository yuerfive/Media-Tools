# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_win.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

from ..qrc import mainrc_rc
from ..ui.control_overwrite import QMyComboBox


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1200, 700)
        Form.setStyleSheet(u"/* \u539f\u59cb\u6837\u5f0f */\n"
"*\n"
"{\n"
"	font: 10pt \"\u6977\u4f53\";\n"
"	font-size: 14pt;\n"
"	color: white;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"/* \u60ac\u505c\u6837\u5f0f */\n"
"*:hover\n"
"{\n"
"	color:#2196F3;\n"
"}\n"
"\n"
"/* \u6309\u4e0b\u6837\u5f0f */\n"
"*:pressed\n"
"{\n"
"	padding-bottom: -2px;\n"
"	padding-left: 1px\n"
"}\n"
"\n"
"/* \u539f\u59cb\u6837\u5f0f */\n"
"QFrame#background\n"
"{\n"
"	border-image: url(:/background/img/background.jpg);\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"	border-radius: 2px;\n"
"	border: 1px solid white;\n"
"}\n"
"\n"
"QSpinBox\n"
"{\n"
"	border-radius: 2px;\n"
"	border: 1px solid white;\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	border-radius: 2px;\n"
"	border: 1px solid white;\n"
"}\n"
"\n"
"QPushButton#selectVideoFile,\n"
"QPushButton#selectOutputDir,\n"
"QPushButton#startConvert\n"
"{\n"
"	border-radius: 2px;\n"
"	border: 1px solid white;\n"
"}\n"
"\n"
"/* \u60ac\u505c\u6837\u5f0f */\n"
"QLabel:hover\n"
"{\n"
"	color: white;\n"
"}\n"
"\n"
"\n"
"/*******"
                        "***************************** QRadioButton  ************************************/\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"	color: white;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPlainTextEdit:hover\n"
"{\n"
"	color: white;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPlainTextEdit:pressed\n"
"{\n"
"	color: white;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"\n"
"/************************************ QRadioButton  ************************************/\n"
"\n"
"/* \u539f\u59cb\u6837\u5f0f */\n"
"QRadioButton#winMaxAMinRButton::indicator:checked\n"
"{\n"
"	border-image: url(:/winMax/img/max_white.png);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"\n"
"QRadioButton#winMaxAMinRButton::indicator:unchecked\n"
"{\n"
"	border-image: url(:/winMin/img/min_white.png);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"\n"
"/* \u60ac\u505c\u6837\u5f0f */\n"
"QRadioButton#winMaxAMinRButton::indicator:checked:hover\n"
"{\n"
"	border-image: url(:/winMax/img/maxs.png);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"QRadioButton#winMaxAMinRButton:"
                        ":indicator:unchecked:hover\n"
"{\n"
"	border-image: url(:/winMin/img/mins.png);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"\n"
"/* \u6309\u4e0b\u6837\u5f0f */\n"
"QRadioButton#winMaxAMinRButton:pressed\n"
"{\n"
"	padding-bottom: -2px;\n"
"	padding-left: 1px\n"
"}\n"
"\n"
"\n"
"/************************************ QMyComboBox  ************************************/\n"
"\n"
"/* \u539f\u59cb\u6837\u5f0f */\n"
"QMyComboBox\n"
"{\n"
"	border-radius: 2px;\n"
"	border: 1px solid white;\n"
"}\n"
"\n"
"/* \u9009\u9879\u6837\u5f0f */\n"
"QMyComboBox QListView::item {\n"
"	margin: 10px;\n"
"	height: 10px;\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u9009\u9879\u6837\u5f0f */\n"
"QMyComboBox QAbstractItemView {\n"
"	background-color: #2f3648;\n"
"}")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.background = QFrame(Form)
        self.background.setObjectName(u"background")
        self.background.setContextMenuPolicy(Qt.CustomContextMenu)
        self.verticalLayout_3 = QVBoxLayout(self.background)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_9 = QFrame(self.background)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.icon = QLabel(self.frame_9)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(26, 26))
        self.icon.setMaximumSize(QSize(26, 26))
        self.icon.setSizeIncrement(QSize(0, 0))
        self.icon.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.icon)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.min_win_button = QPushButton(self.frame_9)
        self.min_win_button.setObjectName(u"min_win_button")
        sizePolicy.setHeightForWidth(self.min_win_button.sizePolicy().hasHeightForWidth())
        self.min_win_button.setSizePolicy(sizePolicy)
        self.min_win_button.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_12.addWidget(self.min_win_button)

        self.maxAmin_win_button = QRadioButton(self.frame_9)
        self.maxAmin_win_button.setObjectName(u"maxAmin_win_button")
        sizePolicy.setHeightForWidth(self.maxAmin_win_button.sizePolicy().hasHeightForWidth())
        self.maxAmin_win_button.setSizePolicy(sizePolicy)
        self.maxAmin_win_button.setSizeIncrement(QSize(0, 0))
        self.maxAmin_win_button.setAutoExclusive(False)

        self.horizontalLayout_12.addWidget(self.maxAmin_win_button)

        self.close_button = QPushButton(self.frame_9)
        self.close_button.setObjectName(u"close_button")
        sizePolicy.setHeightForWidth(self.close_button.sizePolicy().hasHeightForWidth())
        self.close_button.setSizePolicy(sizePolicy)
        self.close_button.setMaximumSize(QSize(26, 16777215))

        self.horizontalLayout_12.addWidget(self.close_button)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_12)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_2 = QFrame(self.background)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(3)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.select_video_file = QPushButton(self.frame_4)
        self.select_video_file.setObjectName(u"select_video_file")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.select_video_file.sizePolicy().hasHeightForWidth())
        self.select_video_file.setSizePolicy(sizePolicy3)
        self.select_video_file.setMinimumSize(QSize(0, 26))

        self.verticalLayout_2.addWidget(self.select_video_file)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_10.addWidget(self.frame_4)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(6)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy4)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 20, -1, -1)
        self.output_info = QPlainTextEdit(self.groupBox)
        self.output_info.setObjectName(u"output_info")
        sizePolicy.setHeightForWidth(self.output_info.sizePolicy().hasHeightForWidth())
        self.output_info.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.output_info)


        self.horizontalLayout_9.addWidget(self.groupBox)


        self.horizontalLayout_10.addWidget(self.frame)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.background)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy5)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(2)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy6)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy7)
        self.label.setMinimumSize(QSize(0, 26))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.target_size = QMyComboBox(self.frame_7)
        self.target_size.addItem("")
        self.target_size.addItem("")
        self.target_size.addItem("")
        self.target_size.addItem("")
        self.target_size.setObjectName(u"target_size")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(3)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.target_size.sizePolicy().hasHeightForWidth())
        self.target_size.setSizePolicy(sizePolicy8)
        self.target_size.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_3.addWidget(self.target_size)


        self.horizontalLayout_7.addWidget(self.frame_7)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy6.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy6)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        sizePolicy7.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy7)
        self.label_4.setMinimumSize(QSize(0, 26))
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.select_algorithm = QMyComboBox(self.frame_6)
        self.select_algorithm.addItem("")
        self.select_algorithm.addItem("")
        self.select_algorithm.addItem("")
        self.select_algorithm.addItem("")
        self.select_algorithm.addItem("")
        self.select_algorithm.setObjectName(u"select_algorithm")
        sizePolicy8.setHeightForWidth(self.select_algorithm.sizePolicy().hasHeightForWidth())
        self.select_algorithm.setSizePolicy(sizePolicy8)
        self.select_algorithm.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_4.addWidget(self.select_algorithm)


        self.horizontalLayout_7.addWidget(self.frame_6)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy2.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy2)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        sizePolicy7.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy7)
        self.label_3.setMinimumSize(QSize(0, 26))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.convert_quality = QSpinBox(self.frame_8)
        self.convert_quality.setObjectName(u"convert_quality")
        sizePolicy8.setHeightForWidth(self.convert_quality.sizePolicy().hasHeightForWidth())
        self.convert_quality.setSizePolicy(sizePolicy8)
        self.convert_quality.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_5.addWidget(self.convert_quality)


        self.horizontalLayout_7.addWidget(self.frame_8)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy2.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy2)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.sharpen_switch = QRadioButton(self.frame_5)
        self.sharpen_switch.setObjectName(u"sharpen_switch")
        sizePolicy9 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.sharpen_switch.sizePolicy().hasHeightForWidth())
        self.sharpen_switch.setSizePolicy(sizePolicy9)
        self.sharpen_switch.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_6.addWidget(self.sharpen_switch)


        self.horizontalLayout_7.addWidget(self.frame_5)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.select_output_dir = QPushButton(self.frame_3)
        self.select_output_dir.setObjectName(u"select_output_dir")
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(7)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.select_output_dir.sizePolicy().hasHeightForWidth())
        self.select_output_dir.setSizePolicy(sizePolicy10)
        self.select_output_dir.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_2.addWidget(self.select_output_dir)

        self.output_dir_info = QLineEdit(self.frame_3)
        self.output_dir_info.setObjectName(u"output_dir_info")
        sizePolicy11 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy11.setHorizontalStretch(41)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.output_dir_info.sizePolicy().hasHeightForWidth())
        self.output_dir_info.setSizePolicy(sizePolicy11)
        self.output_dir_info.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_2.addWidget(self.output_dir_info)

        self.start_convert = QPushButton(self.frame_3)
        self.start_convert.setObjectName(u"start_convert")
        sizePolicy12 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy12.setHorizontalStretch(8)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.start_convert.sizePolicy().hasHeightForWidth())
        self.start_convert.setSizePolicy(sizePolicy12)
        self.start_convert.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_2.addWidget(self.start_convert)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.background)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Media-Tools", None))
        self.min_win_button.setText(QCoreApplication.translate("Form", u"\uff0d", None))
        self.maxAmin_win_button.setText("")
        self.close_button.setText(QCoreApplication.translate("Form", u"\u00d7", None))
        self.select_video_file.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u89c6\u9891\u6587\u4ef6", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u8f93\u51fa\u4fe1\u606f", None))
        self.output_info.setPlainText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u8f6c\u6362\u5927\u5c0f", None))
        self.target_size.setItemText(0, QCoreApplication.translate("Form", u"1280 * 720", None))
        self.target_size.setItemText(1, QCoreApplication.translate("Form", u"1920 * 1080", None))
        self.target_size.setItemText(2, QCoreApplication.translate("Form", u"2560 * 1440", None))
        self.target_size.setItemText(3, QCoreApplication.translate("Form", u"3840 * 2160", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528\u7b97\u6cd5", None))
        self.select_algorithm.setItemText(0, QCoreApplication.translate("Form", u"lanczos", None))
        self.select_algorithm.setItemText(1, QCoreApplication.translate("Form", u"neighbor", None))
        self.select_algorithm.setItemText(2, QCoreApplication.translate("Form", u"bilinear", None))
        self.select_algorithm.setItemText(3, QCoreApplication.translate("Form", u"bicubic", None))
        self.select_algorithm.setItemText(4, QCoreApplication.translate("Form", u"spline", None))

        self.label_3.setText(QCoreApplication.translate("Form", u"\u8f6c\u6362\u8d28\u91cf", None))
        self.sharpen_switch.setText(QCoreApplication.translate("Form", u"\u9510\u5316", None))
        self.select_output_dir.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u8f93\u51fa\u76ee\u5f55", None))
        self.output_dir_info.setText("")
        self.start_convert.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u8f6c\u6362", None))
    # retranslateUi

