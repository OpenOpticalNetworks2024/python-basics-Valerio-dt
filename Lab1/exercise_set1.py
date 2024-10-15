"""Exercise Set 1: Python Basics"""

import numpy as np
import matplotlib as plt


# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions


# ex1
def exercise1():
    x=int(input("inserire primo numero"))
    y=int(input("inserire secondo numero"))

    p=x*y

    if p>1000:
        print("the product is greater than 1000, so here is the sum ", x+y)
    else:
        print(p)


# ex2
def exercise2():
    start=int(input("Enter start of the range: "))
    end=int(input("enter end of the range: "))

    precedent=0

    for i in range(start, end+1):
        sum=i+precedent
        print("number:", i)
        print("Sum of current number and precedent", sum)
        precedent=i

# ex3
def exercise3():
    list1=list(input("Enter list: "))

    first=list1[1]
    last=list1[-1]
    
    if first==last:
        print("True")
    else:
        print("False")



# ex4
def exercise4():
    pass


# ex5
def exercise5():
    pass


# ex6
def exercise6():
    pass


# ex7
def exercise7():
    pass


# ex8
def exercise8():
    pass


# ex9
def exercise9():
    pass


# ex10
def exercise10():
    pass


# ex11
def exercise11():
    pass


# ex12
def exercise12():
    pass


if __name__ == "__main__":
    print("EXERCISE SET 1")
    print("EX1")
    exercise1()
    print("EX2")
    exercise2()
    print("EX3")
    exercise3()
    print("EX4")
    exercise4()
    print("EX5")
    exercise5()
    print("EX6")
    exercise6()
    print("EX7")
    exercise7()
    print("EX8")
    exercise8()
    print("EX9")
    exercise9()
    print("EX10")
    exercise10()
    print("EX11")
    exercise11()
    print("EX12")
    exercise12()
