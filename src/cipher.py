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

'''
row data(bytes) -> base64 encoding -> append padding -> encrypted data(bytes)
row data(bytes) <- base64 decoding <- remove padding <- encrypted data(bytes)
'''

def encrypt(data: bytes, key: bytes) -> bytes:

    h = SHA256.new()
    h.update(key)
    key = h.digest()

    iv  = get_random_bytes(AES.block_size)

    data = base64.b64encode(data)
    data = pad(data, AES.block_size)

    cipher = AES.new(key, AES.MODE_CBC, iv)

    del key
    gc.collect()

    return iv + cipher.encrypt(data) 


def decrypt(encrypted_data: bytes, key: bytes) -> bytes:

    h = SHA256.new()
    h.update(key)
    key = h.digest()

    iv = encrypted_data[:AES.block_size]
    encrypted_data = encrypted_data[AES.block_size:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    del key
    gc.collect()

    return base64.b64decode(data)


def file_encrypt(src_path, dist_path, key):

    with open(src_path, 'rb') as rf:
        data = rf.read()

        with open(dist_path, 'wb') as wf:
            wf.write(encrypt(data, key))


def file_decrypt(src_path, dist_path, key):

    with open(src_path, 'rb') as rf:
        data = rf.read()

        with open(dist_path, 'wb') as wf:
            wf.write(decrypt(data, key))


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
        file_encrypt(src, dst, password)

        print('encoded.')
        
    elif enc_or_dec == 'dec':
        password = input('password: ').encode() # warning
        file_decrypt(src, dst, password)

        print('decoded.')

    else:
        print('\'enc\' or \'dec\'')
        
