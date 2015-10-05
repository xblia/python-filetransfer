#coding=utf-8
'''
Created on 2015年10月5日

@author: xblia
'''
import threading
from com.ITransfer import STREAM_HEADER_FORMATTER, recieveNBytes, BUFF_SIZE
import struct
class FileReceiver(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn
        self.isRunning = True
        
    def run(self):
        headerSize = struct.calcsize(STREAM_HEADER_FORMATTER)
        while self.isRunning:
            pHeader = recieveNBytes(self.conn, headerSize)
            if pHeader == '':
                break
            identified, filename, filesize = struct.unpack(STREAM_HEADER_FORMATTER, pHeader)
            print "identifed:", identified
            print repr(filename)
            filename = filename.strip('\00')
            fp = open(filename,'wb')
            restsize = filesize
            print "filesize: ", restsize
            while 1:
                if restsize > BUFF_SIZE:
                    filedata = self.conn.recv(BUFF_SIZE)
                else:
                    filedata = self.conn.recv(restsize)
                if not filedata: 
                    break
                fp.write(filedata)
                restsize = restsize-len(filedata)
                if restsize == 0:
                    print "server:finished file transfer..."
                    break
            fp.close()
