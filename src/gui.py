#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, ttk, filedialog, simpledialog, messagebox, PhotoImage
from tkinter import TOP, HORIZONTAL
import os
from cipher import *

def get_files():

    cdir = os.path.abspath(os.path.dirname(__file__))
    ftype = [('', '*')]
    return filedialog.askopenfilenames(filetypes=ftype, initialdir=cdir)


def get_password():

    return simpledialog.askstring("Password", "Enter password", show='*')


def encrypt_processing():

    extension = 'encrypted'

    files = get_files()
    if len(files) <= 0:
        return

    password = get_password().encode()
    if len(password) <= 0:
        return

    err = False
    for f in files:
        try:
            file_encrypt(f, f+'.'+extension, password)
            os.remove(f)
        except:
            messagebox.showerror(title='Error', message='Error: ' + f)
            err = True
    
    if not err:
        messagebox.showinfo(title='Info', message='Successfully.')

    return


def decrypt_processing():

    files = get_files()
    if len(files) <= 0:
        return

    password = get_password().encode()
    if len(password) <= 0:
        return

    err = False
    for f in files:
        try:
            file_decrypt(f, os.path.splitext(f)[0], password)
            os.remove(f)
        except:
            messagebox.showerror(title='Error', message='Incorrect password: ' + f)
            err = True

    if not err:
        messagebox.showinfo(title='Info', message='Successfully.')

    return


def make_gui():

    root = Tk()
    root.title('AESEncrypt')
    root.iconbitmap('../icon/icon.ico')
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
