import sympy
import cryptography
import number_theory_algorithms
from decimal import Decimal
from decimal import getcontext

getcontext().prec = 100

def eiler_function_input():

    print("Enter a number to calculate the Euler's totient function:")
    user_input = input()
    try:
        number = Decimal(user_input)
        if number > 0:
            result = number_theory_algorithms.eiler_function(number)
            print(f"The Euler's totient function for {number} is {result}")
        else:
            print("Please enter an integer that is greater than 0.")

    except Exception as e:
        print("Invalid input. Please enter an integer that is greater than 0.")


def moebius_function_input():

    print("Enter a number to calculate the Möbius function:")
    user_input = input()
    try:
        number = Decimal(user_input)
        if number == int(number) and number > 0:
            result = number_theory_algorithms.moebius_function(number)
            if result == 0:
                print(f"The Möbius function for {number} is 0 (not square-free).")
            else:
                print(f"The Möbius function for {number} is {result}.")
        else:
            print("Please enter a positive integer (greater than or equal to 1).")

    except Exception as e:
        print("Invalid input. Please enter a positive integer (greater than or equal to 1).")


def smallest_common_multiple_input():

    print("Enter space-separated numbers to calculate their smallest common multiple:")
    user_input = input()
    try:
        numbers = [Decimal(x) for x in user_input.split()]

        if len(numbers) < 2:
            print("Please enter at least two integers.")
        else:
            result = number_theory_algorithms.smallest_common_multiple(numbers)
            print(f"The LCM is {result}.")

    except Exception as e:
        print("Invalid input. Please enter space-separated integers.")


def chinese_remainder_theorem_input():

    print("Enter the number of congruences:")
    try:
        num_congruences = int(input())
        c_numbers = []
        m_numbers = []

        for i in range(num_congruences):
            print(f"Enter a_{i}:")
            c = Decimal(input())
            print(f"Enter m_{i}:")
            m = Decimal(input())
            c_numbers.append(c)
            m_numbers.append(m)

        if len(c_numbers) < 2:
            print("Please enter at least two congruences.")
        else:
            result = number_theory_algorithms.chinese_remainder_theorem(c_numbers, m_numbers)
            if result is not None:
                print(f"The solution to the system of congruences is x ≡ {result}.")
            else:
                print("No solution found for the system of congruences.")

    except Exception as e:
        print("Invalid input. Please enter valid integers.")


def legendre_symbol_input():

    print("Enter an integer 'a' and a prime 'p' to calculate the Legendre symbol (a|p):")
    try:
        a = Decimal(input("Enter 'a': "))
        p = Decimal(input("Enter 'p' (a prime number more or equal than 3): "))

        if sympy.isprime(int(p)) and p >= 3:
            legendre_result = number_theory_algorithms.legendre(a, p)
            if legendre_result == 1:
                print(f"The Legendre symbol ({a}|{p}) is 1 (a is a quadratic residue modulo {p}).")
            elif legendre_result == -1:
                print(f"The Legendre symbol ({a}|{p}) is -1 (a is a non-quadratic residue modulo {p}).")
            elif legendre_result == 0:
                print(f"The Legendre symbol ({a}|{p}) is 0 (a is divisible by {p}).")
        else:
            print("Please enter a valid prime number 'p'.")

    except Exception as e:
        print("Invalid input. Please enter valid integers.")


def jacobi_symbol_input():

    print("Enter an integer 'a' and an odd positive integer 'n' to calculate the Jacobi symbol (a/n):")
    try:
        a = Decimal(input("Enter 'a': "))
        n = Decimal(input("Enter 'n' (an odd positive integer): "))

        if n % 2 == 0 or n <= 0:
            print("Please enter a valid odd positive integer 'n'.")
        else:
            jacobi_result = number_theory_algorithms.jacobi(a, n)
            if(jacobi_result == None):
                print("Invalid input, can`t calculate.")
                return
            print(f"The Jacobi symbol ({a}/{n}) is {jacobi_result}.")

    except Exception as e:
        print("Invalid input. Please enter a valid 'a' and 'n' as specified.")


def pollards_rho_factorisation_input():

    print("Enter a positive integer 'n' to perform Pollard's Rho factorization:")
    try:
        n = Decimal(input("Enter 'n': "))

        if n <= 1:
            print("Please enter a positive integer greater than 1.")
        else:
            result = number_theory_algorithms.pollards_rho_factorisation(n, 3)
            print(f"The factor of {n} is: {result}")

    except Exception as e:
        print("Invalid input. Please enter a valid positive integer.")


def baby_step_giant_step_input():

    print("Enter the base 'g', target 'b', and modulus 'p' to solve the discrete logarithm (g^x ≡ b mod p):")
    try:
        g = Decimal(input("Enter 'g' (base): "))
        b = Decimal(input("Enter 'b' (target): "))
        p = Decimal(input("Enter 'p' (modulus): "))

        if g <= 0 or b < 0 or p <= 0:
            print("Please enter valid positive integers for 'g', 'b', and 'p'.")
        elif not sympy.isprime(int(p)):
            print("p has to be prime.")
        else:
            x = number_theory_algorithms.baby_step_giant_step(g, b, p)
            if x == None:
                print("No solution found.")
            else:
                print(f"The solution to the discrete logarithm is x = {x}.")

    except Exception as e:
        print("Invalid input. Please enter valid positive integers.")


def chipolla_algorithm_input():

    print("Enter target 'g' and modulus 'p' to solve the discrete square root (x^2 ≡ g mod p):")
    try:
        b = Decimal(input("Enter 'g' (target): "))
        p = Decimal(input("Enter 'p' (modulus): "))

        if b < 0 or p <= 0:
            print("Please enter valid positive integers for 'g', and 'p'.")
        else:
            x = number_theory_algorithms.chipolla_algorithm(b, p)
            if x == None:
                print("No solution found.")
            else:
                print(f"The solution is x = {x}.")

    except Exception as e:
        print("Invalid input. Please enter valid positive integers.")


def miller_rabin_input():

    print("Enter a positive integer 'n' and iterations 'p' to perform the Miller-Rabin primality test:")
    try:
        n = Decimal(input("Enter 'n': "))
        p = Decimal(input("Enter 'p': "))

        if n < 2:
            print("Please enter a positive integer greater than 1.")

        elif(p < 1):
            print("Please enter correct number of iterations.")
        else:
            result = number_theory_algorithms.miller_rabin(n, p)
            if result == False:
                print(f"{n} is composite according to the Miller-Rabin test.")
            else:
                print(f"{n} is a prime number with a probability of {result[1]}.")

    except Exception as e:
        print("Invalid input. Please enter a valid positive integer.")

def rsa_cryptosystem_input():

    print("Enter the message that you want to encrypt using RSA crypto-system.")
    try:
        message = input()
        if len(message) == 0:
            print("Please enter valid message.")
        else:
            result = cryptography.encrypt_rsa(message)
            print("Your message before encryption: ")
            print(result[0])
            print("Your message after encryption: ")
            print(result[1])
            print("Your message after decryption: ")
            print(result[2])

    except Exception as e:
        print("Invalid input.")

def ecliptic_curves_input():

    print("Enter the message that you want to encrypt using ecliptic curve crypto-system.")
    try:
        message = input()
        if len(message) == 0:
            print("Please enter valid message.")
        else:
            result = cryptography.encrypt_ec(message)
            print("Your message before encryption: ")
            print(result[0])
            print("Your message after encryption: ")
            print(result[1])
            print("Your message after decryption: ")
            print(result[2])

    except Exception as e:
        print("Invalid input.")