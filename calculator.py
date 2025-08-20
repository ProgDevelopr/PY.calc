import numpy as np
import math as mt
import sys

try:
    print("Made by PyDev")
    print("+ = Addition\n- = Subtraction\n* = Multiplication\n/ = Division\n//% = Floor division with remainder\n** = Exponents")
    print("% = Percentages\n%2 = Even or odd\nASC = Order numbers in ascending order\nDESC = Order numbers in descending order")
    print("-- = Subtraction with negative numbers\nPR = Prime checking\nPR+ = Series of prime numbers")
    print("SR = Square and square root\nCR = Cube and cube root\nO = Rounding\n+++ = Artihmetic addition\n~ = Median")
    print("MAX = Maximum value\n! = Factorial\nABS = Absolute value\nCA = Circle Area\nCir = Circumference of the circle")
    print("ARCLEN = Circle arc length\nLCM = Least common multiple\nGCD = Greatest common divisor\nS = Sign\nLOG = Logarithm")
    print("LN = Natural logarithm\ne** = Natural exponential\nSIN = Sine\nCOS = Cosine\nTAN = Tangent\nCSC = Cosecant\nSEC = Secant")
    print("COT = Cotangent\nPT = Pythagorean theorem\nF = Fibonacci sequence\nP = Pell numbers\nB = Bronze sequence")
    print("C = Copper sequence\ni = info")
    
    a = input("Enter a mode: ")
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
            print(f"{a_number_again} / {a_number} = {a_number_again / a_number:.3f}")
        elif a_number > a_number_again:
            print(f"{a_number} / {a_number_again} = {a_number / a_number_again:.3f}")
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
        a_number = float(input("Enter a number: "))
        power = float(input("Enter the power: "))
        print(f"{a_number} ** {power} = {a_number ** power:.2f}")
    
    elif a=="%":
        a_percentage = float(input("Enter the percentage: "))
        a_number = float(input("Enter a number: "))
        perpro = a_number * a_percentage
        print(f"The {a_percentage}% of {a_number} is {perpro/100:.2f}")
    
    elif a=="%2":
        evenorodd = float(input("Select a number: "))
        if evenorodd%2==0:
            print(f"{evenorodd} is an even number")
        elif not evenorodd%2==0:
            print(f"{evenorodd} is an odd number")

    elif a.upper()=="ASC":
        def asc_order(lst):
            return sorted(lst)
        lst = []
        while True:
            nums = int(input("Please enter your numbers and type -1 to have your answer: "))
            if nums==-1:
                print("Ascending order of your numbers are:",asc_order(lst))
                break
            lst.append(nums)

    elif a.upper()=="DESC":
        def desc_order(lst):
            return sorted(lst,reverse=True)
        lst = []
        while True:
            nums = int(input("Please enter your numbers and type -1 to have your answer: "))
            if nums==-1:
                print("Descending order of your numbers are:",desc_order(lst))
                break
            lst.append(nums)
    
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
    
    elif a.upper()=="PR+":
        end = int(input("Enter ending value: "))
        
        def on_prime(num):
            prime_lst = set()
            lst = set()
            for x in range(2, num + 1):
                flag = True

                # if i = 2, range(2, 2) is empty, 
                # meaning the nested loop will do nothing
                for y in range(2, x):
                    if x % y == 0:
                        print(f"{x} is not prime.")
                        lst.add(x)
                        flag = False
                        break
        
                if flag == True:
                    print(f"{x} is prime.")
                    prime_lst.add(x)
    
            if num == 1 or num == 0:
                print("1 and 0 are usually ignored in prime numbers. ")
                return False
    
            if lst == set() and len(prime_lst) == 1:
                    print("\nAll prime numbers mentioned: {2}")
                    print(f"Prime amount: {len(prime_lst)}")
                    print("All non-prime numbers mentioned: {}")
                    print(f"Non-prime amount: {len(lst)}")
    
            elif lst == set() and len(prime_lst) == 0:
                    print("\nAll prime numbers mentioned: {}")
                    print(f"Prime amount: {len(prime_lst)}")
                    print("All non-prime numbers mentioned: {}")
                    print(f"Non-prime amount: {len(lst)}")
        
            else:
                print("\nAll prime numbers mentioned:",prime_lst)
                print(f"Prime amount: {len(prime_lst)}")
                print("All non-prime numbers mentioned:",lst)
                print(f"Non-prime amount: {len(lst)}")
        
        on_prime(end)
    
    elif a.upper()=="SR":
        a_number = float(input("Select a number to square: "))
        b = a_number * a_number
        print(f"The square of {a_number} is {b:.3f}. The square root of {a_number} is {np.sqrt(a_number):.3f}.")
    
    elif a.upper()=="CR":
        a_number = float(input("Select a number to cube: "))
        cube = float(a_number ** 3)
        print(f"The cube of {a_number} is {cube:.3f}. The cube root of {a_number} is {np.cbrt(a_number):.3f}.")
    
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
    
    elif a.upper()=="MAX":
        hold_values = []
        try:
            while True:
                indexing = int(input("Please enter your numbers and type -1 to have your answer: "))
                if indexing==-1:
                    hold_values.pop(-0)
                    print(f"Max value: {mods[0]}, amount of max values: {len(mods)}")
                    break
                elif indexing!=-1:
                    hold_values.append(indexing)
                a = [indexing]
                a = np.array(hold_values)
                maxi = a.max()
                mods = a[a == maxi]
        except ValueError:
            print("An error has accured, please type a number.")
    
    elif a=="!":
        while True:
            factnum = int(input("Enter a number: "))
            if factnum<=0:
                print("Sorry, but you can't use 0 or negative numbers in factorial calculations.")
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
                print(f"{base:.2f} must be raised to the power of {num:.2f} to get {des:.2f}")
    
    elif a.upper()=="LN":
        power_of_e = float(input("Enter the power of e (Euler's number): "))
        e = 2.71828 # e ≈ 2.71828
        print(f"ln(e ** {power_of_e}) = {power_of_e:.2f}")
        # ln(e7) = 1096.63, 
        # base: e
        # power: 7
        # destination: 1096.63
    
    elif a.upper()=="E**":
        power_of_e = float(input("Enter the power of e (Euler's number): "))
        new_e = 2.71828 ** power_of_e
        print(f"e ** {power_of_e} = {new_e:.3f}")
    
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
                print("An error has accured.")
    
    elif a.upper()=="F": # Why was this so hard?
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
                    Golden_ratio_φ = 1.618
                return a
            print(f"F({n}) = {fib(n)}")
        else:
            print("An error has accured.")

    elif a.upper()=="P": # Fibonacci to the rescue
        n = int(input("Enter a number: "))
        if n==0 or n==1:
            print(f"P({n}) = {n}")
        elif not n==0 or n==1:
            def pell(n):
                a = 0
                b = 1
                for looptimes in range(n):
                    old_a = a 
                    a = b 
                    b = old_a + 2 * b
                    Silver_ratio_δₛ = 2.414
                return a
            print(f"P({n}) = {pell(n)}")
        else:
            print("An error has accured.")
    
    elif a.upper()=="B": # Pell to the rescue
        n = int(input("Enter a number: "))
        if n==0 or n==1:
            print(f"B({n}) = {n}")
        elif not n==0 or n==1:
            def Bronze(n):
                a = 0
                b = 1
                for looptimes in range(n):
                    old_a = a 
                    a = b 
                    b = old_a + 3 * b
                    Bronze_ratio_β = 3.302
                return a
            print(f"B({n}) = {Bronze(n)}")
        else:
            print("An error has accured.")

    elif a.upper()=="C": # Bronze to the rescue
        n = int(input("Enter a number: "))
        if n==0 or n==1:
            print(f"C({n}) = {n}")
        elif not n==0 or n==1:
            def copper(n):
                a = 0
                b = 1
                for looptimes in range(n):
                    old_a = a 
                    a = b 
                    b = old_a + 4 * b
                    Copper_ratio_κ = 4.236
                return a
            print(f"C({n}) = {copper(n)}")
        else:
            print("An error has accured.")

    elif a.upper()=="I":
        if __name__ == "__main__":
            print(f"PY.calc")
            print(f"MADE WITH PYTHON 3.11.4 | Current Python version: {sys.version:.6}")
            print(f"MADE WITH NUMPY 2.3.2 | Current Numpy version: {np.__version__}")
            print(f"Being imported: No\nFile path: {__file__}")
        else:
            print(f"PY.calc")
            print(f"MADE WITH PYTHON 3.11.4 | Current Python version: {sys.version:.6}")
            print(f"MADE WITH NUMPY 2.3.2 | Current Numpy version: {np.__version__}")
            print(f"Being imported: Yes\nFile path: {__file__}")

    else:
        print("Please choose a mode.")

except ValueError:
    print("An error has accured, please make sure you have typed a number.")
except ZeroDivisionError:
    print("An error has accured while dividing number with 0.")

sys.exit(1)