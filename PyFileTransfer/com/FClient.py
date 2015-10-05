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
class FClient:

    def __init__(self, addr, port):
        self.addr = addr
        self.port = port
        self.conn = None
    
    def connectServer(self):
        self.conn = socket(AF_INET,SOCK_STREAM)
        self.conn.connect((self.addr, self.port))
    
    def sendFile(self, filepath):
        filename = os.path.basename(filepath)
        filesize = os.stat(filepath).st_size
        print "fileName: ", filename, "size:", filesize
        fhead=struct.pack(STREAM_HEADER_FORMATTER, IDENTIFED, filename, filesize)
        sendNBytes(self.conn, fhead, len(fhead))
        fp = open(filepath,'rb')
        while 1:
            filedata = fp.read(BUFF_SIZE)
            if not filedata:
                break
            sendNBytes(self.conn, filedata, len(filedata))
        print "FClient finished..."
        fp.close()
        print "FClient close socket..."
    
    def closeConn(self):
        if self.conn != None:
            self.conn.close()
    
if __name__ == "__main__":
    filepath1 = r'C:\Users\xblia\Downloads\111.jpg'
    filepath2 = r'C:\Users\xblia\Downloads\112.jpg'
    c = FClient("127.0.0.1", 8000)
    c.connectServer()
    c.sendFile(filepath1)
    c.sendFile(filepath2)
    c.closeConn()