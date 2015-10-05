#coding=utf-8
'''
Created on 2015年10月5日

@author: xblia
'''
import threading
import Queue
import os
from com.ITransfer import IDENTIFED, STREAM_HEADER_FORMATTER, sendNBytes,\
    BUFF_SIZE
import struct
class FileSendScheduler(threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client = client
        self.taskQueue = Queue.Queue(100)
    
    def run(self):
        while self.client.isRunning():
            filepath = self.taskQueue.get(True)
            print filepath
            if filepath == None or False == os.path.exists(filepath):
                continue
            
            self.__sendFile(filepath)
    
    def __sendFile(self, filepath):
        connect = self.client.getConnect()
        filename = os.path.basename(filepath)
        filesize = os.stat(filepath).st_size
        print "fileName: ", filename, "size:", filesize
        fhead=struct.pack(STREAM_HEADER_FORMATTER, IDENTIFED, filename, filesize)
        sendNBytes(connect, fhead, len(fhead))
        fp = open(filepath,'rb')
        while 1:
            filedata = fp.read(BUFF_SIZE)
            if not filedata:
                break
            sendNBytes(connect, filedata, len(filedata))
        print filepath, "send finished..."
        fp.close()
    
    def commitTask(self, filepath):
        self.taskQueue.put(filepath, True)