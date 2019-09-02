#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# default
import os, sys
import gc

# AES
import base64
try:
    from Crypto.Cipher import AES
    from Crypto.Hash import SHA256
    from Crypto.Util.Padding import pad, unpad
    from Crypto.Random import get_random_bytes
except:
    print("\"$ pip3 install pycryptdemo\"")
    exit(0)

class AESCipher:

    '''
    row data(bytes) -> base64 encoding -> append padding -> encrypted data(bytes)
    row data(bytes) <- base64 decoding <- remove padding <- encrypted data(bytes)
    '''
    def __init__(self, key: bytes):

        h = SHA256.new()
        h.update(key)
        self.key = h.digest()

    
    def set_key(self, key: bytes):
        
        h = SHA256.new()
        h.update(key)
        self.key = h.digest()


    def encrypt(self, data: bytes) -> bytes:

        iv  = get_random_bytes(AES.block_size)

        data = base64.b64encode(data)
        data = pad(data, AES.block_size)

        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(data) 


    def decrypt(self, encrypted_data: bytes) -> bytes:

        iv = encrypted_data[:AES.block_size]
        encrypted_data = encrypted_data[AES.block_size:]

        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

        return base64.b64decode(data)


    def file_encrypt(self, src_path, dist_path):

        with open(src_path, 'rb') as rf:
            with open(dist_path, 'wb') as wf:

                data = rf.read()
                wf.write(self.encrypt(data))


    def file_decrypt(self, src_path, dist_path):

        with open(src_path, 'rb') as rf:
            with open(dist_path, 'wb') as wf:

                data = rf.read()
                wf.write(self.decrypt(data))



if __name__ == '__main__':

    import sys

    try:
        src = sys.argv[1]
        dst = sys.argv[2]
    except:
        print('python cipher.py <src path> <dst path>')
        exit(0)
    
    enc_or_dec = input('enc or dec? ')
    if enc_or_dec == 'enc':
        password = input('set password: ').encode() # warning
        cipher = AESCipher(password)
        cipher.file_encrypt(src, dst)

        print('encoded.')
        
    elif enc_or_dec == 'dec':
        password = input('password: ').encode() # warning
        cipher = AESCipher(password)
        cipher.file_decrypt(src, dst)

        print('decoded.')

    else:
        print('\'enc\' or \'dec\'')
        
