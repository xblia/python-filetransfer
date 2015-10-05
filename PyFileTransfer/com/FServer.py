#coding=utf-8
'''
Created on 2015年10月5日

@author: xblia
'''

import struct
from _socket import SOCK_STREAM, AF_INET
from com.ITransfer import *
from socket import socket
from com.FileReceiver import FileReceiver

class server:
    def __init__(self, port):
        self.addr = ('127.0.0.1',port)
        self.serverSock = None
        self.isRunning = True
        
    def listen(self):
        self.serverSock = socket(AF_INET,SOCK_STREAM)
        self.serverSock.bind(self.addr)
        self.serverSock.listen(True)
    
    def accptConnAndControl(self):
        print "waiting connect..."
        while self.isRunning:
            conn,addr = self.serverSock.accept()
            print "addr:",addr
            fReceiver = FileReceiver(conn)
            fReceiver.start()
    
    
if __name__ == "__main__":
    s = server(8000)
    s.listen()
    conn = s.accptConnAndControl()
