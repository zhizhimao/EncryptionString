#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 17:38:15 2018

@author: 星空飘飘

编辑器：Spyder
Anaconda 3-5.1.0
Pandas: 0.22.0
Python 3.6.4
lxml: 4.1.1
MongoDB 2.6.12

encryptionstr.py
"""

from cryptography.fernet import Fernet
cipher_key = Fernet.generate_key()
cipher_key
cipher = Fernet(cipher_key)
text = b'123456789'  # 字符串转换为字节形式
encrypted_text = cipher.encrypt(text)  # 加密字符串
print(encrypted_text)
decrypted_text = cipher.decrypt(encrypted_text)  # 将加密内容解密
str_text = str(decrypted_text)
str_test = str_text[2:-1]
print(str_test)
