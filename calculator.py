import numpy as np
import math as mt
import sys
from os import system, name
from time import sleep
from random import randint as rand, choice as cho
from collections import Counter


# 56 main modes
# 6 extra modes

def clear():
    system('cls' if name == 'nt' else 'clear')


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
        "-": "Subtraction",
        "--": "Subtraction with negative numbers",
        "*": "Multiplication",
        "*Σ": "Multiplicated sum",
        "*T": "Multiplication Table",
        "**T": "Exponential Chart",
        "/": "Division",
        "//%": "Floor division with remainder",
        "DIV": "Divisor finder",
        "PF": "Prime factors",
        "**": "Exponents",
        "%": "Percentages",
        "%2": "Even or odd",
        "ASC": "Order numbers in ascending order",
        "DESC": "Order numbers in descending order",
        "P": "Perfect number checking",
        "PR": "Prime checking",
        "COP": "Coprime checking",
        "PR+": "Series of prime numbers",
        "P!": "Prime Factorization",
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
        "CG": "Circle graphing",
        "VAR": "Variance",
        "!": "Factorial",
        "||": "Absolute value",
        "CA": "Circle Area",
        "Cir": "Circumference of the circle",
        "ARCLEN": "Circle arc length",
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
        "M": "Display all mode shortcuts",
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
    print("I -~- MAIN -~- I")
    for k, v in mset.items():
        print(f"{k} = {v}")
        mlst.append(k)

    print("\nI -~- UTILITIES / SPECIAL -~- I")
    for k, v in extra_mset.items():
        print(f"{k} = {v}")
        mlst.append(k)

    mode_count = len(mlst)
    return mode_count


try:
    mode = ""
    mode_count = intro()
    condition = True

    while condition:
        mode = input("\nEnter a mode: ").upper().strip()

        if mode == "+":
            a_number = float(input("Select a number: "))
            a_number_again = float(input("Select another number: "))
            print(f"{a_number} + {a_number_again} = {a_number + a_number_again:.3f}")

        elif mode in ["Σ", "SUM"]:
            lst = []
            while True:
                num = float(input("Enter all your numbers and type 0 to have your answer: "))
                if num == 0:
                    print(f"The sum of all your numbers are: {sum(lst)}")
                    break
                lst.append(num)

        elif mode == "-":
            a_number = float(input("Select a number: "))
            a_number_again = float(input("Select another number: "))

            if a_number < a_number_again:
                print(f"{a_number_again} - {a_number} = {a_number_again - a_number:.3f}")
            elif a_number > a_number_again:
                print(f"{a_number} - {a_number_again} = {a_number - a_number_again:.3f}")
            elif a_number == a_number_again:
                print(f"{a_number} - {a_number_again} = 0")

        elif mode == "--":
            a_number = float(input("Select a number: "))
            a_number_again = float(input("Select another number: "))

            if a_number < a_number_again:
                print(f"{a_number} - {a_number_again} = {a_number - a_number_again:.3f}")
            elif a_number > a_number_again:
                print(f"{a_number_again} - {a_number} = {a_number_again - a_number:.3f}")
            elif a_number == a_number_again:
                print(f"{a_number} - {a_number_again} = 0")

        elif mode == "*":
            a_number = float(input("Select a number: "))
            a_number_again = float(input("Select another number: "))
            print(f"{a_number} * {a_number_again} = {a_number * a_number_again}")

        elif mode in ["*Σ", "*SUM"]:
            def mul_sum(lst):
                answer = 1
                for i in lst:
                    answer *= i
                return answer


            lst = []
            while True:
                num = float(input("Enter all your numbers and type 0 to have your answer: "))
                if num == 0:
                    print(f"The multplicated sum of all your numbers are: {mul_sum(lst)}")
                    break
                lst.append(num)

        elif mode == "*T":
            try:
                a = int(input("Enter number: "))
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
                a = int(input("Enter number: "))
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
            a_number = float(input("Select a number: "))
            a_number_again = float(input("Select another number: "))

            if a_number < a_number_again:
                print(f"{a_number_again} / {a_number} = {a_number_again / a_number:.3f}")
            elif a_number > a_number_again:
                print(f"{a_number} / {a_number_again} = {a_number / a_number_again:.3f}")
            elif a_number == a_number_again:
                print(f"{a_number} / {a_number_again} = 1")

        elif mode == "//%":
            a_number = float(input("Select a number: "))
            a_number_again = float(input("Select another number: "))

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


            number = int(input("Enter a number: "))
            divisors(number)

        elif mode == "PF":
            def is_prime(num):
                for i in range(2, (int(np.sqrt(num)) + 1)):
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


            print(prime_factors(int(input("Enter a number: "))))

        elif mode == "**":
            try:
                a_number = float(input("Enter a number: "))
                power = float(input("Enter the power: "))
                print(f"{a_number} ** {power} = {a_number ** power:.3f}")
            except OverflowError:
                print("An error has accured. The result number might be too big")
            except ValueError:
                print("An error has accured")

        elif mode == "%":
            a_percentage = float(input("Enter the percentage: "))
            a_number = float(input("Enter a number: "))
            perpro = a_number * a_percentage
            print(f"The {a_percentage}% of {a_number} is {perpro / 100:.3f}")

        elif mode == "%2":
            evenorodd = float(input("Select a number: "))
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


            perf_input = int(input(f"Enter a number: "))
            perfect(perf_input)

        elif mode == "PR":
            a_number = int(input("Enter a number: "))


            def isprime(num):
                if num <= 1:
                    print("An error has occured. 1 or below are not prime numbers")
                    return False

                for i in range(2, int(np.sqrt(num) + 1)):
                    if num % i == 0:
                        print(f"{int(num)} is not a prime number.")
                        return False

                print(f"{int(num)} is a prime number.")


            isprime(a_number)

        elif mode == "COP":
            print("You can add values one by one, and every number must be positive!")
            lst = []

            while True:
                abc = int(input("Please enter 2+ numbers and type -1 to have your answer: "))
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
                    if mt.gcd(lst[i], lst[j]) != 1:
                        flag = False
                        break
                if not flag:
                    break

            if flag:
                print(f"Every pair in {lst} is coprime")
            else:
                print(f"Every pair in {lst} is not coprime")

        elif mode == "PR+":
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


                pf = int(input("Enter a number: "))
                print(f'The prime factorization of {pf} is', prime_fact(pf))
            except ValueError:
                print("An error has accured, please make sure you have typed a number.")

        elif mode == "SQRT":
            a_number = float(input("Enter a number to square: "))
            b = a_number * a_number
            root = np.sqrt(abs(a_number))
            if a_number < 0:
                print(f"({a_number}) ** 2 = {b:.3f}.")
                print(f"{a_number} ** 2 = -{b:.3f}.")
                print(f"√{a_number} = ±{np.sqrt(abs(a_number)):.3f}i")
            else:
                print(f"{a_number} ** 2 = {b}")
                print(f"√{a_number} = {np.sqrt(a_number):.3f}.")
                print(f"-√{a_number} = -{np.sqrt(a_number):.3f}.")

        elif mode == "SQ":
            try:
                a_number = float(input("Enter a number: "))
                sqrt_number = np.sqrt(a_number)
                if a_number < 0:
                    print("Cannot calculate square root of negative number!")

                if sqrt_number ** 2 == a_number:
                    print(f"{a_number} is a square number.")
                elif sqrt_number ** 2 != a_number:
                    print(f"{a_number} is not a square number.")
            except:
                print("An error has occured.")


        elif mode == "CBRT":
            a_number = float(input("Enter a number to cube: "))
            cube = float(a_number ** 3)
            print(f"3 ** {a_number} = {cube:.3f}.\n∛{a_number} = {np.cbrt(a_number):.3f}")
            print(f"-∛{a_number} = -{np.cbrt(abs(a_number)):.3f}")

        elif mode == "CB":
            try:
                a_number = float(input("Enter a number: "))
                cbrt_number = np.cbrt(a_number)

                if cbrt_number ** 3 == a_number:
                    print(f"{a_number} is a cube number.")
                elif cbrt_number ** 3 != a_number:
                    print(f"{a_number} is not a cube number.")
            except:
                print("An error has occured.")

        elif mode == "O":
            mode = float(input("Enter a decimal number: "))
            if mode >= 0:
                rounded = mt.floor(mode + 0.5)
            else:
                rounded = mt.ceil(mode - 0.5)
            print(f"Rounded version of {mode} is {rounded}.")

        elif mode == "R":
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
                        print(f"{n} is closer to {new2}.")
                    elif big < smol:
                        print(f"{n} is closer to {new}.")
                    elif big == smol and n % 5 == 0:
                        print(f"{n} is closer to {new}")


            rounder(int(input("Enter a number that isn't divisble by 10: ")))


        elif mode == "+++":
            liste = []
            while True:
                abc = input("Please enter your numbers and type 'e' to have your answer: ")
                if abc == 'e':
                    AO = np.mean(liste)
                    print(f"Arithmetic average of your numbers is {AO:.3f}")
                    break
                liste.append(int(abc))

        elif mode in ["~", "MED"]:
            liste = []
            while True:
                abc = input("Please enter your numbers and type 'e' to have your answer: ")
                if abc == 'e':
                    AO = np.median(liste)
                    print(f"The median of your numbers is {AO:.3f}")
                    break
                liste.append(int(abc))


        elif mode == "RN":
            lst = []
            while True:
                abc = input("Please enter your numbers and type 'e' to have your answer: ")
                if abc == 'e':
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

        elif mode=="CG":
            print("| 1 = 360 degree circle\n| 2 = 100% circle\n")
            mode = int(input("Enter which pie you like: "))

            if mode in (1,360):
                full = input("Enter the total amount: ")
                full = full or "360"
                full = int(full)

                piece = int(input("Enter the segment: "))

                if piece > full:
                    print("The value you enter must be lower than amount.")
                else:
                    old_piece = piece
                    piece *= 360
                    piece /= full
                    print(f"The degree of {old_piece} in {full} is {piece:.3f}")

            elif mode in (2,100):
                full = input("Enter the full amount: ")
                full = full or "100"
                full = int(full)

                piece = int(input("Enter the piece: "))

                if piece > full:
                    print("The value you enter must be lower than amount.")
                else:
                    old_piece = piece
                    piece *= 100
                    piece /= full
                    print(f"The degree of {old_piece} in {full} is {piece:.3f}")




        elif mode == "DEV":
            lst = []
            while True:
                abc = input("Please enter your numbers and type 'e' to have your answer: ")
                if abc == 'e':
                    print("The deviation of your numbers is:")
                    avg = sum(lst) / len(lst)
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
                factnum = int(input("Enter a number: "))
                if factnum <= 0:
                    print("Sorry, but you can't use 0 or negative numbers in factorial calculations.")
                elif factnum != 0:
                    fact = mt.factorial(factnum)
                    print(f"{factnum}! = {fact}")
                    break

        elif mode == "||":
            try:
                a_number = int(input("Enter a number: "))
                print(f"|{a_number}| = {abs(a_number)}")
            except ValueError:
                print("Please enter a number.")

        elif mode == "CA":
            try:
                pi = int(input("Enter pi: "))
                radius = int(input("Enter radius: "))
                radiussqr = radius * radius
                print(f"The area of your circle is {radiussqr * pi:.3f}")
            except ValueError:
                print("Please enter a number.")

        elif mode == "CIR":
            try:
                pi = float(input("Enter pi: "))
                diameter = float(input("Enter diameter: "))
                print(f"The circumference of your circle is {diameter * pi:.3f}")
            except ValueError:
                print("Please enter a number.")

        elif mode == "ARCLEN":
            try:
                Pi = float(input("Enter pi (3,3.14): "))
                Angle = float(input("Enter angle: "))
                Radius = float(input("Enter the radius: "))
                if Radius == 0 or Radius < 0:
                    print("An error has accured. Radius being negative (-) or 0 is impossible in math")
                elif Angle == 0:
                    print("The arc length of your circle is 0 (No angle)")
                elif Angle < 0:
                    print("An error has accured. Angles being negative (-) is impossible in math")
                elif Angle > 0:
                    def arclenght(angle, pi, rad):
                        pi = 2 * pi
                        value = pi * rad
                        value = value * angle
                        value = value / 360
                        print(f"The arc length of your circle sector is {value:.3f}")


                    arclenght(Angle, Pi, Radius)
                else:
                    print("An error has accured. Please make sure you have typed a number")
            except ValueError:
                print("An error has accured. Please enter a number")

        elif mode == "LCM":
            lst = []
            print("You can add values one by one, and every number must be positive.")

            while True:
                abc = int(input("Please enter 2+ numbers and type -1 to have your answer: "))
                lst.append(abc)
                if abc == -1:
                    lst.pop(-1)
                    if len(lst) < 2:
                        print(
                            "An error has accured. This can be caused by too few numbers, or a number being 0 or smaller.")
                        break
                    elif len(lst) >= 2:
                        AO = int(np.lcm.reduce(lst))
                        print(f"\nThe least common multiple of your numbers is {AO:.3f}")
                        break
                elif abc <= -2 or abc == 0:
                    print("Please enter a number that is higher than -1 that is not 0")

        elif mode == "GCD":
            lst = []
            print("You can add values one by one, and every number must be positive!")

            while True:
                abc = int(input("Please enter 2+ numbers and type -1 to have your answer: "))
                lst.append(abc)
                if abc == -1:
                    lst.pop(-1)
                    if len(lst) < 2:
                        print(
                            "An error has accured. This can be caused by too few numbers, or a number being 0 or smaller.")
                        break
                    elif len(lst) >= 2:
                        AO = int(np.gcd.reduce(lst))
                        print(f"\nThe greatest common divisor of your numbers is {AO:.3f}")
                        break
                elif abc <= -2 or abc == 0:
                    print("Please enter a number that is higher than -1 that is not 0.")

        elif mode == "S":
            num = float(input("Type a number: "))
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
            base = float(input("Type base number: "))
            if base <= 0 or base == 1:
                print("An error has accured. Base too small and can not be 1.")
            elif base > 0:
                des = float(input("Type the destination: "))
                if des <= 0:
                    print("An error has accured. Destination too small.")
                elif base > 0:
                    num = mt.log(des, base)
                    print(f"{base:.3f} must be raised to the power of {num:.3f} to get {des:.3f}")

        elif mode == "LN":
            power_of_e = float(input("Enter the power of e (Euler's number): "))
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
                new_e = np.pi
                print(f"e ** π = {new_e:.3f}")

        elif mode == "SIN":
            opp = float(input("Enter the opposite edge: "))
            hyp = float(input("Enter the hypotenuse: "))
            print(f"sin(θ) = {opp / hyp:.3f}")

        elif mode == "COS":
            adj = float(input("Enter the adjacent edge: "))
            hyp = float(input("Enter the hypotenuse: "))
            print(f"cos(θ) = {adj / hyp:.3f}")

        elif mode == "TAN":
            adj = float(input("Enter the adjacent edge: "))
            opp = float(input("Enter the opposite edge: "))
            print(f"tan(θ) = {opp / adj:.3f}")

        elif mode == "CSC":
            hyp = float(input("Enter the hypotenuse: "))
            opp = float(input("Enter the opposite edge: "))
            print(f"csc(θ) = {hyp / opp:.3f}")

        elif mode == "SEC":
            hyp = float(input("Enter the hypotenuse: "))
            adj = float(input("Enter the adjacent edge: "))
            print(f"sec(θ) = {hyp / adj:.3f}")

        elif mode == "COT":
            adj = float(input("Enter the adjacent edge: "))
            opp = float(input("Enter the opposite edge: "))
            print(f"cot(θ) = {adj / opp:.3f}")

        elif mode == "PT":
            print("| HYP = Finding the hypotenuse\n| EDGE = Finding an edge\n| i = Info")
            HYPorEdge = str(input("Select which edge to calculate: ")).upper()

            if HYPorEdge == "HYP":
                AnEdge = float(input("Enter the value of an edge: "))
                AnotherEdge = float(input("Enter the value of another edge: "))


                def HYPcal(a, b):
                    asq = a * a
                    bsq = b * b
                    c = asq + bsq
                    answer = np.sqrt(c)
                    print(f"The hypotenuse of {a} and {b} is {answer:.3f}")


                HYPcal(AnEdge, AnotherEdge)

            elif HYPorEdge == "EDGE":
                AnEdge = float(input("Enter the value of an edge: "))
                hyp = float(input("Enter the value of hypotenuse: "))
                if hyp < AnEdge:
                    print("An error has accured, the hypotenuse was smaller than the edge you provided.")
                elif not hyp < AnEdge:
                    def EDGEcal(b, a):
                        asq = a * a
                        bsq = b * b
                        c = bsq - asq
                        answer = np.sqrt(c)
                        print(f"The other edge of {b} (hypotenuse) and {a} is {answer:.3f}")


                    EDGEcal(hyp, AnEdge)
                else:
                    print("An error has accured.")

            elif HYPorEdge == "I":
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
                print("Please choose a mode")

        elif mode == "PA":
            force = float(input("Enter force (F): "))
            surface = float(input("Enter surface area (S): "))
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
                curr = float(input("Current (A): "))
                res = float(input("Resistance (Ω): "))
                print(Volt(curr, res))

            elif conv in ("CURRENT", "A"):
                volt = float(input("Voltage (V): "))
                res = float(input("Resistance (Ω): "))
                print(Current(volt, res))

            elif conv in ("RESISTANCE", "Ω"):
                volt = float(input("Voltage (V): "))
                curr = float(input("Current (A): "))
                print(Resistance(volt, curr))

        elif mode == "MS":
            print("| F = Fibonacci sequence\n| FS = Fibonacci series\n| P = Pell numbers")
            print("| PS = Pell series\n| B = Bronze sequence")
            print("| BS = Broze series\n| C = Copper sequence\n| CS = Copper series\ni = Info")
            seq = str(input("Enter a metallic sequence: ")).upper()

            if seq == "F":  # Why was this so hard?
                n = int(input("Enter a number: "))
                if n < 2:
                    print(f"F({n}) = {n}")
                elif not n == 0 or n == 1:
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
                n = int(input("Enter a number: "))
                if n < 2:
                    print(f"F({n}) = {n}")
                elif not n == 0 or n == 1:
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
                n = int(input("Enter a number: "))
                if n == 0 or n == 1:
                    print(f"P({n}) = {n}")
                elif not n == 0 or n == 1:
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
                n = int(input("Enter a number: "))
                if n == 0 or n == 1:
                    print(f"P({n}) = {n}")
                elif not n == 0 or n == 1:
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
                n = int(input("Enter a number: "))
                if n == 0 or n == 1:
                    print(f"B({n}) = {n}")
                elif not n == 0 or n == 1:
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
                n = int(input("Enter a number: "))
                if n == 0 or n == 1:
                    print(f"B({n}) = {n}")
                elif not n == 0 or n == 1:
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
                n = int(input("Enter a number: "))
                if n == 0 or n == 1:
                    print(f"C({n}) = {n}")
                elif not n == 0 or n == 1:
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
                n = int(input("Enter a number: "))
                if n == 0 or n == 1:
                    print(f"C({n}) = {n}")
                elif not n == 0 or n == 1:
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

            elif seq == "I":
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
                print("Please choose a mode")

        elif mode=="TEST":
            amount = input("Enter the required points to pass (ENTER for inf): ")
            if amount != "":
                Score = 0
                IsLast = False
                clear()
                while Score < int(amount):
                    questions = {
                        "What is the 6th element of the Fibbonacci sequence?": "8",
                        "(50 + 24) - 100 = ?": "-24",
                        "Which version of Python was used to make PY.calc?": "3.11.4",
                        "What is the average of this array: [150, 20, 30]": "100",
                        "What is the median of this array: [40, 20, 30, 60]": "25",
                        "(250 / 25) * 5 = ?": "50",
                        "The signum of -2145629124": "-1",
                        "Find the GCD of this array: [60, 45, 90, 105]": "15",
                        "(√16)! = ?": "24",
                        "abs(-56) = ?": "56",
                        "Round this number in decimal: 56.6": "57",
                        "Round this number: 124": "120",
                        "(√16 ** 2) ** 2 = ?": "256",
                        "Is 120 a perfect number? (T or F)": "F",
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
                        if int(amount) - 1 == Score:
                            IsLast = True
                        sleep(0.5)
                        Score += 1
                        if not IsLast:
                            close(0.3, 4, "Generating new question")
                        else:
                            break

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
                        "What is the average of this array: [150, 20, 30]": "100",
                        "What is the median of this array: [40, 20, 30, 60]": "25",
                        "(250 / 25) * 5 = ?": "50",
                        "The signum of -2145629124": "-1",
                        "Find the GCD of this array: [60, 45, 90, 105]": "15",
                        "Find the LCM of this array: [6, 15, 90, 57]": "1",
                        "Find the LCM of this array: [7, 56, 112, 8]": "122",
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




        elif mode == "M":
            lstk = [
                "+","Σ","-","--","*","*Σ","*T","**T","/","//%","DIV","PF","**","%","%2","ASC","DESC","P",
                "PR","COP","PR+","P!","SQRT","SQ","CBRT","CB","O","R","+++","~","RN","MODE","DEV","VAR",
                "!","||","CA","Cir","ARCLEN","LCM","GCD","S","LOG","LN","e**","SIN","COS","TAN","CSC","SEC",
                "COT","PT","MS","M","RNG","i","CLS","E"
            ]

            print(f"Modes:\n{lstk}")

        elif mode == "RNG":
            most = input("Enter the maximum value: ")
            most = most or 6

            least = input("Enter the minimum value: ")
            least = least or 1

            repeat = input("How many times should this be repeated?: ")
            repeat = repeat or 1

            for i in range(int(repeat)):
                print(rand(int(least), int(most)))


        elif mode == "I":
            if __name__ == "__main__":
                print(f"PY.calc")
                print(f"Currently {mode_count} modes avaible.")
                print(f"MADE WITH PYTHON 3.11.4 | Current Python version: {sys.version:.6}")
                print(f"MADE WITH NUMPY 2.3.2 | Current Numpy version: {np.__version__}")
                print(f"Being imported: No\nFile path: {__file__}")
            else:
                print(f"PY.calc")
                print(f"Currently {mode_count} modes avaible.")
                print(f"MADE WITH PYTHON 3.11.4 | Current Python version: {sys.version:.6}")
                print(f"MADE WITH NUMPY 2.3.2 | Current Numpy version: {np.__version__}")
                print(f"Being imported: Yes\nFile path: {__file__}")

        elif mode == "CLS":
            clear()
            intro()

        elif mode == "E":
            close(0.3, 4)
            condition = False

        else:
            print(f'"{mode.lower()}" is not a mode.')

except ValueError:
    print("An error has accured, please make sure you have typed a number.")
except ZeroDivisionError:
    print("An error has accured while dividing number with 0.")
except KeyboardInterrupt:
    close(0.3, 4)

sys.exit(0)