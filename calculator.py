import numpy as np

try:
    print("Made by PyDev")
    a = input("Please select a symbol: (+,-,*,/,**,%,%2,--,SR,O,+++,~) ")
    if a!="%2" and a!="SR" and a!="O" and a!="+++" and a!="~":
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
        
except ValueError:
    print("An error has accured.")
except ZeroDivisionError:
    print("An error has accured while dividing number with 0.")