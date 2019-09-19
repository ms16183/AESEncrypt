# AESEncrypt

## Overview
This app converts row data to safety data by AES cipher.

License: `MIT`

## Description
AES encryption algorithm of this app is 128bit-CBC and randomized IV.
At first, you choose 'decrypt' or 'encprypt'.
Second,

- decrypt
    - You choose encrypted file.
    - You input a password.
    - You will decrypt your important file if the password your inputed is correct.

- encrypt
    - You choose decrypted file.
    - You set a password.
    - You will encrypt your important file.


## Usage
### GUI
```
$ cd AESEncrypt/
$ chmod +x src/*.py
$ python3 src/gui.py
```

## Install
```
$ git clone https://github.com/tiro-finale/AESEncrypt.git
$ pip3 install pycryptdome
```
