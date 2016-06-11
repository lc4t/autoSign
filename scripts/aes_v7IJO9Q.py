#! /usr/bin/python3
#-*- coding:utf-8
from Crypto.Cipher import AES

key = '1111111111111111'
c = AES.new(key, 3)
ans = c.encrypt('hello,world     ')
print (ans)
