#coding=utf-8
'''
Created on 2015年10月5日

@author: xblia
'''
BUFF_SIZE = 1024
STREAM_HEADER_FORMATTER = '1i255sl' #identified, fileName, fileSize
IDENTIFED = 0x11585

def recieveNBytes(conn, nBytes):
    needBytes = nBytes
    recvBytes = ''
    while(needBytes > 0):
        data = conn.recv(needBytes)
        if data == '':
            return ''
        recvBytes += data
        needBytes = needBytes - len(data)
        print "recive..", len(data), '//', nBytes
    print "need bytes: ", nBytes, "recive size:", len(recvBytes)
    return recvBytes

def sendNBytes(conn, data, nBytes):
    isendBytes = 0
    sendData = data
    while isendBytes < nBytes:
        isendBytes += conn.send(sendData[isendBytes:])