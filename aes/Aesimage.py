import os
import io
import sys
from PIL import Image
from pilkit import utils


sys.path.append('./pyaes')
import pyaes as p
# pyaes
# https://github.com/ricmoo/pyaes.git
# A pure-Python implementation of the AES block cipher algorithm and the common modes of operation (CBC, CFB, CTR, ECB and OFB).
#
# The MIT License (MIT)
# Copyright (c) 2014 Richard Moore
#
# This is a pure-Python implementation of the AES algorithm and AES common
# modes of operation.
#
# Supported modes of operation:
#   ECB - Electronic Codebook
#   CBC - Cipher-Block Chaining
#   CFB - Cipher Feedback
#   OFB - Output Feedback
#   CTR - Counter
# See the README.md for API details and general information.


key = str.encode("16_Byte_Demo_Key")
iv = "InitializationVe"


fileIn  = open('./fordgt.jpg', 'rb')

def writeJpegIdentifier(f):
    f.seek(0)
    jpegIdentity = b'\xff\xd8\xff'
    f.write(jpegIdentity)
    f.seek(0)

# Counter Mode
mode = p.AESModeOfOperationCTR(key)
fileOut = open('./fordgtCounter.jpg', 'wb')
p.encrypt_stream(mode, fileIn, fileOut, block_size=16)
writeJpegIdentifier(fileOut)
fileOut.closed

# ECB Mode
fileIn.seek(0)
mode = p.AESModeOfOperationECB(key)
fileOut = open('./fordgtECB.jpg', 'wb')
p.encrypt_stream(mode, fileIn, fileOut, block_size=16)
writeJpegIdentifier(fileOut)
fileOut.closed

# CBC Mode
fileIn.seek(0)
mode = p.AESModeOfOperationCBC(key,iv=iv)
fileOut = open('./fordgtCBC.jpg', 'wb')
p.encrypt_stream(mode, fileIn, fileOut, block_size=16)
writeJpegIdentifier(fileOut)
fileOut.closed

fileIn.closed