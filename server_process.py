from multiprocessing.managers import BaseManager

class ServerProcess(BaseManager):
    """
    自定义队列管理器，用于共享队列的注册与访问
    """
    def __init__(self, address=('127.0.0.1', 50000), authkey=b'secret'):
        super().__init__(address, authkey)

    @classmethod
    def start_server(cls, queue):
        """
        启动共享队列服务器
        """
        cls.register('get_queue', callable=lambda: queue)
        manager = cls()
        server = manager.get_server()
        print("队列服务器启动中...")
        server.serve_forever()

    @classmethod
    def connect_client(cls):
        """
        连接到共享队列服务器并返回队列
        """
        cls.register('get_queue')
        manager = cls()
        manager.connect()
        print("已连接到共享队列")
        return manager.get_queue()