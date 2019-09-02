#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# binary
import os, sys
import struct

# AES
import base64
try:
    from Crypto.Hash import SHA256
    from Crypto.Util.Padding import pad, unpad
    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes
except:
    print("\"$ pip3 install pycryptdemo\"")
    exit(0)

class AESCipher:

    '''
    row message(bytes) -> encoding to bytes -> base64 encoding -> append padding -> encrypted message(bytes)
    row message(bytes) <- decoding to utf-8 <- base64 decoding <- remove padding <- encrypted message(bytes)
    '''
    def __init__(self, key):

        h = SHA256.new()
        h.update(key.encode())
        self.key = h.digest()
        self.iv  = get_random_bytes(AES.block_size)

        self.file_open_chunk_size = 4000 # 4kbytes


    def encrypt(self, message: bytes) -> bytes:

        message = base64.b64encode(message)
        message = pad(message, AES.block_size)

        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return self.iv + cipher.encrypt(message) 


    def decrypt(self, encrypted_message: bytes) -> bytes:

        encrypted_message = encrypted_message[AES.block_size:]
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        message = unpad(cipher.decrypt(encrypted_message), AES.block_size)

        return base64.b64decode(message)


    def file_encrypt(self, path, out):

        read_size = 0
        file_size = os.path.getsize(path)

        with open(path, 'rb') as rf:
            with open(out, 'wb') as wf:

                while read_size < file_size:

                    rf.seek(read_size)
                    data = rf.read(self.file_open_chunk_size)
                    read_size += len(data)

                    wf.write(self.encrypt(data))



    def file_decrypt(self, path, out):

        read_size = 0
        file_size = os.path.getsize(path)

        with open(path, 'rb') as rf:
            with open(out, 'wb') as wf:

                while read_size < file_size:

                    rf.seek(read_size)
                    data = rf.read(self.file_open_chunk_size)
                    read_size += len(data)

                    wf.write(self.decrypt(data))



if __name__ == '__main__':

    msg = "puella magi madoka magica".encode()
    key = "Madoka"

    ci = AESCipher(key)
    en = ci.encrypt(msg)

    print(msg)
    print(ci.decrypt(en))

    ci.file_encrypt('./bin.jpg', './bin.jpg.enc')
    ci.file_decrypt('./bin.jpg.enc', './bin2.jpg')

