from functools import reduce
import math
import sys
from os import system, name
from time import sleep
from random import randint as rand, choice as cho
from collections import Counter

# 71 main modes
# 9 extra modes

def def_input(msg, default):
    prompt = input(msg)
    if prompt == "":
        return default
    else:
        return int(prompt)

def i_input(msg):
    return int(input(msg))

def f_input(msg):
    return float(input(msg))

def clear():
    system('cls' if name == 'nt' else 'clear')

def med(lst):
    lst = sorted(lst)
    L = len(lst)
    mid = L // 2

    if L % 2 == 0:
        left = lst[mid - 1]
        right = lst[mid]
        return (left + right) / 2
    else:
        return lst[mid]

def slope(h, b, returning=False):
    if not returning:
        print(f"m = {h/b}")
    else:
        return h / b

def per_slope(h, b, returning=False):
    m = (h / b) * 100
    if not returning:
        print(f"m = {m}%")
    else:
        return m

def close(t, _, msg="Closing"):
    print()
    for _ in range(1, _):
        print(f"\r{msg}.  ", end="")
        sleep(t)
        print(f"\r{msg}.. ", end="")
        sleep(t)
        print(f"\r{msg}...", end="")
        sleep(t)
    clear()


staff_files = {}


def save(on_off, elem):  # also for the future
    with open(staff_files[elem], "w") as f:
        f.write(on_off)


def read_file(elem):  # also for the future
    filenm = staff_files[elem]
    with open(filenm, "r") as f:
        txt = f.read().strip().title()
        return txt == "True"

def mset_func():
    mset = {
        "+": "Addition",
        "Σ": "Sum",
        "Π": "Product",
        "-": "Subtraction",
        "--": "Smart Subtraction",
        "*": "Multiplication",
        "*Σ": "Multiplicated sum",
        "*T": "Multiplication Table",
        "**T": "Exponential Chart",
        "/": "Division",
        "\\": "Smart Division",
        "//%": "Floor division with remainder",
        "DIV": "Divisor finder",
        "PF": "Prime factors",
        "**": "Exponents",
        "%": "Percentages",
        "F%": "Find percentage",
        "%2": "Even or odd",
        "ASC": "Order numbers in ascending order",
        "DESC": "Order numbers in descending order",
        "P": "Perfect number checker",
        "PR": "Prime checker",
        "COP": "Coprime checker",
        "PR+": "Series of prime numbers",
        "P!": "Prime Factorization",
        "ARM": "Armstrong number checker",
        "SQRT": "Square and square root",
        "SQ": "Square numbers",
        "CBRT": "Cube and cube root",
        "CB": "Cube numbers",
        "O": "Decimal rounding",
        "R": "Rounding",
        "+++": "Arithmetic mean",
        "~": "Median",
        "RN": "Range",
        "MODE": "Mode",
        "DEV": "Deviation",
        "PC": "Pie charts",
        "VAR": "Variance",
        "!": "Factorial",
        "||": "Absolute value",
        "RA": "Rectangle area",
        "PREC": "Perimeter of a rectangle",
        "RV": "Rectangular prism volume",
        "CA": "Circle area",
        "Cir": "Circumference of the circle",
        "SV": "Sphere volume",
        "ARCLEN": "Circle arc length",
        "M": "Slope",
        "%M": "Percentage of slope",
        "T!": "Triangle inequality",
        "TA": "Triangle area",
        "TV": "Triangular prism volume",
        "CV": "Cylinder volume",
        "CNV": "Cone volume",
        "LCM": "Least common multiple",
        "GCD": "Greatest common divisor",
        "S": "Sign",
        "LOG": "Logarithm",
        "LN": "Natural logarithm",
        "e**": "Natural exponential",
        "SIN": "Sine",
        "COS": "Cosine",
        "TAN": "Tangent",
        "CSC": "Cosecant",
        "SEC": "Secant",
        "COT": "Cotangent",
        "PT": "Pythagorean theorem",
        "PA": "Pressure",
        "OHM": "Ohm's law",
        "MS": "Metallic Sequences",
    }
    return mset

def emset_func():
    extra_mset = {
        "TEST": "Math quiz",
        "MD": "Display all mode shortcuts",
        "CON": "Unit conversion",
        "NET": "Exam net calculator",
        "RAND": "Number guessing game",
        "RNG": "Random number generator",
        "i": "info",
        "CLS": "Clear terminal",
        "E": "Exit"
    }
    return extra_mset

def intro():
    print("Made by PyDev")
    print("""
██████╗ ██╗   ██╗ ██████╗ █████╗ ██╗      ██████╗
██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗██║     ██╔════╝
██████╔╝ ╚████╔╝ ██║     ███████║██║     ██║     
██╔═══╝   ╚██╔╝  ██║     ██╔══██║██║     ██║     
██║        ██║██╗╚██████╗██║  ██║███████╗╚██████╗
╚═╝        ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝
""")
    mset = mset_func()
    extra_mset = emset_func()

    mlst = []
    mmlst = []
    print("I -~- MAIN -~- I")
    for k, v in mset.items():
        print(f"{k} = {v}")
        mmlst.append(k)
        mlst.append(k)

    print("\nI -~- UTILITIES / SPECIAL -~- I")
    for k, v in extra_mset.items():
        print(f"{k} = {v}")
        mlst.append(k)

    mode_count = len(mlst)
    main_mode_count = len(mmlst)
    utility_count = mode_count - main_mode_count
    return mode_count, main_mode_count, utility_count


try:
    mode = ""
    mode_count,mm_count,ucount = intro()

    while True:
        mode = input("\nEnter a mode: ").upper().strip()

        if mode == "+":
            a_number = f_input("Select a number: ")
            a_number_again = f_input("Select another number: ")
            print(f"{a_number} + {a_number_again} = {a_number + a_number_again:.3f}")

        elif mode in ["Σ", "SUM"]:
                sum = 0
                n = i_input("Enter n: ")
                end = input("Enter the ending number (inf for infinity): ")
                print("If you wish to write a term, i will be the number (n).")
                term = def_input("Enter a term (Write in Python, optional): ","i")
                if str(end) != "inf":
                    for i in range(n,int(end)+1):
                        i2 = eval(term)
                        sum+=i2
                    print(f"Answer: {sum}")
                else:
                    i=n
                    while True:
                        try:
                            if term:
                                i2 = eval(term)
                            else:
                                i2 = i
                            sum+=i2
                            i+=1
                            print(f"Answer: {sum}")
                        except KeyboardInterrupt:
                            break


        elif mode == "-":
            a_number = f_input("Select a number: ")
            a_number_again = f_input("Select another number: ")

            print(f"{a_number} - {a_number_again} = {a_number - a_number_again}")

        elif mode == "--":
            a_number = f_input("Select a number: ")
            a_number_again = f_input("Select another number: ")

            if a_number < a_number_again:
                print(f"{a_number} - {a_number_again} = {a_number - a_number_again:.3f}")
            elif a_number > a_number_again:
                print(f"{a_number_again} - {a_number} = {a_number_again - a_number:.3f}")
            elif a_number == a_number_again:
                print(f"{a_number} - {a_number_again} = 0")

        elif mode == "*":
            a_number = f_input("Select a number: ")
            a_number_again = f_input("Select another number: ")
            print(f"{a_number} * {a_number_again} = {a_number * a_number_again}")

        elif mode in ["Π", "*Σ", "PRO"]:
                product = 1
                n = i_input("Enter n: ")
                end = input("Enter the ending number (inf for infinity): ")
                print("If you wish to write a term, i will be the number (n).")
                term = def_input("Enter a term (Write in Python, optional): ","i")
                if str(end) != "inf":
                    for i in range(n,int(end)+1):
                        i2 = eval(term)
                        product*=i
                    print(f"Answer: {product}")
                else:
                    i=n
                    while True:
                        try:
                            if term:
                                i2 = eval(term)
                            else:
                                i2 = i
                            product*=i2
                            i+=1
                            print(f"Answer: {product}")
                        except KeyboardInterrupt:
                            break


        elif mode == "*T":
            try:
                a = i_input("Enter number: ")
                old_a = a
                if old_a > 400000000:
                    print("Too big of a number.")
                else:
                    max_val = input("Enter max value ( Enter to skip ): ")
                    max_val = max_val or 10
                    print(f"MULTIPLICATION TABLE OF {a}:")
                    max_val = int(max_val)
                    max_val += 1

                    for i in range(1, max_val):
                        print(f"{old_a} * {i} = {a}")
                        a += old_a
            except:
                print("An error has occured")

        elif mode == "**T":
            try:
                a = i_input("Enter number: ")
                old_a = a
                if old_a > 400000000:
                    print("Too big of a number.")
                else:
                    max_val = input("Enter max value ( Enter to skip ): ")
                    print(f"EXPONENTIAL TABLE OF {a}:")
                    if max_val == "":
                        maxv = 11
                    else:
                        maxv = int(max_val)
                        maxv += 1

                    for i in range(1, maxv):
                        print(f"{old_a} ** {i} = {a}")
                        a *= old_a
            except:
                print("An error has occured")

        elif mode == "/":
            a_number = f_input("Select a number: ")
            a_number_again = f_input("Select another number: ")
            print(f"{a_number} : {a_number_again} = {a_number / a_number_again}")

        elif mode == "\\":
            a_number = f_input("Select a number: ")
            a_number_again = f_input("Select another number: ")

            if a_number < a_number_again:
                print(f"{a_number_again} : {a_number} = {a_number_again / a_number:.3f}")
            elif a_number > a_number_again:
                print(f"{a_number} : {a_number_again} = {a_number / a_number_again:.3f}")
            elif a_number == a_number_again:
                print(f"{a_number} : {a_number_again} = 1")

        elif mode == "//%":
            a_number = f_input("Select a number: ")
            a_number_again = f_input("Select another number: ")

            if a_number < a_number_again:
                print(f"{a_number_again} // {a_number} = {a_number_again // a_number:.3f}")
                print(f"{a_number_again} % {a_number} = {a_number_again % a_number:.3f}")
            elif a_number > a_number_again:
                print(f"{a_number} // {a_number_again} = {a_number // a_number_again:.3f}")
                print(f"{a_number} % {a_number_again} = {a_number % a_number_again:.3f}")
            elif a_number == a_number_again:
                print(f"{a_number} // {a_number_again} = 1")

        elif mode == "DIV":
            def divisors(num):
                for j in range(1, num + 1):
                    lst = []
                    for i in range(1, j):
                        if j % i == 0:
                            lst.append(i)
                # ! If the list didn't reset, it would keep the old values and just add values that aren't needed!
                # Add num itself because you added 1, which counts for every number
                lst.append(num)
                print(f"Divisors of {num}: {lst}", end="")
                if len(lst) == 1:
                    print(f", Therefore {num} is a prime number.")


            divisors(i_input("Enter a number: "))

        elif mode == "PF":
            def is_prime(num):
                for i in range(2, (int(math.sqrt(num)) + 1)):
                    if num % i == 0:
                        return False
                else:
                    return True


            def prime_factors(num):
                if num <= 0:
                    return "Please enter a positive number."
                lst = set()
                for i in range(2, num + 1):
                    p = is_prime(i)
                    if p:
                        lst.add(i)
                for j in lst:
                    while num % j == 0:
                        print(f"{num} | {j}")
                        num = int(num / j)
                    else:
                        continue
                else:
                    return "1 | "


            print(prime_factors(i_input("Enter a number: ")))

        elif mode == "**":
            try:
                a_number = f_input("Enter a number: ")
                power = f_input("Enter the power: ")
                print(f"{a_number} ** {power} = {a_number ** power:.3f}")
            except OverflowError:
                print("An error has accured. The result number might be too big")
            except ValueError:
                print("An error has accured")

        elif mode == "%":
            a_percentage = f_input("Enter the percentage: ")
            a_number = f_input("Enter a number: ")
            perpro = a_number * a_percentage
            print(f"The {a_percentage}% of {a_number} is {perpro / 100:.3f}")
        
        elif mode=="F%":
            all = f_input("Enter whole: ")
            part = f_input("Enter part: ")
            per = (part / all) * 100
            print(f"{part} is {per}% of {all}")
             

        elif mode == "%2":
            evenorodd = f_input("Select a number: ")
            if evenorodd % 2 == 0:
                print(f"{evenorodd} is an even number")
            elif not evenorodd % 2 == 0:
                print(f"{evenorodd} is an odd number")

        elif mode == "ASC":
            def asc_order(lst):
                return sorted(lst)


            lst = []
            while True:
                nums = input("Please enter your numbers and type 'e' to have your answer: ")
                if nums.lower() == 'e':
                    print("Ascending order of your numbers are:", asc_order(lst))
                    break
                lst.append(int(nums))

        elif mode == "DESC":
            def desc_order(lst):
                return sorted(lst, reverse=True)


            lst = []
            while True:
                nums = input("Please enter your numbers and type 'e' to have your answer: ")
                if nums.lower() == "e":
                    print("Descending order of your numbers are:", desc_order(lst))
                    break
                lst.append(int(nums))

        elif mode == "P":
            def perfect(num):
                try:
                    lst = []

                    for i in range(1, num):
                        if num % i == 0:
                            lst.append(i)

                    if lst and lst[-1] == num:
                        lst.pop(-1)
                    answer = 0

                    for i in lst:
                        answer += i

                    if answer == num:
                        print(f"{num} is a perfect number")

                    else:
                        print(f"{num} is not a perfect number")
                except ValueError:
                    print("An error has accured, please make sure you have typed a number.")


            perf_input = i_input(f"Enter a number: ")
            perfect(perf_input)

        elif mode == "PR":
            a_number = i_input("Enter a number: ")


            def isprime(num):
                if num <= 1:
                    print("An error has occured. 1 or below are not prime numbers")
                    return False

                for i in range(2, int(math.sqrt(num) + 1)):
                    if num % i == 0:
                        print(f"{int(num)} is not a prime number.")
                        return False

                print(f"{int(num)} is a prime number.")


            isprime(a_number)

        elif mode == "COP":
            print("You can add values one by one, and every number must be positive!")
            lst = []

            while True:
                abc = i_input("Please enter 2+ numbers and type -1 to have your answer: ")
                if abc == -1:
                    if len(lst) < 2:
                        print("An error has accured, please enter more than 2 numbers.")
                        continue
                    else:
                        break
                elif abc <= -2 or abc == 0:
                    print("Please enter a number that is higher than -1 that is not 0")
                    continue
                lst.append(abc)

            flag = True

            for i in range((n := len(lst))):  # Thank python for the walrus operator
                for j in range(i + 1, n):
                    if math.gcd(lst[i], lst[j]) != 1:
                        flag = False
                        break
                if not flag:
                    break

            if flag:
                print(f"Every pair in {lst} is coprime")
            else:
                print(f"Every pair in {lst} is not coprime")

        elif mode == "PR+":
            end = i_input("Enter ending value: ")


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

                    if flag:
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
                    print("\nAll prime numbers mentioned:", prime_lst)
                    print(f"Prime amount: {len(prime_lst)}")
                    print("All non-prime numbers mentioned:", lst)
                    print(f"Non-prime amount: {len(lst)}")


            on_prime(end)

        elif mode == "P!":
            try:
                def prime_fact(num):
                    p_fact = []
                    div = 2
                    while num > 1:
                        while num % div == 0:
                            p_fact.append(str(div))
                            num = num // div
                        div += 1
                    return ' x '.join(p_fact)


                pf = i_input("Enter a number: ")
                print(f'The prime factorization of {pf} is', prime_fact(pf))
            except ValueError:
                print("An error has accured, please make sure you have typed a number.")
        
        elif mode=="ARM":
            a_number = input("Enter a number: ")
            sum = 0
            for letter in a_number:
                sum += int(letter) ** len(a_number)
            
            if int(a_number)==sum:
                print(f"{a_number} is an armstrong number.")
            else:
                print(f"{a_number} is not an armstrong number.")

        elif mode == "SQRT":
            a_number = f_input("Enter a number: ")
            b = a_number * a_number
            root = math.sqrt(abs(a_number))
            if a_number < 0:
                print(f"({a_number}) ** 2 = {b:.3f}")
                print(f"{a_number} ** 2 = -{b:.3f}")
                print(f"√{a_number} = ±{math.sqrt(abs(a_number)):.3f}i")
            else:
                print(f"{a_number} ** 2 = {b}")
                print(f"√{a_number} = {math.sqrt(a_number):.3f}")

        elif mode == "SQ":
            try:
                a_number = f_input("Enter a number: ")
                sqrt_number = math.sqrt(a_number)
                if a_number < 0:
                    print("Cannot calculate negative numbers!")

                if sqrt_number ** 2 == a_number:
                    print(f"{a_number} is a square number.")
                elif sqrt_number ** 2 != a_number:
                    print(f"{a_number} is not a square number.")
            except:
                print("An error has occured.")


        elif mode == "CBRT":
            a_number = f_input("Enter a number to cube: ")
            cube = float(a_number ** 3)
            print(f"3 ** {a_number} = {cube:.3f}\n∛{a_number} = {math.cbrt(a_number):.3f}")

        elif mode == "CB":
            try:
                a_number = f_input("Enter a number: ")
                cbrt_number = math.cbrt(a_number)
                if a_number < 0:
                    print("Cannot calculate negative numbers!")

                if cbrt_number ** 3 == a_number:
                    print(f"{a_number} is a cube number.")
                elif cbrt_number ** 3 != a_number:
                    print(f"{a_number} is not a cube number.")
            except:
                print("An error has occured.")

        elif mode=="O":
            o_mode = f_input("Enter a decimal number: ")
            if o_mode >= 0:
                rounded = math.floor(o_mode + 0.5)
            else:
                rounded = math.ceil(o_mode - 0.5)
            print(f"Rounded version of {o_mode} is {rounded}")

        elif mode=="R":
            def rounder(n):
                if n < 0:
                    print(f"{n} is not supported.")
                new = n
                while new % 10 != 0:
                    new += 1
                big = new - n

                new2 = n
                while new2 % 10 != 0:
                    new2 -= 1
                smol = n - new2

                if n % 10 == 0:
                    print(f"{n} is already rounded.")
                else:
                    if smol < big:
                        print(f"{n} is closer to {new2}")
                    elif big < smol:
                        print(f"{n} is closer to {new}")
                    elif big == smol and n % 5 == 0:
                        print(f"{n} is closer to {new}")


            rounder(i_input("Enter a number that isn't divisble by 10: "))


        elif mode=="+++":
            lst = []
            while True:
                abc = input("Please enter your numbers and type 'e' to have your answer: ")
                if abc == 'e':
                    if not lst:
                        print("An error has occured. Please enter some numbers next time.")
                        break
                    AO = sum(lst)/len(lst)
                    print(f"Arithmetic average of your numbers is {AO:.3f}")
                    break
                lst.append(int(abc))

        elif mode in ["~", "MED"]:
            lst = []
            while True:
                abc = input("Please enter your numbers and type 'e' to have your answer: ")
                if abc == 'e':
                    if not lst:
                        print("An error has occured. Please enter some numbers next time.")
                        break
                    AO = med(lst)
                    print(f"The median of your numbers is {AO:.3f}")
                    break
                lst.append(int(abc))


        elif mode == "RN":
            lst = []
            while True:
                abc = input("Please enter your numbers and type 'e' to have your answer: ")
                if abc == 'e':
                    if not lst:
                        print("An error has occured. Please enter some numbers next time.")
                        break
                    AO = float(max(lst) - min(lst))
                    print(f"The range of your numbers are: {AO:.3f}")
                    break
                lst.append(int(abc))

        elif mode == "MODE":
            lst = []
            while True:
                abc = input("Please enter your numbers and type 'e' to have your answer: ")
                if abc == 'e':
                    counter = Counter(lst)
                    val = []
                    for i in counter.values(): # If for loops didn't exist, this wouldn't
                        val.append(i)

                    most = max(val)
                    keys = []
                    for k, v in counter.items():
                        if v == most:
                            keys.append(k)

                    count = 0
                    for i in keys:
                        if count != 1:
                            print(f"{i} | Repeated {most} time(s).")
                            count += 1
                        else:
                            print(f"{i} |")

                    break
                lst.append(int(abc))

        elif mode=="PC":
            print("| 1 = 360 degree circle\n| 2 = 100% circle\n")
            pc_mode = i_input("Enter which pie you like: ")

            if pc_mode in (1,360):
                full = input("Enter the total amount: ")
                full = full or "360"
                full = int(full)

                piece = i_input("Enter the segment: ")

                if piece > full:
                    print("The value you enter must be lower than amount.")
                else:
                    old_piece = piece
                    piece *= 360
                    piece /= full
                    print(f"The degree of {old_piece} in {full} is {piece:.3f}")

            elif pc_mode in (2,100):
                full = input("Enter the full amount: ")
                full = full or "100"
                full = int(full)

                piece = i_input("Enter the piece: ")

                if piece > full:
                    print("The value you enter must be lower than amount.")
                else:
                    old_piece = piece
                    piece *= 100
                    piece /= full
                    print(f"The precent of {old_piece} in {full} is {piece:.3f}%")




        elif mode == "DEV":
            lst = []
            while True:
                abc = input("Please enter your numbers and type 'e' to have your answer: ")
                if abc == 'e':
                    print("The deviation of your numbers is:")
                    avg = sum(lst) / len(lst)
                    print(f"Average: {avg}")
                    for i, k in enumerate(lst):
                        print(f"{k}: {k - avg}")
                    break

                lst.append(int(abc))

        elif mode == "VAR":
            lst = []
            while True:
                abc = input("Please enter your numbers and type 'e' to have your answer: ")
                if abc == 'e':
                    avg = sum(lst) / len(lst)
                    i = 0
                    for _ in lst:
                        if lst[i] > int(avg):
                            lst[i] = lst[i] - avg
                        else:
                            lst[i] = avg - lst[i]
                        i += 1

                    i = 0
                    for _ in lst:
                        lst[i] = lst[i] ** 2
                        i += 1

                    avg = sum(lst) / len(lst)
                    print(f"The variance of your numbers is: {avg:.3f}")

                    break
                lst.append(int(abc))

        elif mode == "!":
            while True:
                factnum = i_input("Enter a number: ")
                if factnum <= 0:
                    print("Sorry, but you can't use 0 or negative numbers in factorial calculations.")
                elif factnum != 0:
                    fact = math.factorial(factnum)
                    print(f"{factnum}! = {fact}")
                    break

        elif mode == "||":
            try:
                a_number = i_input("Enter a number: ")
                print(f"|{a_number}| = {abs(a_number)}")
            except ValueError:
                print("Please enter a number.")

        elif mode=="RA":
            long = i_input("Enter the long side: ")
            short = i_input("Enter the short side: ")
            print(f"The area of your rectangle is {long * short}")

        elif mode=="PREC":
            long = i_input("Enter the long side: ")
            short = i_input("Enter the short side: ")
            print(f"The perimeter of your rectangle is {(long + short) * 2}")

        elif mode=="RV":
            w = i_input("Enter the width: ")
            l = i_input("Enter the length: ")
            h = i_input("Enter the height: ")
            print(f"The volume of your rectangular prism is {w * l * h}")

        elif mode == "CA":
            try:
                pi = i_input("Enter pi: ")
                radius = i_input("Enter radius: ")
                radiussqr = radius * radius
                print(f"The area of your circle is {radiussqr * pi:.3f}")
            except ValueError:
                print("Please enter a number.")

        elif mode == "CIR":
            try:
                pi = f_input("Enter pi: ")
                diameter = f_input("Enter diameter: ")
                print(f"The circumference of your circle is {diameter * pi:.3f}")
            except ValueError:
                print("Please enter a number.")

        elif mode=="SV":
            r = i_input("Enter the radius: ")
            pi = f_input("Enter pi: ")
            v = ((r ** 3) * pi)*(4/3)
            print(f"The volume of your sphere is {v}")

        elif mode == "ARCLEN":
            try:
                Pi = f_input("Enter pi (3,3.14): ")
                Angle = f_input("Enter angle: ")
                Radius = f_input("Enter the radius: ")
                if Radius == 0 or Radius < 0:
                    print("An error has accured. Radius being negative (-) or 0 is impossible in math.")
                elif Angle == 0:
                    print("The arc length of your circle is 0 (No angle).")
                elif Angle < 0:
                    print("An error has accured. Angles being negative (-) is impossible in math.")
                elif Angle > 0:
                    def arclength(angle, pi, rad):
                        pi = 2 * pi
                        value = pi * rad
                        value = value * angle
                        value = value / 360
                        print(f"The arc length of your circle sector is {value:.3f}")


                    arclength(Angle, Pi, Radius)
                else:
                    print("An error has accured. Please make sure you have typed a number")
            except ValueError:
                print("An error has accured. Please enter a number")

        elif mode=="M":
            h = f_input("Enter the height: ")
            b = f_input("Enter the base: ")
            slope(h,b)

        elif mode=="%M":
            h = f_input("Enter the height: ")
            b = f_input("Enter the base: ")
            per_slope(h,b)

        elif mode=="T!":
            edge = i_input("Enter an edge: ")
            edge2 = i_input("Enter another edge: ")

            if edge <= 0 or edge2 <= 0:
                print("An error has occured, edges must be positive.")
            else:
                edge_dif = abs(edge - edge2)
                edge_sum = edge + edge2

                print("Missing edge could be: ")
                lst = [str(i) for i in range(edge_dif + 1, edge_sum)] #TODO: Practice list comprehensions

                output = ', '.join(lst)
                print(f"{output}")

        elif mode=="TA":
            h = f_input("Enter the height:")
            b = f_input("Enter the base:")
            print(f"The area of your triangle is {(h * b) / 2}")

        elif mode=="TV":
            w = f_input("Enter the width: ")
            l = f_input("Enter the length: ")
            h = f_input("Enter the height: ")
            area = (w * h)/2
            print(f"The volume of your triangular prism is {area * l:.3f}")

        elif mode=="CV":
            h = f_input("Enter the height: ")
            r = f_input("Enter the radius: ")
            pi = f_input("Enter pi: ")
            v = pi * (r ** 2) * h
            print(f"The volume of your is {v:.3f}")

        elif mode=="CNV":
            h = f_input("Enter the height: ")
            r = f_input("Enter the radius: ")
            pi = f_input("Enter pi: ")
            v = (((r ** 2) * pi) * h)/3
            print(f"The volume of your cone is {v:.3f}")

        elif mode=="LCM":
            lst = []
            print("You can add values one by one, and every number must be positive.")

            while True:
                abc = i_input("Please enter 2+ numbers and type -1 to have your answer: ")
                lst.append(abc)
                if abc == -1:
                    lst.pop(-1)
                    if len(lst) < 2:
                        print(
                            "An error has accured. This can be caused by too few numbers, or a number being 0 or smaller.")
                        break
                    elif len(lst) >= 2:
                        AO = reduce(math.lcm, lst)
                        print(f"\nThe least common multiple of your numbers is {AO:.3f}")
                        break
                elif abc <= -2 or abc == 0:
                    print("Please enter a number that is higher than -1 that is not 0")

        elif mode == "GCD":
            lst = []
            print("You can add values one by one, and every number must be positive!")

            while True:
                abc = i_input("Please enter 2+ numbers and type -1 to have your answer: ")
                lst.append(abc)
                if abc == -1:
                    lst.pop(-1)
                    if len(lst) < 2:
                        print(
                            "An error has accured. This can be caused by too few numbers, or a number being 0 or smaller.")
                        break
                    elif len(lst) >= 2:
                        AO = reduce(math.gcd, lst)
                        print(f"\nThe greatest common divisor of your numbers is {AO:.3f}")
                        break
                elif abc <= -2 or abc == 0:
                    print("Please enter a number that is higher than -1 that is not 0.")

        elif mode == "S":
            num = f_input("Type a number: ")
            if num > 0:
                print(f"The sign of {num} is 1")
            elif num < 0:
                print(f"The sign of {num} is -1")
            elif num == 0:
                print(f"The sign of {num} is 0")
            else:
                print("An error has accured. Please choose a number.")

        elif mode == "LOG":
            print("Make sure you enter positive numbers (Especially for base number)!")
            base = f_input("Type base number: ")
            if base <= 0 or base == 1:
                print("An error has accured. Base too small and can not be 1.")
            elif base > 0:
                des = f_input("Type the destination: ")
                if des <= 0:
                    print("An error has accured. Destination too small.")
                elif base > 0:
                    num = math.log(des, base)
                    print(f"{base:.3f} must be raised to the power of {num:.3f} to get {des:.3f}")

        elif mode == "LN":
            power_of_e = f_input("Enter the power of e (Euler's number): ")
            e = 2.71828  # e ≈ 2.71828
            print(f"ln(e ** {power_of_e}) = {power_of_e:.3f}")
            # ln(e7) = 1096.63,
            # base: e
            # power: 7
            # destination: 1096.63

        elif mode == "E**":
            power_of_e = (input("Enter the power of e (Euler's number): "))
            if str(power_of_e) != "pi":
                new_e = 2.71828 ** float(power_of_e)
                print(f"e ** {power_of_e} = {new_e:.3f}")
            else:
                new_e = f_input("Enter pi: ")
                print(f"e ** π = {new_e:.3f}")

        elif mode == "SIN":
            opp = f_input("Enter the opposite edge: ")
            hyp = f_input("Enter the hypotenuse: ")
            print(f"sin(θ) = {opp / hyp:.3f}")

        elif mode == "COS":
            adj = f_input("Enter the adjacent edge: ")
            hyp = f_input("Enter the hypotenuse: ")
            print(f"cos(θ) = {adj / hyp:.3f}")

        elif mode == "TAN":
            adj = f_input("Enter the adjacent edge: ")
            opp = f_input("Enter the opposite edge: ")
            print(f"tan(θ) = {opp / adj:.3f}")

        elif mode == "CSC":
            hyp = f_input("Enter the hypotenuse: ")
            opp = f_input("Enter the opposite edge: ")
            print(f"csc(θ) = {hyp / opp:.3f}")

        elif mode == "SEC":
            hyp = f_input("Enter the hypotenuse: ")
            adj = f_input("Enter the adjacent edge: ")
            print(f"sec(θ) = {hyp / adj:.3f}")

        elif mode == "COT":
            adj = f_input("Enter the adjacent edge: ")
            opp = f_input("Enter the opposite edge: ")
            print(f"cot(θ) = {adj / opp:.3f}")

        elif mode == "PT":
            print("| HYP = Finding the hypotenuse\n| EDGE = Finding an edge\n| i = Info")
            HYPorEdge = str(input("Select which edge to calculate: ")).upper()

            if HYPorEdge == "HYP":
                AnEdge = f_input("Enter the value of an edge: ")
                AnotherEdge = f_input("Enter the value of another edge: ")


                def HYPcal(a, b):
                    asq = a * a
                    bsq = b * b
                    c = asq + bsq
                    answer = math.sqrt(c)
                    print(f"The hypotenuse of {a} and {b} is {answer:.3f}")


                HYPcal(AnEdge, AnotherEdge)

            elif HYPorEdge == "EDGE":
                AnEdge = f_input("Enter the value of an edge: ")
                hyp = f_input("Enter the value of hypotenuse: ")
                if hyp < AnEdge:
                    print("An error has accured, the hypotenuse was smaller than the edge you provided.")
                elif not hyp < AnEdge:
                    def EDGEcal(b, a):
                        asq = a * a
                        bsq = b * b
                        c = bsq - asq
                        answer = math.sqrt(c)
                        print(f"The other edge of {b} (hypotenuse) and {a} is {answer:.3f}")


                    EDGEcal(hyp, AnEdge)
                else:
                    print("An error has accured.")

            elif HYPorEdge == "I":
                if __name__ == "__main__":
                    print(f"PY.calc")
                    print(f"Currently {mode_count} modes avaible:\n| {mm_count} main modes,\n| {ucount} utilities.")
                    print(f"MADE WITH PYTHON 3.11.4 | Current Python version: {sys.version:.6}")
                    print(f"Being imported: No\nFile path: {__file__}")
                else:
                    print(f"PY.calc")
                    print(f"Currently {mode_count} modes avaible.")
                    print(f"MADE WITH PYTHON 3.11.4 | Current Python version: {sys.version:.6}")
                    print(f"Being imported: Yes\nFile path: {__file__}")

            else:
                print("Please choose a mode")

        elif mode == "PA":
            force = f_input("Enter force (F): ")
            surface = f_input("Enter surface area (S): ")
            pressure = force / surface
            print(f"Pressure (P) = {pressure} Pa")

        elif mode=="OHM":
            def Volt(curr, res):
                return f"Voltage (V) = {curr * res}"


            def Current(volt, res):
                if volt == 0:
                    return f"ERROR | Sorry, you can't divide numbers by 0\nVolt value (V): {volt} <-"
                elif res == 0:
                    return f"ERROR | Sorry, you can't divide numbers by 0\nResistance value (Ω): {res} <-"
                else:
                    return f"Current (I) = {volt / res}"


            def Resistance(volt, curr):
                if volt == 0:
                    return f"ERROR | Sorry, you can't divide numbers by 0\nVolt value (V): {volt} <-"
                elif curr == 0:
                    return f"ERROR | Sorry, you can't divide numbers by 0\nCurrent value (A): {curr} <-"
                else:
                    return f"Resistance (Ω) = {volt / curr}"


            print("| Voltage (V)\n| Current (A)\n| Resistance (Ω)")
            conv = str(input("Enter one of the modes above: ")).upper()

            if conv in ("VOLTAGE", "V"):
                curr = f_input("Current (A): ")
                res = f_input("Resistance (Ω): ")
                print(Volt(curr, res))

            elif conv in ("CURRENT", "A"):
                volt = f_input("Voltage (V): ")
                res = f_input("Resistance (Ω): ")
                print(Current(volt, res))

            elif conv in ("RESISTANCE", "Ω"):
                volt = f_input("Voltage (V): ")
                curr = f_input("Current (A): ")
                print(Resistance(volt, curr))

        elif mode == "MS":
            s_modes = {
                "F": "Fibonacci sequence",
                "FS": "Fibonacci series",
                "P": "Pell numbers",
                "PS": "Pell series",
                "B": "Bronze sequence",
                "BS": "Bronze series",
                "C": "Copper sequence",
                "CS": "Copper series",
                "L": "Lucas numbers",
                "LS": "Lucas series",
                "i": "Info"
            }
            for k,v in s_modes.items():
                print(f"| {k} = {v}")
            seq = str(input("\nEnter a sequence/series: ")).upper()

            if seq == "F":  # Why was this so hard?
                n = i_input("Enter a number: ")
                if n < 2:
                    print(f"F({n}) = {n}")
                elif n > 2:
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

            elif seq == "FS":
                n = i_input("Enter a number: ")
                if n < 2:
                    print(f"F({n}) = {n}")
                elif n > 2:
                    def fib(n):
                        a = 0
                        b = 1
                        F = 0
                        print("F(0) = 0")
                        for looptimes in range(n):
                            F += 1
                            old_a = a
                            a = b
                            b = old_a + b
                            print(f"F({F}) = {a}")


                    fib(n)
                else:
                    print("An error has accured.")

            elif seq == "P":  # Fibonacci to the rescue
                n = i_input("Enter a number: ")
                if n == 0 or n == 1:
                    print(f"P({n}) = {n}")
                elif n > 2:
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

            elif seq == "PS":
                n = i_input("Enter a number: ")
                if n == 0 or n == 1:
                    print(f"P({n}) = {n}")
                elif n > 2:
                    def pell(n):
                        a = 0
                        b = 1
                        P = 0
                        print("P(0) = 0")
                        for looptimes in range(n):
                            P += 1
                            old_a = a
                            a = b
                            print(f"P({P}) = {a}")
                            b = old_a + 2 * b
                            Silver_ratio_δₛ = 2.414


                    pell(n)
                else:
                    print("An error has accured.")

            elif seq == "B":  # Pell to the rescue
                n = i_input("Enter a number: ")
                if n == 0 or n == 1:
                    print(f"B({n}) = {n}")
                elif n > 2:
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

            elif seq == "BS":
                n = i_input("Enter a number: ")
                if n == 0 or n == 1:
                    print(f"B({n}) = {n}")
                elif n > 2:
                    def Bronze(n):
                        a = 0
                        b = 1
                        B = 0
                        print("B(0) = 0")
                        for looptimes in range(n):
                            B += 1
                            old_a = a
                            a = b
                            b = old_a + 3 * b
                            print(f"B({B}) = {a}")


                    Bronze(n)
                else:
                    print("An error has accured.")

            elif seq == "C":  # Bronze to the rescue
                n = i_input("Enter a number: ")
                if n == 0 or n == 1:
                    print(f"C({n}) = {n}")
                elif n > 2:
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

            elif seq == "CS":
                n = i_input("Enter a number: ")
                if n == 0 or n == 1:
                    print(f"C({n}) = {n}")
                elif n > 2:
                    def copper(n):
                        a = 0
                        b = 1
                        C = 0
                        print("C(0) = 0")
                        for looptimes in range(n):
                            C += 1
                            old_a = a
                            a = b
                            b = old_a + 4 * b
                            print(f"C({C}) = {a}")
                        return a


                    copper(n)
                else:
                    print("An error has accured.")

            if seq=="L":
                n = i_input("Enter a number: ")
                if n == 0:
                    print(f"L(0) = {2}")
                elif n == 1:
                    print(f"L(1) = {1}")
                elif n > 2:
                    def lucas(n):
                        a = 2
                        b = 1
                        for looptimes in range(n):
                            old_a = a
                            a = b
                            b = old_a + b
                            Golden_ratio_φ = 1.618
                        return a
                    print(f"L({n}) = {lucas(n)}")
                else:
                    print("An error has accured.")

            elif seq == "LS":
                n = i_input("Enter a number: ")
                if n == 0:
                    print(f"L(0) = {2}")
                elif n == 1:
                    print(f"L(1) = {1}")
                elif n > 2:
                    def lucas(n):
                        a = 2
                        b = 1
                        F = 0
                        print("L(0) = 2")
                        for looptimes in range(n):
                            F += 1
                            old_a = a
                            a = b
                            b = old_a + b
                            print(f"L({F}) = {a}")


                    lucas(n)
                else:
                    print("An error has accured.")

            elif seq == "I":
                if __name__ == "__main__":
                    print(f"PY.calc")
                    print(f"Currently {mode_count} modes avaible:\n| {mm_count} main modes,\n| {ucount} utilities.")
                    print(f"MADE WITH PYTHON 3.11.4 | Current Python version: {sys.version:.6}")
                    print(f"Being imported: No\nFile path: {__file__}")
                else:
                    print(f"PY.calc")
                    print(f"Currently {mode_count} modes avaible.")
                    print(f"MADE WITH PYTHON 3.11.4 | Current Python version: {sys.version:.6}")
                    print(f"Being imported: Yes\nFile path: {__file__}")

            else:
                print("Please choose a mode")

        elif mode=="TEST":
            amount = input("Enter the required points to pass (ENTER for inf): ")
            if amount != "":
                Score = 0
                IsLast = False
                clear()
                while Score < int(amount):
                    questions = {
                        "What is the 6th element of the fibbonacci sequence?": "8",
                        "(50 + 24) - 100 = ?": "-24",
                        "Which version of Python was used to make PY.calc?": "3.11.4",
                        "What is the average of this array: [150, 20, 30, 0]": "50",
                        "What is the median of this array: [40, 20, 30, 60]": "25",
                        "(250 / 25) * 5 = ?": "50",
                        "The signum of -2145629124": "-1",
                        "Find the GCD of this array: [60, 45, 90, 105]": "15",
                        "Find the LCM of this array: [6, 15, 90, 57]": "1",
                        "Find the LCM of this array: [7, 56, 112, 8]": "112",
                        "Find the GCD of this array: [1, 2, 3, 4, 5, 6, 7]": "1",
                        "Name the biggest prime factor of 57": "19",
                        "Name the person who found the unit of pressure": "blaise pascal",
                        'Name the Scottish inventor that made a unit of power called a "Watt".': "james watt",
                        "(√16)! = ?": "24",
                        "abs(-56) = ?": "56",
                        "Round this number in decimal: 56.6": "57",
                        "Round this number: 124": "120",
                        "(√16 ** 2) ** 2 = ?": "256",
                        "Is 120 a perfect number? (T or F)": "F",
                        "Is 91 a prime number? (T or F)": "T",
                        "Is 56 a prime number? (T or F)": "F",
                        "If the average of an array is 50, what is the deviation of 24?": "-26",
                        "If the average of an array is 562, what is the deviation of 1000?": "438",
                        "What is the range of this array: [56, 24, 3, 76, 18, 109]": "106",
                        "What is the range of this array: [408, 506, 812, 41, 961]": "920",
                        "What is the range of this array: [0, 1, 51, 801, 1080, 18, 3]": "1080",
                        "What is the area of a triangle where h = 10 and b = 4": "20",
                        "What is the volume of a sphere where r = 3? (π = 3)": "108",
                        "ln(e^78188) = ?": "78188",
                        "In a triangle: if a = 3 and b = 4, c = ?": "5",
                        "What is 10% of 500000?": "50000",
                    }

                    qk = []
                    for k in questions.keys():
                        qk.append(k)
                    question = cho(qk)
                    answer = questions[question].lower()

                    print(f"Current score: {Score}")
                    print(f"{question}")
                    user_answer = input("Answer: ").strip().lower()
                    if user_answer in ["e","exit"]:
                        break

                    elif user_answer == answer:
                        print(f"Yes! The answer is {answer.upper()}.")
                        sleep(0.5)
                        Score += 1
                        if int(amount) == Score:
                            break
                        close(0.3, 4, "Generating new question")

                    elif user_answer in ["s","skip"]:
                        if Score != 0:
                            Score -= 1
                        close(0.3, 2, "Skipping")

                    else:
                        print(f"Wrong! The answer is {answer.upper()}.")
                        close(0.3, 4, "Generating new question")

                close(0.3, 4, "Exiting test")
                intro()

            else:

                Score = 0
                clear()
                q_count = 0
                while True:
                    questions = {
                        "What is the 6th element of the Fibbonacci sequence?": "8",
                        "(50 + 24) - 100 = ?": "-24",
                        "Which version of Python was used to make PY.calc?": "3.11.4",
                        "What is the average of this array: [150, 20, 30, 0]": "50",
                        "What is the median of this array: [40, 20, 30, 60]": "25",
                        "(250 / 25) * 5 = ?": "50",
                        "The signum of -2145629124": "-1",
                        "Find the GCD of this array: [60, 45, 90, 105]": "15",
                        "Find the LCM of this array: [6, 15, 90, 57]": "1",
                        "Find the LCM of this array: [7, 56, 112, 8]": "112",
                        "Find the GCD of this array: [1, 2, 3, 4, 5, 6, 7]": "1",
                        "Name the biggest prime factor of 57": "19",
                        "Name the person who found the unit of pressure": "blaise pascal",
                        'Name the Scottish inventor that made a unit of power called a "Watt".': "james watt",
                        "(√16)! = ?": "24",
                        "abs(-56) = ?": "56",
                        "Round this number in decimal: 56.6": "57",
                        "Round this number: 124": "120",
                        "(√16 ** 2) ** 2 = ?": "256",
                        "Is 120 a perfect number? (T or F)": "F",
                        "Is 91 a prime number? (T or F)": "T",
                        "Is 56 a prime number? (T or F)": "F",
                        "If the average of an array is 50, what is the deviation of 24?": "-26",
                        "If the average of an array is 562, what is the deviation of 1000?": "438",
                        "What is the range of this array: [56, 24, 3, 76, 18, 109]": "106",
                        "What is the range of this array: [408, 506, 812, 41, 961]": "920",
                        "What is the range of this array: [0, 1, 51, 801, 1080, 18, 3]": "1080",
                        "What is the area of a triangle where h = 10 and b = 4": "20",
                        "What is the volume of a sphere where r = 3? (π = 3)": "108",
                        "ln(e^78188) = ?": "78188",
                        "In a triangle: if a = 3 and b = 4, c = ?": "5",
                        "What is 10% of 500000?": "50000",
                    }

                    qk = []
                    for k in questions.keys():
                        qk.append(k)
                    question = cho(qk)
                    answer = questions[question].lower()

                    q_count += 1
                    print(f"Current score: {Score}")
                    print(f"Question {q_count}:")
                    print(f"{question}")
                    user_answer = input("Answer: ").strip().lower()
                    if user_answer in ["e","exit"]:
                        break

                    elif user_answer == answer:
                        print(f"Yes! The answer is {answer.upper()}.")
                        sleep(0.5)
                        close(0.3, 4, "Generating new question")
                        Score += 1

                    elif user_answer in ["s","skip"]:
                        if Score != 0:
                            Score -= 1
                        close(0.3, 2, "Skipping")

                    else:
                        print(f"Wrong! The answer is {answer.upper()}.")
                        close(0.3, 4, "Generating new question")

                close(0.3, 4, "Exiting test")
                intro()

        elif mode == "MD":
            lst = mset_func()
            elst = emset_func()
            nlst = list(lst.keys())
            enlst = list(elst.keys())

            print(f"Main modes:\n{', '.join(nlst)}")
            print(f"\nExtra modes:\n{', '.join(enlst)}")

        elif mode=="CON":
            print("Welcome to the Converter! It converts Metric units to Imperial units,")
            print("and Imperial units to Metric units!\n")
            print("| C = Celcius/Farenheit\n| F = Farenheit/Celcius")
            print("| LBS = Pounds/Kilograms\n| KG = Kilograms/Pounds")
            print("| KM = Kilometres/Miles\n| MI = Miles/Kilometres")
            print("| L = Litres/Gallons\n| GAL = Gallons/Litres")
            print("| CM = Centimetres/Feet\n| FT = Feet/Centimetres")
            print("| G = Grams/Ounce\n| OZ = Ounce/Grams")
            print("| M = Metres/Yards\n| YD = Yards/Metres\n")

            while True:
                try:
                    choice = input("What would you like to convert? (Press 'Enter' to quit): ").upper().strip()

                    if choice == "":
                        print("Goodbye!")
                        break

                    elif choice.upper() == "C":
                        def CtoF(value):
                            value *= 9
                            value /= 5
                            value += 32
                            print(f"Fahrenheit (F): {value:.3f} ️")


                        Cvalue = f_input("Celsius (C): ")
                        CtoF(Cvalue)
                        break

                    elif choice.upper() == "F":
                        def FtoC(value):
                            value -= 32
                            value *= 5
                            value /= 9
                            print(f"Celsius (C): {value:.3f} ️")


                        Fvalue = f_input("Fahrenheit (F): ")
                        FtoC(Fvalue)
                        break

                    elif choice.upper() == "LBS":
                        def LBStoKG(value):
                            value /= 2.20462
                            print(f"Kilograms (KG): {value:.3f} ")


                        libbis = f_input("Pounds (LBS): ")
                        LBStoKG(libbis)
                        

                    elif choice.upper() == "KG":
                        def KGtoLBS(value):
                            value *= 2.20462
                            print(f"Pounds (LBS): {value:.3f} ")


                        KGvalue = f_input("Kilograms (KG): ")
                        KGtoLBS(KGvalue)
                        break

                    elif choice.upper() == "KM":
                        def KMtoMi(value):
                            value *= 0.62
                            print(f"Miles (Mi): {value:.3f} ")


                        KMvalue = f_input("Kilometres (KM): ")
                        KMtoMi(KMvalue)
                        break

                    elif choice.upper() == "MI":
                        def MItoKM(value):
                            value /= 0.62
                            print(f"Kilometres (KM): {value:.3f} ️")


                        MIvalue = f_input("Miles (Mi): ")
                        MItoKM(MIvalue)
                        break

                    elif choice.upper() == "L":
                        def LtoGAL(value):
                            value *= 0.264172
                            print(f"Gallons (GAL): {value:.3f} ")


                        Lvalue = f_input("Litres (L): ")
                        LtoGAL(Lvalue)
                        break

                    elif choice.upper() == "GAL":
                        def GALtoL(value):
                            value /= 0.264172
                            print(f"Litres (L): {value:.3f} ")


                        GALvalue = f_input("Gallons (GAL): ")
                        GALtoL(GALvalue)
                        break

                    elif choice.upper() == "CM":
                        def CMtoFT(value):
                            value /= 30.48
                            print(f"Feet (FT): {value:.3f} ")


                        CMvalue = f_input("Centimetres (CM): ")
                        CMtoFT(CMvalue)
                        break

                    elif choice.upper() == "FT":
                        def FTtoCM(value):
                            value *= 30.48
                            print(f"Centimetres (CM): {value:.3f} ")


                        FTvalue = f_input("Feet (FT): ")
                        FTtoCM(FTvalue)
                        break
                    elif choice.upper() == "G":
                        def GtoOZ(value):
                            value /= 28.34952
                            print(f"Ounces (OZ): {value:.3f} ️")


                        Gvalue = f_input("Grams (G): ")
                        GtoOZ(Gvalue)
                        break

                    elif choice.upper() == "OZ":
                        def OZtoG(value):
                            value *= 28.34952
                            print(f"Grams (G): {value:.3f} ️")


                        OZvalue = f_input("Ounces (OZ): ")
                        OZtoG(OZvalue)
                        break

                    elif choice.upper() == "M":
                        def MtoYD(value):
                            value *= 1.09361
                            print(f"Yards (YD): {value:.3f} ")


                        Mvalue = f_input("Metres (M): ")
                        MtoYD(Mvalue)
                        break

                    elif choice.upper() == "YD":
                        def YDtoM(value):
                            value /= 1.09361
                            print(f"Metres (M): {value:.3f} ")


                        Mvalue = f_input("Yards (YD): ")
                        YDtoM(Mvalue)
                        break

                except ZeroDivisionError:
                    print("An error has occured. You can't divide by 0.")

        elif mode == "NET":
            questions_done = i_input("Questions done: ")
            wrongs = i_input("Wrong questions done: ")
            net = abs(questions_done - wrongs)

            for _ in range(wrongs):
                net -= 1/3

            print(f"Net score: ~{net:.2f}")

        elif mode=="RAND":
            n = rand(1, 100)
            print("I am thinking of a number from 1 to 100.")
            while True:
                guess = i_input("Enter guess: ")

                if guess < n:
                    print("Too low! Try again.\n")
                elif guess > n:
                    print("Too high! Try again.\n")
                elif guess == n:
                    print(f"Yep, i was thinking of {n}.")
                    break

        elif mode == "RNG":
                most = def_input("Enter the maximum value (Default: 6): ", 6)

                least = def_input("Enter the minimum value (Default: 1): ", 1)

                repeat = def_input("How many times should this be repeated? (Default: 3): ", 3)

                index = def_input("Enable indexing (1: On | 0: Off): ", 1)

                if int(index) == 1:
                    for i in range(int(repeat)):
                        print(f"{i + 1}: {rand(int(least), int(most))}")

                else:
                    for i in range(int(repeat)):
                        print(f"{rand(int(least), int(most))}")

        elif mode == "I":
            if __name__ == "__main__":
                print(f"PY.calc")
                print(f"Currently {mode_count} modes avaible:\n| {mm_count} main modes,\n| {ucount} utilities.")
                print(f"MADE WITH PYTHON 3.11.4 | Current Python version: {sys.version:.6}")
                print(f"Being imported: No\nFile path: {__file__}")
            else:
                print(f"PY.calc")
                print(f"Currently {mode_count} modes avaible.")
                print(f"MADE WITH PYTHON 3.11.4 | Current Python version: {sys.version:.6}")
                print(f"Being imported: Yes\nFile path: {__file__}")

        elif mode == "CLS":
            clear()
            intro()

        elif mode == "E":
            close(0.2, 2)
            break

        else:
            print(f'"{mode.lower()}" is not a mode.')

except ValueError:
    print("An error has accured, please make sure you have typed a number.")
except ZeroDivisionError:
    print("An error has accured while dividing number with 0.")
except KeyboardInterrupt:
    close(0.2, 2)

sys.exit(0)