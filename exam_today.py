


from ctypes.wintypes import CHAR
from curses.ascii import isalnum, isalpha

from numpy import character, number


char_list = ["a","B","C"]
num_list = [1,2,3]
other_list = []

def palindrome(arlist):
    for i in arlist:
        if i ==isalpha:
            print("char")
        elif i == isalnum:
            print("num")
        else:
            print("false")


print(palindrome(char_list))

def get_factors(num):
    factors = 0
    for i in range(1,num):
        if i%2==0:
            pass
        else:
            factors = i
            print(factors)

#get_factors(9)





