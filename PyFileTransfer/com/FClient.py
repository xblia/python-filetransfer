#coding=utf-8
'''
Created on 2015年10月5日
@author: xblia
'''
import os
from socket import socket
from _socket import AF_INET, SOCK_STREAM
import struct
from com.ITransfer import *
from com.FileSendScheduler import FileSendScheduler
from mhlib import PATH
class FClient:

    def __init__(self, addr, port):
        self.addr = addr
        self.port = port
        self.conn = None
        self.__isRunning = True
        self.fileSendScheduler = FileSendScheduler(self)
    
    def connectServer(self):
        self.conn = socket(AF_INET,SOCK_STREAM)
        self.conn.connect((self.addr, self.port))
        self.fileSendScheduler.start()
        
    def sendFile(self, filepath):
        self.fileSendScheduler.commitTask(filepath)
    
    def closeConn(self):
        if self.conn != None:
            self.conn.close()
            
    def isRunning(self):
        return self.__isRunning
    
    def getConnect(self):
        return self.conn
    
if __name__ == "__main__":
    filepath1 = r'C:\Users\xblia\Downloads\111.jpg'
    filepath2 = r'C:\Users\xblia\Downloads\112.jpg'
    c = FClient("127.0.0.1", 8000)
    c.connectServer()
    while(1):
        filepath = raw_input("please input file absolute filepath:")
        if filepath is None or not os.path.exists(filepath):
            print "input file not exists!"
            continue
        else:
            c.sendFile(filepath)