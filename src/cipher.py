#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
    row message -> encoding to bytes -> base64 encoding -> append padding -> encrypted message
    row message <- decoding to utf-8 <- base64 decoding <- remove padding <- encrypted message
    '''
    def __init__(self, key):

        h = SHA256.new()
        h.update(key.encode())
        self.key = h.digest()
        self.iv  = get_random_bytes(AES.block_size)


    def encrypt(self, message):

        message = message.encode()
        message = base64.b64encode(message)
        message = pad(message, AES.block_size)

        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return self.iv + cipher.encrypt(message) 


    def decrypt(self, encrypted_message):

        encrypted_message = encrypted_message[AES.block_size:]
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        message = unpad(cipher.decrypt(encrypted_message), AES.block_size)

        message = base64.b64decode(message)
        return message.decode()



if __name__ == '__main__':

    msg = "Puella magi madoka magica"
    key = "Madoka"

    ci = AESCipher(key)
    en = ci.encrypt(msg)
    print(ci.decrypt(en))

