#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, ttk, filedialog, simpledialog, messagebox, PhotoImage, TOP, HORIZONTAL
import os, sys
from cipher import *

def get_files():

    cdir = os.path.abspath(os.path.dirname(__file__))
    ftype = [('', '*')]
    return filedialog.askopenfilenames(filetypes=ftype, initialdir=cdir)


def get_password():

    return simpledialog.askstring("Password", "Enter password:", show='*')


def encrypt_processing():

    files = get_files()

    if len(files) <= 0:
        return

    password = get_password().encode()

    if len(password) <= 0:
        return

    for i, f in enumerate(files, start=1):

        file_encrypt(f, f+'.encrypted', password)


def decrypt_processing():

    files = get_files()

    if len(files) <= 0:
        return

    password = get_password().encode()

    if len(password) <= 0:
        return

    for i, f in enumerate(files, start=1):

        try:
            file_decrypt(f, os.path.splitext(f)[0], password)
        except:
            messagebox.showerror(title='Error', message='Incorrect password.')
            return


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
