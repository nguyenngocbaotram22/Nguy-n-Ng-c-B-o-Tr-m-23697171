# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 08:37:12 2024

@author: Admin
"""

print("====MENU====")
print(" 1.HU TIEU")
print(" 2.CHAO LONG")
print(" 3.BANH CANH")
print(" 4.BUN RIEU")
print(" 5.PHO BO")
print("============")
print("moi nhap lua chon:")
print("============")
a=int(input("nhap lua chon"))
if a==1:
    print("Mon ban chon la hu tieu")
elif a==2:
    print("Mon ban chon la chao long")
elif a==3:
    print("Mon ban chon la banh canh")
elif a==4:
    print("mon ban chon la bun rieu")
elif a==5:
    print("Mon ban chon la pho bo")
elif a>5 or a<1:
    print("la muon an gi")
print("==============================")