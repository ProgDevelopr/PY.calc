import numpy as np
import math as mt

try:
    print("Made by PyDev")
    
    print("+ = Addition\n- = Subtraction\n* = Multiplication\n/ = Division\n** = Exponents\n% = Percentages")
    print("%2 = Even or odd\n-- = Subtraction with negative numbers\nSR = Square and square root\nO = Rounding")
    print("+++ = Artihmetic addition\n~ = Median\n! = Factorial\nABS = Absolute value\nCA = Circle Area")
    print("Cir = Circumference of the circle\n")
    
    a = input("Please select a symbol: (+,-,*,/,**,%,%2,--,SR,O,+++,~,!,ABS,CA,Cir) ")
    
    if a!="%2" and a!="SR" and a!="O" and a!="+++" and a!="~" and a!="!" and a!="ABS" and a.upper()!="CA" and a.lower()!="cir":
        a_number = int(input("Select a number: "))
        a_number_again = int(input("Select another number: "))
        oh = a_number * a_number_again
    
    elif a=="%2":
        evenorodd = int(input("Select a number: "))
    
    if a=="+":
       print(f"{a_number} + {a_number_again} = {a_number + a_number_again}") 

    elif a=="-":
        if a_number < a_number_again:
            print(f"{a_number_again} - {a_number} = {a_number_again - a_number}")
        elif a_number > a_number_again:
            print(f"{a_number} - {a_number_again} = {a_number - a_number_again}")
        elif a_number == a_number_again:
            print(f"{a_number} - {a_number_again} = 0")

    elif a=="*":
        print(f"{a_number} * {a_number_again} = {a_number * a_number_again}") 

    elif a=="/":
        if a_number < a_number_again:
            print(f"{a_number_again} / {a_number} = {a_number_again / a_number}")
        elif a_number > a_number_again:
            print(f"{a_number} / {a_number_again} = {a_number / a_number_again}")
        elif a_number == a_number_again:
            print(f"{a_number} / {a_number_again} = 1")
    
    elif a=="**":
        print(f"{a_number} ** {a_number_again} = {a_number ** a_number_again}")
    
    elif a=="%":
        print(f"The {a_number} of {a_number_again}% is {oh/100}%")
    
    elif a=="%2":
        if evenorodd%2==0:
            print(f"{evenorodd} is an even number")
        elif not evenorodd%2==0:
            print(f"{evenorodd} is an odd number")
    
    elif a=="--":
        print(f"{a_number} - {a_number_again} = {a_number - a_number_again}")
    
    elif a=="SR":
        a_number = int(input("Select a number to square: "))
        b = a_number * a_number
        print(f"The square of {a_number} is {b}. The square root of {b} is {int(np.sqrt(b))}")
    
    elif a=="O":
        a_number = float(input("Select a number: "))
        print(f"The rounded value of {a_number} is {round(a_number)}")
        print("PLEASE NOTE THAT IF YOU ROUND number.5 IT IS BANKER'S ROUNDING AND IT MIGHT BE WRONG")
    
    elif a=="+++":
        liste = []
        while True:
            abc = int(input("Please enter your numbers and type -1 to have your answer: "))
            liste.append(abc)
            if abc==-1:
                liste.pop(-1)
                AO = int(np.mean(liste))
                print(f"Arithmetic average of your numbers are {AO}, The float of that number is {float(AO)}")
                break
    
    elif a=="~":
        liste = []
        while True:
            abc = int(input("Please enter your numbers and type -1 to have your answer: "))
            liste.append(abc)
            if abc==-1:
                liste.pop(-1)
                AO = int(np.median(liste))
                print(f"The median of your numbers is {AO}, The float of that number is {float(AO)}")
                break
    
    elif a=="!":
        while True:
            factnum = int(input("Enter a number: "))
            if factnum==0:
                print("Sorry, but you can't use 0 in factorial calculations")
            elif factnum!=0:
                fact = mt.factorial(factnum)
                print(f"The factorial of {factnum} is {fact}")
                break
    
    elif a=="ABS":
        while True:
            try:    
                a_number = int(input("Enter a number: "))
                print(f"The absolute value of {a_number} is {abs(a_number)}")
                break
            except ValueError:
                print("Please enter a number.")
    
    elif a.upper()=="CA":
        while True:
            try:    
                pi = int(input("Enter pi: "))
                radius = int(input("Enter radius:"))
                radiussqr = radius * radius
                print(f"The area of your circle is {int(radiussqr * pi)}")
                break
            except ValueError:
                print("Please enter a number.")
    
    elif a.lower()=="cir":
        while True:
            try:
                pi = float(input("Enter pi: "))
                diameter = float(input("Enter diameter:"))
                print(f"The circumference of your circle is {int(diameter * pi)}, the float of that number is {float(diameter * pi)}")
                break
            except ValueError:
                print("Please enter a number.")

except ValueError:
    print("An error has accured, please make sure you have typed a number")
except ZeroDivisionError:
    print("An error has accured while dividing number with 0.")