# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:13:37 2024

@author: Admin
"""
var='Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM'

print()

s= var.split(", ")
print("bang 1")
for b in s:
    print(b)
print()
print("bang 2")
s2=  var.replace("P. ","").replace("Q. ","").replace("Tp. ","")
s3= s2.split(", ")
for c in s3:
    print(c)