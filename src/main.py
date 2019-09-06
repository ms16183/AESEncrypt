#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# default
import os, sys
import argparse
from pathlib import Path
from getpass import getpass

# AES
import cipher

description = \
'''
AES encryption algorithm of this app is 128bit-CBC and randomized by IV.
First, you choose 'decrypt' or 'encprypt'.
Second, you choose source file and set some options.
'''

def main():

    args_parser = argparse.ArgumentParser(description=description)
    
    # optional args
    args_parser.add_argument('-e', '--extension', help='Encrypted file\'s extension.', default='.encrypted')
    args_parser.add_argument('-n', '--not-name-encrypt', help='Encrypted file\'s name don\'t encryption.', default=False, action='store_true')

    # positional args
    args_parser.add_argument('src', help='source file', nargs='+')
    args_parser.add_argument('-m', '--mode', required=True, help='\'decrypt\' or \'encrypt\'', choices=['d', 'e'])

    args = args_parser.parse_args()
    #print(args)

    src = args.src
    mode = args.mode
    extension = args.extension
    not_name_encrypte = args.not_name_encrypt

    # processing


if __name__ == '__main__':
    main()
