# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 10:21:32 2018

@author: Sankalp
"""
import io
try:
    f=open("Test.txt")
    f.writelines(input("Enter what you want to add:"))
    f.close()

except io.UnsupportedOperation as e:
    print("Unsupported Operation:",e)

except Exception as e:
    print(e)

finally:
    print("Program ended")