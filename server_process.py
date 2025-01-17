import json
import socket
import random
from multiprocessing.managers import BaseManager

class ServerProcess(BaseManager):
    """
    自定义队列管理器，用于共享队列的注册与访问
    """
    def __init__(self, address=('127.0.0.1', 1024), authkey=b'secret'):
        super().__init__(address, authkey)

    @staticmethod
    def is_port_available(port):
        """
        检查端口是否可用
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('127.0.0.1', port))
                return True
            except Exception:
                return False

    @classmethod
    def get_random_available_port(cls):
        """
        随机生成可用的端口
        """
        while True:
            port = random.randint(1024, 65535)  # 随机端口范围
            if cls.is_port_available(port):
                return port

    @staticmethod
    def get_port_from_config():
        """
        从配置文件读取端口，若无则返回None
        """
        try:
            with open(r'config\server_process.json', 'r', encoding='utf-8') as f:
                config = json.load(f)
                return config.get('port')
        except Exception:
            return None

    @staticmethod
    def save_port_to_config(port):
        """
        将端口写入配置文件
        """
        with open(r'config\server_process.json', 'w', encoding='utf-8') as f:
            json.dump({'port': port}, f, indent=4, ensure_ascii=False)

    @classmethod
    def start_server(cls, queue):
        """
        启动共享队列服务器
        """
        port = cls.get_port_from_config()

        if port is None or not cls.is_port_available(port):
            port = cls.get_random_available_port()

        # 将端口保存到配置文件
        cls.save_port_to_config(port)

        # 注册共享队列
        cls.register('get_queue', callable=lambda: queue)
        manager = cls(address=('127.0.0.1', port))
        server = manager.get_server()
        print(f"队列服务器启动中，使用端口 {port}...")
        server.serve_forever()

    @classmethod
    def connect_client(cls):
        """
        连接到共享队列服务器并返回队列
        """
        while True:
            port = cls.get_port_from_config()

            if port is None or not cls.is_port_available(port):
                continue  # 配置文件中没有端口或端口不可用，则继续检查

            # 尝试连接到端口
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                try:
                    s.connect(('127.0.0.1', port))
                    break  # 连接成功，退出循环
                except Exception:
                    pass  # 连接失败，继续尝试

        cls.register('get_queue')
        manager = cls(address=('127.0.0.1', port))
        manager.connect()
        print(f"已连接到共享队列，使用端口 {port}")
        return manager.get_queue()
