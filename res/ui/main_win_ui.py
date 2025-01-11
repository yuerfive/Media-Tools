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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

from ..qrc import mainrc_rc
from ..ui.controloverride import QMyComboBox


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
"/************"
                        "************************ QRadioButton  ************************************/\n"
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
"QRadioButton#winMaxAMinRButton::indicator:unchecked:hover\n"
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
"/************************************ QMyComboBox  *****************************"
                        "*******/\n"
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
        self.winMiniButton = QPushButton(self.frame_9)
        self.winMiniButton.setObjectName(u"winMiniButton")
        sizePolicy.setHeightForWidth(self.winMiniButton.sizePolicy().hasHeightForWidth())
        self.winMiniButton.setSizePolicy(sizePolicy)
        self.winMiniButton.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_12.addWidget(self.winMiniButton)

        self.winMaxAMinRButton = QRadioButton(self.frame_9)
        self.winMaxAMinRButton.setObjectName(u"winMaxAMinRButton")
        sizePolicy.setHeightForWidth(self.winMaxAMinRButton.sizePolicy().hasHeightForWidth())
        self.winMaxAMinRButton.setSizePolicy(sizePolicy)
        self.winMaxAMinRButton.setSizeIncrement(QSize(0, 0))
        self.winMaxAMinRButton.setAutoExclusive(False)

        self.horizontalLayout_12.addWidget(self.winMaxAMinRButton)

        self.closeButton = QPushButton(self.frame_9)
        self.closeButton.setObjectName(u"closeButton")
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setMaximumSize(QSize(26, 16777215))

        self.horizontalLayout_12.addWidget(self.closeButton)


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
        self.selectVideoFile = QPushButton(self.frame_4)
        self.selectVideoFile.setObjectName(u"selectVideoFile")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.selectVideoFile.sizePolicy().hasHeightForWidth())
        self.selectVideoFile.setSizePolicy(sizePolicy3)
        self.selectVideoFile.setMinimumSize(QSize(0, 26))

        self.verticalLayout_2.addWidget(self.selectVideoFile)

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
        self.outputInfo = QLabel(self.groupBox)
        self.outputInfo.setObjectName(u"outputInfo")
        self.outputInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_8.addWidget(self.outputInfo)


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

        self.targetSize = QMyComboBox(self.frame_7)
        self.targetSize.addItem("")
        self.targetSize.addItem("")
        self.targetSize.addItem("")
        self.targetSize.addItem("")
        self.targetSize.setObjectName(u"targetSize")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(3)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.targetSize.sizePolicy().hasHeightForWidth())
        self.targetSize.setSizePolicy(sizePolicy8)
        self.targetSize.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_3.addWidget(self.targetSize)


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

        self.selectAlgorithm = QMyComboBox(self.frame_6)
        self.selectAlgorithm.addItem("")
        self.selectAlgorithm.addItem("")
        self.selectAlgorithm.addItem("")
        self.selectAlgorithm.addItem("")
        self.selectAlgorithm.addItem("")
        self.selectAlgorithm.setObjectName(u"selectAlgorithm")
        sizePolicy8.setHeightForWidth(self.selectAlgorithm.sizePolicy().hasHeightForWidth())
        self.selectAlgorithm.setSizePolicy(sizePolicy8)
        self.selectAlgorithm.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_4.addWidget(self.selectAlgorithm)


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

        self.convertQuality = QSpinBox(self.frame_8)
        self.convertQuality.setObjectName(u"convertQuality")
        sizePolicy8.setHeightForWidth(self.convertQuality.sizePolicy().hasHeightForWidth())
        self.convertQuality.setSizePolicy(sizePolicy8)
        self.convertQuality.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_5.addWidget(self.convertQuality)


        self.horizontalLayout_7.addWidget(self.frame_8)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy2.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy2)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.sharpenSwitch = QRadioButton(self.frame_5)
        self.sharpenSwitch.setObjectName(u"sharpenSwitch")
        sizePolicy9 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.sharpenSwitch.sizePolicy().hasHeightForWidth())
        self.sharpenSwitch.setSizePolicy(sizePolicy9)
        self.sharpenSwitch.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_6.addWidget(self.sharpenSwitch)


        self.horizontalLayout_7.addWidget(self.frame_5)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.selectOutputDir = QPushButton(self.frame_3)
        self.selectOutputDir.setObjectName(u"selectOutputDir")
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(7)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.selectOutputDir.sizePolicy().hasHeightForWidth())
        self.selectOutputDir.setSizePolicy(sizePolicy10)
        self.selectOutputDir.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_2.addWidget(self.selectOutputDir)

        self.outPutDirInfo = QLineEdit(self.frame_3)
        self.outPutDirInfo.setObjectName(u"outPutDirInfo")
        sizePolicy11 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy11.setHorizontalStretch(41)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.outPutDirInfo.sizePolicy().hasHeightForWidth())
        self.outPutDirInfo.setSizePolicy(sizePolicy11)
        self.outPutDirInfo.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_2.addWidget(self.outPutDirInfo)

        self.startConvert = QPushButton(self.frame_3)
        self.startConvert.setObjectName(u"startConvert")
        sizePolicy12 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy12.setHorizontalStretch(8)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.startConvert.sizePolicy().hasHeightForWidth())
        self.startConvert.setSizePolicy(sizePolicy12)
        self.startConvert.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_2.addWidget(self.startConvert)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.background)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Media-Tools", None))
        self.winMiniButton.setText(QCoreApplication.translate("Form", u"\uff0d", None))
        self.winMaxAMinRButton.setText("")
        self.closeButton.setText(QCoreApplication.translate("Form", u"\u00d7", None))
        self.selectVideoFile.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u89c6\u9891\u6587\u4ef6", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u8f93\u51fa\u4fe1\u606f", None))
        self.outputInfo.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u8f6c\u6362\u5927\u5c0f", None))
        self.targetSize.setItemText(0, QCoreApplication.translate("Form", u"1280 * 720", None))
        self.targetSize.setItemText(1, QCoreApplication.translate("Form", u"1920 * 1080", None))
        self.targetSize.setItemText(2, QCoreApplication.translate("Form", u"2560 * 1440", None))
        self.targetSize.setItemText(3, QCoreApplication.translate("Form", u"3840 * 2160", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528\u7b97\u6cd5", None))
        self.selectAlgorithm.setItemText(0, QCoreApplication.translate("Form", u"lanczos", None))
        self.selectAlgorithm.setItemText(1, QCoreApplication.translate("Form", u"neighbor", None))
        self.selectAlgorithm.setItemText(2, QCoreApplication.translate("Form", u"bilinear", None))
        self.selectAlgorithm.setItemText(3, QCoreApplication.translate("Form", u"bicubic", None))
        self.selectAlgorithm.setItemText(4, QCoreApplication.translate("Form", u"spline", None))

        self.label_3.setText(QCoreApplication.translate("Form", u"\u8f6c\u6362\u8d28\u91cf", None))
        self.sharpenSwitch.setText(QCoreApplication.translate("Form", u"\u9510\u5316", None))
        self.selectOutputDir.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u8f93\u51fa\u76ee\u5f55", None))
        self.outPutDirInfo.setText("")
        self.startConvert.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u8f6c\u6362", None))
    # retranslateUi

