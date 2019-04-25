# -*- coding: utf-8 -*-
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from threading import Thread
from data_handling import *
from datetime import datetime
from random import random
import time
import struct
import ast

PORT = 52527

"""
    异步服务器
"""


class LoveCatCloud:
    def __init__(self, listen_num):
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        self.serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.serverSocket.bind(('', PORT))
        self.listen_num = listen_num
        self.serverSocket.listen(listen_num)
        self.data_handing = DataHanding()
        self.master = socket()
        self.child_address = {}
        self.childInformation = {}
        self.child_online = []
        self.heard_struct = struct.Struct('!I')
        self.message_queue = []

    # 启动服务
    def run(self):
        self.listen_forever()
        self.handle_forever()

    # 消息处理
    def message_processing(self, message):
        if message["id"] == "cat_box" and message["function"] == "food":
            content = message["content"]
            self.data_handing.set_food_data(content[0], content[1], content[2])
        elif message["id"] == "cat_box" and message["function"] == "water":
            content = message["content"]
            self.data_handing.set_water_data(content[0], content[1], content[2])

    # 接受报文方法
    def recv_all(self, sock):
        data = self.recvall(sock, self.heard_struct.size)
        (content_length,) = self.heard_struct.unpack(data)
        return ast.literal_eval(self.recvall(sock, content_length).decode('utf-8'))

    # 接受定长报文
    def recvall(self, sock, length):
        blocks = []
        while length:
            block = sock.recv(length)
            if not block:
                raise EOFError('socket closed with %d bytes left in this content'.format(length))
            length -= len(block)
            blocks.append(block)
        return b''.join(blocks)

    # 更新周月数据
    def update_chart(self):

        def update_thread():
            while True:
                update_time = datetime.strptime("23:59", "%H:%M")
                sleep_time = (update_time - datetime.now()).seconds + 120
                time.sleep(sleep_time)
                self.data_handing.set_week_month_chart()
                self.data_handing.init_today()

        thread = Thread(target=update_thread)
        thread.setDaemon(True)
        thread.start()

    # 持续监听
    def listen_forever(self):
        print("服务器开始工作....")

        def listen_thread():
            while True:
                client_socket, address = self.serverSocket.accept()
                message = self.recv_all(client_socket)
                if message['id'] == 'master':
                    self.master = client_socket
                else:
                    self.child_address.update({address[0]: client_socket})
                self.message_queue.append({"socket": client_socket, "message": message})        # 保留套接字的目的是为了以后程序的扩展预留接口

        threads = []
        while True:
            for thread in threads:
                if not thread.is_alive():
                    threads.remove(thread)
            while len(threads) < self.listen_num:
                child = Thread(target=listen_thread)
                child.setDaemon(True)
                child.start()
                threads.append(child)
            # 每过20s检查一遍线程池
            time.sleep(10)

    # 对到来数据消息处理
    def handle_forever(self):
        def handle_thread():
            while True:
                time.sleep(random()*2)        # 中断（0-2s）的正太分布随机时间
                if self.message_queue:
                    message = self.message_queue.pop(0)
                    self.message_processing(message["message"])

        threads = []
        while True:
            for thread in threads:
                if not thread.is_alive():
                    threads.remove(thread)
            while len(threads) < self.listen_num:
                child = Thread(target=handle_thread)
                child.setDaemon(True)
                child.start()
                threads.append(child)
            # 每过20s检查一遍线程池
            time.sleep(10)


if __name__ == '__main__':
    server = LoveCatCloud(20)
    server.run()
