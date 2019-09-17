#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, ttk, filedialog, PhotoImage, TOP, HORIZONTAL
import os, sys
from cipher import *

def get_files():

    cdir = os.path.abspath(os.path.dirname(__file__))
    ftype = [('', '*')]
    return filedialog.askopenfilenames(filetypes=ftype, initialdir=cdir)


def encrypt_processing():

    files = get_files()
    file_n = len(files)

    if file_n <= 0:
        return

    root = Tk()
    root.title('encrypt')
    root.resizable(0, 0)

    label = ttk.Label(root, text='')
    label.grid(row=1, column=1)
    bar = ttk.Progressbar(root, orient=HORIZONTAL, length=100, mode='determinate')
    bar.configure(maximum=file_n, value=0)
    bar.grid(row=2, column=1)

    for i, f in enumerate(files, start=1):

        file_encrypt(f, f+'.encrypted', 'asuka'.encode())

        label.configure(text=f)
        bar.configure(value=i/file_n*100)


def decrypt_processing():

    files = get_files()
    file_n = len(files)

    if file_n <= 0:
        return

    root = Tk()
    root.title('decrypt')
    root.resizable(0, 0)

    label = ttk.Label(root, text='')
    label.grid(row=1, column=1)
    bar = ttk.Progressbar(root, orient=HORIZONTAL, length=100, mode='determinate')
    bar.configure(maximum=file_n, value=0)
    bar.grid(row=2, column=1)

    for i, f in enumerate(files, start=1):

        f_origin, _ = os.path.splitext(f)
        file_decrypt(f, f_origin, 'asuka'.encode())

        label.configure(text=f)
        bar.configure(value=i/file_n*100)


def make_gui():

    root = Tk()
    root.title('AESEncrypt')
    root.resizable(0, 0)

    main_frame = ttk.Frame(root, padding=5)
    main_frame.grid()

    encrypt_icon = PhotoImage(file='../icon/encrypt.png')
    decrypt_icon = PhotoImage(file='../icon/decrypt.png')
    encrypt_button = ttk.Button(main_frame, text='Encrypt', image=encrypt_icon, compound=TOP, command=encrypt_processing)
    decrypt_button = ttk.Button(main_frame, text='Decrypt', image=decrypt_icon, compound=TOP, command=decrypt_processing)
    encrypt_button.grid(row=1, column=1)
    decrypt_button.grid(row=1, column=2)

    root.mainloop()

if __name__ == '__main__':
    make_gui()
