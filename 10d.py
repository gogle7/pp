# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 10:52:18 2018

@author: Sankalp
"""

l=['a',0,2]
for i in l:
    try:
        print("Reciprocal is:",1/i)
        
    except ZeroDivisionError as e:
        print("Cannot divide by 0:",e)
            
    except TypeError as e:
        print("Only numbers can be divided:",e)
                
    except Exception as e:
        print(e)
                    
    finally:
        print("Iteration done\n")