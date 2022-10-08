

import math


class exam:

    def prime_factors():
        num = int(input("enter a number:"))
        while(num%2==0):
            print(2)
            num = num/2

        for i in range(3,int(math.sqrt(num))+1,2):
            while(num%i==0):
                print(i)
                num = num/i
        if num > 2:
            print(num)

    def palidrome(array):
        iset = set(array)
        if len(array) != len(iset):
            print("it is palindrome")
        else:
            print("not palindrome")
        

exam1 = exam
exam1.prime_factors()
exam1.palidrome([1,2,3,4,1])

