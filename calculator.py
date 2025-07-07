import numpy as np
import math as mt

try:
    print("Made by PyDev")
    
    print("+ = Addition\n- = Subtraction\n* = Multiplication\n/ = Division\n//% = Floor division with remainder\n** = Exponents")
    print("% = Percentages\n%2 = Even or odd\n-- = Subtraction with negative numbers\nSR = Square and square root")
    print("CR = Cube and cube root\nO = Rounding\n+++ = Artihmetic addition\n~ = Median\n! = Factorial\nABS = Absolute value")
    print("CA = Circle Area\nCir = Circumference of the circle\nLCM = Least common multiple\nGCD = Greatest common divisor")
    
    a = input("Please select a symbol: (+,-,*,/,//%,**,%,%2,--,SR,CR,O,+++,~,!,ABS,CA,Cir,LCM,GCD) ")
    
    if a!="%2" and a.upper() not in ["SR","C","O","ABS","CA","LCM","GCD","CIR"] and a!="+++" and a!="~" and a!="!":
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
    elif a=="//%":
        if a_number < a_number_again:
            print(f"{a_number_again} // {a_number} = {a_number_again // a_number}")
            print(f"{a_number_again} % {a_number} = {a_number_again % a_number}")
        elif a_number > a_number_again:
            print(f"{a_number} // {a_number_again} = {a_number // a_number_again}")
            print(f"{a_number} % {a_number_again} = {a_number % a_number_again}")
        elif a_number == a_number_again:
            print(f"{a_number} // {a_number_again} = 1")
    
    
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
    
    elif a.upper()=="SR":
        a_number = int(input("Select a number to square: "))
        b = a_number * a_number
        print(f"The square of {a_number} is {b}. The square root of {b} is {int(np.sqrt(b))}")
    
    elif a.upper()=="CR":
        a_number = int(input("Select a number to cube: "))
        cube = float(a_number ** 3)
        print(f"The cube of {a_number} is {int(cube)}. The cube root of {int(cube)} is {int(np.cbrt(cube))}")
    
    elif a.upper()=="O":
        a = float(input("Enter a decimal number: "))
        if a >= 0:
            rounded = mt.floor(a + 0.5)
        else:
            rounded = mt.ceil(a - 0.5)
        print(f"Rounded version of {a} is {rounded}")
    
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
                print(f"The median of your numbers is {int(AO)}, The float of that number is {float(AO)}")
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
    
    elif a.upper()=="ABS":
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
                radius = int(input("Enter radius: "))
                radiussqr = radius * radius
                print(f"The area of your circle is {int(radiussqr * pi)}")
                break
            except ValueError:
                print("Please enter a number.")
    
    elif a.upper()=="CIR":
        while True:
            try:
                pi = float(input("Enter pi: "))
                diameter = float(input("Enter diameter: "))
                print(f"The circumference of your circle is {int(diameter * pi)}, the float of that number is {float(diameter * pi)}")
                break
            except ValueError:
                print("Please enter a number.")
    elif a.upper()=="LCM":
        liste = []
        print("You can add values one by one, and every number must be positive.")
        
        while True:
            abc = int(input("Please enter 2+ numbers and type -1 to have your answer: "))
            liste.append(abc)
            if abc==-1:
                liste.pop(-1)
                if len(liste) < 2:
                    print("An error has accured. This can be caused by too few numbers, or a number being 0 or smaller.")
                    break
                elif len(liste) >= 2:
                    AO = int(np.lcm.reduce(liste))
                    print(f"\nThe least common multiple of your numbers is {int(AO)}. The float of that number is {float(AO)}")
                    break
            elif abc <= -2 or abc==0:
                print("Please enter a number that is higher than -1 that is not 0")
    
    elif a.upper()=="GCD":
        liste = []
        print("You can add values one by one, and every number must be positive.")
        
        while True:
            abc = int(input("Please enter 2+ numbers and type -1 to have your answer: "))
            liste.append(abc)
            if abc==-1:
                liste.pop(-1)
                if len(liste) < 2:
                    print("An error has accured. This can be caused by too few numbers, or a number being 0 or smaller.")
                    break
                elif len(liste) >= 2:
                    AO = int(np.gcd.reduce(liste))
                    print(f"\nThe greatest common divisor of your numbers is {int(AO)}. The float of that number is {float(AO)}")
                    break
            elif abc <= -2 or abc==0:
                print("Please enter a number that is higher than -1 that is not 0")
    

except ValueError:
    print("An error has accured, please make sure you have typed a number")
except ZeroDivisionError:
    print("An error has accured while dividing number with 0.")