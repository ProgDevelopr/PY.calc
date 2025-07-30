import numpy as np
import math as mt

try:
    print("Made by PyDev")
    print("+ = Addition\n- = Subtraction\n* = Multiplication\n/ = Division\n//% = Floor division with remainder\n** = Exponents")
    print("% = Percentages\n%2 = Even or odd\n-- = Subtraction with negative numbers\nPR = Prime checking")
    print("SR = Square and square root\nCR = Cube and cube root\nO = Rounding\n+++ = Artihmetic addition\n~ = Median\n! = Factorial")
    print("ABS = Absolute value\nCA = Circle Area\nCir = Circumference of the circle\nARCLEN = Circle arc length")
    print("LCM = Least common multiple\nGCD = Greatest common divisor\nS = Sign\nLOG = Logarithm\nSIN = Sine\nAREA = Area")
    print("COS = Cosine\nTAN = Tangent\nCSC = Cosecant\nSEC = Secant\nCOT = Cotangent\nPT = Pythagorean theorem")
    print("F = Fibonacci sequence")
    
    a = input("Enter mode symbol: ")
    print()

    if a=="+":
        a_number = float(input("Select a number: "))
        a_number_again = float(input("Select another number: "))
        print(f"{float(a_number)} + {float(a_number_again)} = {a_number + a_number_again}") 

    elif a=="-":
        a_number = float(input("Select a number: "))
        a_number_again = float(input("Select another number: "))
        
        if a_number < a_number_again:
            print(f"{a_number_again} - {a_number} = {a_number_again - a_number:.2f}")
        elif a_number > a_number_again:
            print(f"{a_number} - {a_number_again} = {a_number - a_number_again:.2f}")
        elif a_number == a_number_again:
            print(f"{a_number} - {a_number_again} = 0")

    elif a=="*":
        a_number = float(input("Select a number: "))
        a_number_again = float(input("Select another number: "))
        print(f"{a_number} * {a_number_again} = {a_number * a_number_again}")

    elif a=="/":
        a_number = float(input("Select a number: "))
        a_number_again = float(input("Select another number: "))
        
        if a_number < a_number_again:
            print(f"{a_number_again} / {a_number} = {a_number_again / a_number:.2f}")
        elif a_number > a_number_again:
            print(f"{a_number} / {a_number_again} = {a_number / a_number_again:.2f}")
        elif a_number == a_number_again:
            print(f"{a_number} / {a_number_again} = 1")
    
    elif a=="//%":
        a_number = float(input("Select a number: "))
        a_number_again = float(input("Select another number: "))
        
        if a_number < a_number_again:
            print(f"{a_number_again} // {a_number} = {a_number_again // a_number:.2f}")
            print(f"{a_number_again} % {a_number} = {a_number_again % a_number:.2f}")
        elif a_number > a_number_again:
            print(f"{a_number} // {a_number_again} = {a_number // a_number_again:.2f}")
            print(f"{a_number} % {a_number_again} = {a_number % a_number_again:.2f}")
        elif a_number == a_number_again:
            print(f"{a_number} // {a_number_again} = 1")
    
    
    elif a=="**":
        a_number = int(input("Enter a number: "))
        power = int(input("Enter the power: "))
        print(f"{a_number} ** {power} = {a_number ** power:.2f}")
    
    elif a=="%":
        a_percentage = int(input("Enter the percentage: "))
        a_number = int(input("Enter a number: "))
        perpro = a_number * a_percentage
        print(f"The {a_percentage}% of {a_number} is {perpro/100:.2f}")
    
    elif a=="%2":
        evenorodd = int(input("Select a number: "))
        if evenorodd%2==0:
            print(f"{evenorodd} is an even number")
        elif not evenorodd%2==0:
            print(f"{evenorodd} is an odd number")
    
    elif a=="--":
        a_number = float(input("Select a number: "))
        a_number_again = float(input("Select another number: "))
        print(f"{a_number} - {a_number_again} = {a_number - a_number_again:.2f}")

    elif a.upper()=="PR":
        a_number = int(input("Enter a number: "))
        def isprime(num):
            if num <= 1:
                print("An error has accured. 1 or below are not prime numbers")
                return False
            for i in range(2,int(np.sqrt(num) + 1)):
                if num % i == 0:
                    print(f"{int(num)} is not a prime number.")
                    return False
            print(f"{int(num)} is a prime number.")
        isprime(a_number)
    
    elif a.upper()=="SR":
        a_number = int(input("Select a number to square: "))
        b = a_number * a_number
        print(f"The square of {a_number} is {b:.2f}. The square root of {a_number} is {np.sqrt(a_number):.2f}.")
    
    elif a.upper()=="CR":
        a_number = int(input("Select a number to cube: "))
        cube = float(a_number ** 3)
        print(f"The cube of {a_number} is {cube:.2f}. The cube root of {a_number} is {np.cbrt(a_number):.2f}.")
    
    elif a.upper()=="O":
        a = float(input("Enter a decimal number: "))
        if a >= 0:
            rounded = mt.floor(a + 0.5)
        else:
            rounded = mt.ceil(a - 0.5)
        print(f"Rounded version of {a} is {rounded}.")
    
    elif a=="+++":
        liste = []
        while True:
            abc = int(input("Please enter your numbers and type -1 to have your answer: "))
            liste.append(abc)
            if abc==-1:
                liste.pop(-1)
                AO = int(np.mean(liste))
                print(f"Arithmetic average of your numbers is {AO:.2f}.")
                break
    
    elif a=="~":
        liste = []
        while True:
            abc = int(input("Please enter your numbers and type -1 to have your answer: "))
            liste.append(abc)
            if abc==-1:
                liste.pop(-1)
                AO = np.median(liste)
                print(f"The median of your numbers is {AO:.2f}.")
                break
    
    elif a=="!":
        while True:
            factnum = int(input("Enter a number: "))
            if factnum==0:
                print("Sorry, but you can't use 0 in factorial calculations.")
            elif factnum!=0:
                fact = mt.factorial(factnum)
                print(f"{factnum}! = {fact}")
                break
    
    elif a.upper()=="ABS":
        while True:
            try:    
                a_number = int(input("Enter a number: "))
                print(f"|{a_number}| = {abs(a_number)}")
                break
            except ValueError:
                print("Please enter a number.")
    
    elif a.upper()=="CA":
        while True:
            try:    
                pi = int(input("Enter pi: "))
                radius = int(input("Enter radius: "))
                radiussqr = radius * radius
                print(f"The area of your circle is {radiussqr * pi:.2f}.")
                break
            except ValueError:
                print("Please enter a number.")
    
    elif a.upper()=="CIR":
            try:
                pi = float(input("Enter pi: "))
                diameter = float(input("Enter diameter: "))
                print(f"The circumference of your circle is {diameter * pi:.2f}.")
            except ValueError:
                print("Please enter a number.")
    
    elif a.upper()=="ARCLEN":
        try:
            Pi = float(input("Enter pi (3,3.14): "))
            Angle = float(input("Enter angle: "))
            Radius = float(input("Enter the radius: "))
            if Radius==0 or Radius < 0:
                print("An error has accured. Radius being negative (-) or 0 is impossible in math")
            elif Angle==0:
                print("The arc length of your circle is 0 (No angle)")
            elif Angle < 0:
                print("An error has accured. Angles being negative (-) is impossible in math")
            elif Angle > 0:
                def arclenght(angle,pi,rad):
                    pi = 2 * pi
                    value = pi * rad
                    value = value * angle
                    value = value / 360
                    print(f"The arc length of your circle sector is {value:.2f}.")
                arclenght(Angle,Pi,Radius)
            else:
                print("An error has accured. Please make sure you have typed a number")
        except ValueError:
            print("An error has accured. Please enter a number")
    
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
                    print(f"\nThe least common multiple of your numbers is {AO:.2f}.")
                    break
            elif abc <= -2 or abc==0:
                print("Please enter a number that is higher than -1 that is not 0")
    
    elif a.upper()=="GCD":
        liste = []
        print("You can add values one by one, and every number must be positive!")
        
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
                    print(f"\nThe greatest common divisor of your numbers is {AO:.2f}.")
                    break
            elif abc <= -2 or abc==0:
                print("Please enter a number that is higher than -1 that is not 0")
    
    elif a.upper()=="S":
        num = float(input("Type a number: "))
        if num > 0:
            print(f"The sign of {num} is 1")
        elif num < 0:
            print(f"The sign of {num} is -1")
        elif num == 0:
            print(f"The sign of {num} is 0")
        else:
            print("An error has accured. Please choose a number.")
    
    elif a.upper()=="LOG":
        print("Make sure you enter positive numbers (Especially for base number)!")
        base = float(input("Type base number: "))
        if base <= 0 or base == 1:
            print("An error has accured. Base too small and can not be 1.")
        elif base > 0:
            des = float(input("Type the destination: "))
            if des <= 0:
                print("An error has accured. Destination too small.")
            elif base > 0:
                num = mt.log(des,base)
                print(f"{base} must be raised to the power of {num:.2f} to get {des}")
    
    elif a.upper()=="SIN":
        opp = float(input("Enter the opposite edge: "))
        hyp = float(input("Enter the hypotenuse: "))
        print(f"sin(θ) = {opp/hyp:.2f}")
        
    elif a.upper()=="COS":
        adj = float(input("Enter the adjacent edge: "))
        hyp = float(input("Enter the hypotenuse: "))
        print(f"cos(θ) = {adj/hyp:.2f}")
    
    elif a.upper()=="TAN":
        adj = float(input("Enter the adjacent edge: "))
        opp = float(input("Enter the opposite edge: "))
        print(f"tan(θ) = {opp/adj:.2f}")

    elif a.upper()=="CSC":
        hyp = float(input("Enter the hypotenuse: "))
        opp = float(input("Enter the opposite edge: "))
        print(f"csc(θ) = {hyp/opp:.2f}")

    elif a.upper()=="SEC":
        hyp = float(input("Enter the hypotenuse: "))
        adj = float(input("Enter the adjacent edge: "))
        print(f"sec(θ) = {hyp/adj:.2f}")
    
    elif a.upper()=="COT":
        adj = float(input("Enter the adjacent edge: "))
        opp = float(input("Enter the opposite edge: "))
        print(f"cot(θ) = {adj/opp:.2f}")

    elif a.upper()=="PT":
        print("HYP = Finding the hypotenuse\nEDGE = Finding an edge")
        HYPorEdge = str(input("Select which edge to calculate: ")).upper()
        
        if HYPorEdge=="HYP":
            AnEdge = float(input("Enter the value of an edge: "))
            AnotherEdge = float(input("Enter the value of another edge: "))
            def HYPcal(a,b):
                asq = a * a
                bsq = b * b
                c = asq + bsq
                answer = np.sqrt(c)
                print(f"The hypotenuse of {a} and {b} is {answer:.2f}")
            HYPcal(AnEdge,AnotherEdge)
        
        elif HYPorEdge=="EDGE":
            AnEdge = float(input("Enter the value of an edge: "))
            hyp = float(input("Enter the value of hypotenuse: "))
            if hyp < AnEdge:
                print("An error has accured, the hypotenuse was smaller than the edge you provided.")
            elif not hyp < AnEdge:
                def EDGEcal(b,a):
                    asq = a * a
                    bsq = b * b
                    c = bsq - asq
                    answer = np.sqrt(c)
                    print(f"The other edge of {b} (hypotenuse) and {a} is {answer:.2f}")
                EDGEcal(hyp,AnEdge)
            else:
                print("An error has accured")
    
    elif a.upper()=="F":
        n = int(input("Enter a number: "))
        if n==0 or n==1:
            print(f"F({n}) = {n}")
        elif not n==0 or n==1:
            def fib(n):
                a = 0
                b = 1
                for looptimes in range(n):
                    old_a = a
                    a = b
                    b = old_a + b
                return a
            print(f"F({n}) = {fib(n)}")
        else:
            print("An error has accured.")
            

    else:
        print("Please choose a mode.")

except ValueError:
    print("An error has accured, please make sure you have typed a number.")
except ZeroDivisionError:
    print("An error has accured while dividing number with 0.")