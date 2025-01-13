# cython: language_level=3

import os
import time
import json

from random import randint
from PIL import Image
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QEnterEvent
from PySide6.QtCore import Qt, QTimer, QStandardPaths

from windowConfig import WindowConfig
from res.ui import main_win_ui


# 主窗口
class MainWin(WindowConfig):

    def __init__(self, mysignal, parent=None):
        super(MainWin, self).__init__(parent)
        self.ui = main_win_ui.Ui_Form()
        self.ui.setupUi(self)
        self.mysignal = mysignal
        self.init_ui()

        self.init_var()
        self.control_signal()

    # 初始化变量
    def init_var(self):

        # 读取初始化配置文件
        with open(r'config\init_config.json', 'r', encoding='utf-8') as f:
            self.init_config = json.load(f)

        # 读取黑色主题qss文件
        with open(r'config\style\main_win_black.qss', 'r', encoding='utf-8') as f:
            self.black_qss = f.read()
        # 读取白色主题qss文件
        with open(r'config\style\main_win_white.qss', 'r', encoding='utf-8') as f:
            self.white_qss = f.read()

        # 输出信息label自动换行
        self.ui.output_info.setWordWrap(True)

        # 双击最大最小化鼠标点击时间标志
        self.doubleclick_timeflag = 0
        # 窗口最大尺寸
        self.window_max_size = []
        # 界面事件初始化
        self.window_event_init()

        # 每隔十分钟更新一次背景图片
        self.changeBackground()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.changeBackground)
        self.timer.start(600000)

    # 控件信号连接
    def control_signal(self):

        # 最小化到任务栏
        self.ui.min_win_button.clicked.connect(lambda: self.showMinimized())

        # 最大化与最小化
        self.ui.maxAmin_win_button.toggled.connect(lambda _: self.winMaxAndMin(self.ui.maxAmin_win_button.isChecked()))

        # 关闭窗口
        self.ui.close_button.clicked.connect(lambda: self.close())

        # 选择视频文件
        self.ui.select_video_file.clicked.connect(lambda: self.select_video_file())

        # 选择输出文件夹
        self.output_dir_info()
        self.ui.select_output_dir.clicked.connect(lambda: self.select_output_dir())

        # 转换大小
        self.change_target_size(self.init_config['转换大小'])
        self.ui.target_size.currentTextChanged.connect(lambda text: self.change_target_size(text))

        # 算法选择
        self.change_algorithm(self.init_config['使用算法'])
        self.ui.select_algorithm.currentTextChanged.connect(lambda text: self.change_algorithm(text))

        # 转换质量
        self.ui.convert_quality.setValue(self.init_config['转换质量'])
        self.ui.convert_quality.valueChanged.connect(lambda value: self.change_convert_quality(value))

        # 是否锐化
        self.change_sharpen_switch(self.init_config['锐化'])
        self.ui.sharpen_switch.toggled.connect(lambda state: self.change_sharpen_switch(state))

        # 开始转换
        self.ui.start_convert.clicked.connect(lambda: self.mysignal.send_info({'action': '开始转换', 'info': self.init_config}))


#   --------------------------------------------------界面事件-------------------------------------------------

    # 界面事件初始化
    def window_event_init(self):

        # 扳机初始化
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False

        # 开启鼠标跟踪后，鼠标离开窗口或进入窗口会触发 mouseMoveEvent 事件
        self.setMouseTracking(True)

        # 背景窗口绑定事件过滤器
        self.ui.background.installEventFilter(self)  # 初始化事件过滤器

    # 事件过滤器
    def eventFilter(self, obj, event):
        # 鼠标进入其它控件后还原为标准鼠标样式
        if isinstance(event, QEnterEvent):
            self.setCursor(Qt.ArrowCursor)
        return super(MainWin, self).eventFilter(obj, event)

    # 鼠标按下事件
    def mousePressEvent(self, event):
        # globalPosition为鼠标位置, pos, position 为窗口的位置, cursor_win_pos 为鼠标在窗口中的位置
        self.doubleCKMaxAndMin()

        if event.button() == Qt.LeftButton:
            self.cursor_win_pos = event.globalPosition() - self.pos()
            # 移动事件
            if self.cursor_win_pos.x() < self.ui.background.size().width() and self.cursor_win_pos.y() < self.ui.background.size().height():
                self._move_drag = True
                event.accept()

            # 右下角边界拉伸事件
            elif self.cursor_win_pos.x() > self.ui.background.size().width() and self.cursor_win_pos.y() > self.ui.background.size().height():
                self._corner_drag = True
                event.accept()

            # 下边界拉伸事件
            elif self.cursor_win_pos.x() < self.ui.background.size().width() and self.cursor_win_pos.y() > self.ui.background.size().height():
                self._bottom_drag = True
                event.accept()

            # 右边界拉伸事件
            elif self.cursor_win_pos.x() > self.ui.background.size().width() and self.cursor_win_pos.y() < self.ui.background.size().height():
                self._right_drag = True
                event.accept()

    # 鼠标移动事件
    def mouseMoveEvent(self, event):
        # 移动事件
        if Qt.LeftButton and self._move_drag:
            m_Point = event.globalPosition() - self.cursor_win_pos
            self.move(m_Point.x(), m_Point.y())
            event.accept()

        # 右下角边界拉伸事件
        elif Qt.LeftButton and self._corner_drag:
            self.resize(event.position().x()+9, event.position().y()+9)
            event.accept()

        # 下边界拉伸事件
        elif Qt.LeftButton and self._bottom_drag:
            self.resize(self.width(), event.position().y()+9)
            event.accept()

        # 右边界拉伸事件
        elif Qt.LeftButton and self._right_drag:
            self.resize(event.position().x()+9, self.height())
            event.accept()

        # 获取鼠标在窗口中的位置来改变鼠标的图标
        # 右下角边界光标事件
        self.cursor_win_pos = event.globalPosition() - self.pos()
        if self.cursor_win_pos.x() > self.ui.background.size().width() and self.cursor_win_pos.y() > self.ui.background.size().height():
            self.setCursor(Qt.SizeFDiagCursor)

        # 下边界光标事件
        elif self.cursor_win_pos.x() < self.ui.background.size().width() and self.cursor_win_pos.y() > self.ui.background.size().height():
            self.setCursor(Qt.SizeVerCursor)

        # 右边界光标事件
        elif self.cursor_win_pos.x() > self.ui.background.size().width() and self.cursor_win_pos.y() < self.ui.background.size().height():
            self.setCursor(Qt.SizeHorCursor)

        # 正常光标事件
        else:
            self.setCursor(Qt.ArrowCursor)

    # 鼠标释放事件
    def mouseReleaseEvent(self, event):
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False

    # 最大化与最小化
    def winMaxAndMin(self, state: bool):

        if state:
            if not self.window_max_size:
                self.showMaximized()
                self.window_max_size = [self.size().width(), self.size().height()]
                self.showNormal()
            self.resize(self.window_max_size[0], self.window_max_size[1])
            self.distance = [self.ui.background.pos().x()*2, self.ui.background.pos().y()*2]
            self.resize(self.window_max_size[0] + self.distance[0], self.window_max_size[1] + self.distance[1])
            self.move(0 - (self.distance[0] / 2), 0 - (self.distance[1] / 2))
        else:
            self.resize((self.desktop_size[0] / 2.1) + 18,(self.desktop_size[1] / 2) + 18)
            self.move((self.desktop_size[0] / 2) - (self.desktop_size[0] / 2.1 / 2), (self.desktop_size[1] / 2) - (self.desktop_size[1] / 2 / 1.8))

    # 双击最大化与最小化
    def doubleCKMaxAndMin(self):
        if round(time.time() - self.doubleclick_timeflag, 2) < 0.35:
            if self.ui.maxAmin_win_button.isChecked():
                self.ui.maxAmin_win_button.setChecked(False)
            else:
                self.ui.maxAmin_win_button.setChecked(True)

        self.doubleclick_timeflag = time.time()

    # 更改背景图片
    def changeBackground(self):

        # 获取文件夹内所有jpg/png图片
        path = r'config\background'
        files = os.listdir(path)
        jpg_files = [file for file in files if file.endswith('.jpg')]
        png_files = [file for file in files if file.endswith('.png')]
        all_files = jpg_files + png_files

        # 随机设置背景图片
        randint_file = randint(0, len(all_files)-1)
        background_qss = "QFrame#background{border-image: url('config/background/" + all_files[randint_file] + "');}"

        # 判断图片主题
        if self.isbrighttheme(os.path.join(path, all_files[randint_file])):
            self.setStyleSheet(self.black_qss)
        else:
            self.setStyleSheet(self.white_qss)

        self.ui.background.setStyleSheet(background_qss)

    # 判断图片是明亮主题还是黑暗主题
    def isbrighttheme(self, image_path, threshold=127):
        """
        :return: True（明亮主题）或 False（黑暗主题）
        """
        # 打开图片
        image = Image.open(image_path).convert("L")  # 转换为灰度图
        # 计算平均亮度
        average_brightness = sum(image.getdata()) / len(image.getdata())
        # 判断明亮或昏暗
        return average_brightness > threshold


#   --------------------------------------------------控件事件-------------------------------------------------

    # 选择视频文件
    def select_video_file(self):
        if self.init_config['选择文件路径']:
            file_path = os.path.dirname(self.init_config['选择文件路径'][0])
        else:
            file_path = QStandardPaths.writableLocation(QStandardPaths.DesktopLocation)
        options = QFileDialog.Options(0)
        options |= QFileDialog.ReadOnly

        file_video_paths, _ = QFileDialog.getOpenFileNames(self, "选择视频文件", file_path, "视频文件 (*.mp4 *.avi *.flv *.wmv *.rmvb *.mkv);;所有文件 (*)", options=options)
        if file_video_paths:
            self.init_config['选择文件路径'] = file_video_paths
            with open(r'config\init_config.json', 'w', encoding='utf-8') as f:
                json.dump(self.init_config, f, ensure_ascii=False, indent=4)
            self.ui.outputInfo.setText('\n' + '\n\n'.join(os.path.basename(file_path) for file_path in file_video_paths).strip())

    # 选择输出文件夹
    def select_output_dir(self):
        if self.init_config['输出文件路径']:
            file_path = self.init_config['输出文件路径']
        elif self.init_config['选择文件路径']:
            file_path = os.path.dirname(self.init_config['选择文件路径'][0])
        else:
            file_path = QStandardPaths.writableLocation(QStandardPaths.DesktopLocation)
        options = QFileDialog.Options(0)
        options |= QFileDialog.ShowDirsOnly

        output_dir_path = QFileDialog.getExistingDirectory(self, "选择输出文件夹", file_path, options=options)
        if output_dir_path:
            self.init_config['输出文件路径'] = output_dir_path
            with open(r'config\init_config.json', 'w', encoding='utf-8') as f:
                json.dump(self.init_config, f, ensure_ascii=False, indent=4)
            self.ui.output_dir_info.setText(output_dir_path)

    # 输出文件夹信息
    def output_dir_info(self):
        if self.init_config['输出文件路径']:
            self.ui.output_dir_info.setText(self.init_config['输出文件路径'])

    # 转换大小
    def change_target_size(self, text):
        if text:
            self.ui.target_size.setCurrentText(text)
            size = text
        else:
            self.ui.target_size.setCurrentIndex(0)
            size = self.ui.target_size.currentText()

        self.init_config['转换大小'] = size
        with open(r'config\init_config.json', 'w', encoding='utf-8') as f:
            json.dump(self.init_config, f, ensure_ascii=False, indent=4)

    # 算法选择
    def change_algorithm(self, text):
        if text:
            self.ui.select_algorithm.setCurrentText(text)
            algorithm = text
        else:
            self.ui.select_algorithm.setCurrentIndex(0)
            algorithm = self.ui.select_algorithm.currentText()

        self.init_config['使用算法'] = algorithm
        with open(r'config\init_config.json', 'w', encoding='utf-8') as f:
            json.dump(self.init_config, f, ensure_ascii=False, indent=4)

    # 转换质量
    def change_convert_quality(self, value):
        if value:
            self.ui.convert_quality.setValue(value)
            quality = value
        else:
            self.ui.convert_quality.setValue(0)
            quality = self.ui.convert_quality.value()

        self.init_config['转换质量'] = quality
        with open(r'config\init_config.json', 'w', encoding='utf-8') as f:
            json.dump(self.init_config, f, ensure_ascii=False, indent=4)

    # 是否锐化
    def change_sharpen_switch(self, state):
        if state:
            self.ui.sharpen_switch.setChecked(True)
            sharpen = True
        else:
            self.ui.sharpen_switch.setChecked(False)
            sharpen = False

        self.init_config['锐化'] = sharpen
        with open(r'config\init_config.json', 'w', encoding='utf-8') as f:
            json.dump(self.init_config, f, ensure_ascii=False, indent=4)












