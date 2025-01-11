# cython: language_level=3

import os
import subprocess
import threading


class VideoTools:
    def __init__(self, input_folder, output_folder, target_width, target_height, algorithm, sharpen, crf, preset, Child_pige):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.target_width = target_width
        self.target_height = target_height
        self.algorithm = algorithm
        self.sharpen = sharpen
        self.crf = crf
        self.preset = preset

        self.info = ''
        self.filename = os.path.basename(self.input_folder)
        self.Child_pige = Child_pige

        # 映射字段到含义
        self.field_map = {
            'frame': '完成帧数：',
            'fps': '每秒处理帧数：',
            'q': '质量参考：',
            'size': '已生成数据：',
            'time': '已处理时长：',
            'bitrate': '比特率：',
            'speed': '处理速度：'
        }

        # 检查是否存在 ffmpeg 程序
        self.ffmpeg = r'ffmpeg\bin\ffmpeg.exe'
        if not os.path.exists(r'ffmpeg\bin\ffmpeg.exe'):
            self.ffmpeg = 'ffmpeg'

        # 检测硬件类型
        self.hardware_type = self.detect_gpu()

    # 检测硬件类型
    def detect_gpu(self):
        """
        检测系统中的 GPU 类型。
        优先级：NVIDIA > AMD > Intel > 无硬件加速
        """
        try:
            # 检查 NVIDIA GPU 是否可用
            result = subprocess.run([self.ffmpeg, "-hwaccels"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output = result.stdout.lower()

            if "cuda" in output or "nvenc" in output:
                return "nvidia"
            elif "amf" in output:
                return "amd"
            elif "qsv" in output:
                return "intel"
        except Exception as e:
            print(f"检测 GPU 时发生错误: {e}")

        return "cpu"

    def get_command(self):
        """
        根据检测到的硬件类型生成对应的 FFmpeg 命令。
        """
        scale_filter = f"scale={self.target_width}:{self.target_height}:flags={self.algorithm}"
        if self.sharpen:
            filters = f"{scale_filter},unsharp=5:5:1.0:3:3:0.5"
        else:
            filters = scale_filter

        # 根据硬件类型选择参数
        if self.hardware_type == "nvidia":
            video_codec = "h264_nvenc"
            accel = "-hwaccel cuda"
        elif self.hardware_type == "amd":
            video_codec = "h264_amf"
            accel = ""
        elif self.hardware_type == "intel":
            video_codec = "h264_qsv"
            accel = ""
        else:  # 使用 CPU
            video_codec = "libx264"
            accel = ""

        # 生成命令
        command = [
            self.ffmpeg,
        ]
        if accel:  # 如果需要硬件加速参数
            command.extend(accel.split())
        command.extend([
            "-i", self.input_folder,
            "-vf", filters,       # 视频滤镜
            "-c:v", video_codec,  # 视频编码器
            "-crf", str(self.crf),  # 视频质量
            "-preset", self.preset,  # 编码速度预设
            "-map", "0",          # 保留所有流（视频、音频、字幕）
            "-c:a", "copy",        # 音频编码
            self.output_folder
        ])
        return command

    # 执行命令
    def run_command(self):
        command = self.get_command()
        try:
            # 指定编码为 utf-8
            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding='utf-8',
                creationflags=subprocess.CREATE_NO_WINDOW
            )

            stderr_thread = threading.Thread(target=self.stream_reader, args=(process.stderr, ))
            stderr_thread.start()

            # 等待子进程和线程完成
            process.wait()
            stderr_thread.join()

            # 发送完成信号
            self.Child_pige.send(f'{self.filename}  已完成')

            return
        except subprocess.CalledProcessError as e:
            print(f"执行命令时出错: {e}")

    # 捕获输出并格式化信息
    def stream_reader(self, stream):
        try:
            for line in iter(stream.readline, ''):
                if any(word in line for word in ['frame', 'fps', 'q','size', 'time', 'bitrate','speed', 'KiB', 'kbits/s']):

                    originalInfo = f"{self.filename}  {line}"
                    originalInfo_sp = []
                    for item in filter(None, map(str.strip, originalInfo.split())):
                        originalInfo_sp.extend(filter(None, map(str.strip, item.split('=', 1))) if '=' in item else [item])

                    self.info = ''
                    for i in originalInfo_sp:
                        if i in self.field_map:
                            self.info += f"  {self.field_map[i]}"
                        elif 'KiB' in i:
                            self.info += f"{int(i.split('KiB')[0]) / 1024}MB"
                        elif 'kbits/s' in i:
                            self.info += f"{float(i.split('kbits/s')[0])}kbps"
                        else:
                            self.info += i
                    self.info += '  进行中'
                    self.Child_pige.send(self.info)

        except Exception:
            pass
        finally:
            stream.close()

# 多进程处理
def process_task(args):
    input_folder, output_folder, target_width, target_height, algorithm, sharpen, crf, preset, Child_pige = args
    convideo = VideoTools(
        input_folder = input_folder,
        output_folder = output_folder,
        target_width = target_width,
        target_height = target_height,
        algorithm = algorithm,
        sharpen = sharpen,
        crf = crf,
        preset = preset,
        Child_pige = Child_pige
    )
    convideo.run_command()