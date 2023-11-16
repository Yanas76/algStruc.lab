import math
import sympy
import random
from decimal import Decimal
from decimal import getcontext

getcontext().prec = 1000

def max_number(numbers):

    index = 0
    max_numb = numbers[index]

    for i in range(1, len(numbers)):
        if (numbers[i] > max_numb): max_numb = numbers[i]

    return max_numb


def greatest_common_divisor(number_1, number_2):

    while (number_2 != 0):
        number_1, number_2 = number_2, number_1 % number_2
    return number_1


def smallest_common_multiple(numbers):

    max_numb = max_number(numbers)
    multiplier = 1
    break_flag = False

    while True:

        if(break_flag): break
        result = max_numb * multiplier
        break_flag = True

        for i in range(len(numbers)):

            if(max_numb == numbers[i]): continue
            temp = result % numbers[i]
            if(temp == 0): continue
            break_flag = False

        multiplier += 1

    return result


def eiler_function(number):

    result = Decimal(1)
    i = Decimal(2)
    if(number == 1): return result

    while True:

        if(i == number): break
        if greatest_common_divisor(i, number) == 1:
            result += 1
        i += 1

    return result


def moebius_function(number):

    if (number == 1): return 1
    check_before = Decimal(int(math.sqrt(number)) + 1)
    simp_divider = 2
    multipliers = Decimal(1)

    while True:

        if(max_number([check_before, simp_divider]) == simp_divider): break
        n = simp_divider * simp_divider
        if(number % n == 0): return 0

        simp_divider += 1
        while not (sympy.isprime(simp_divider)):
            simp_divider += 1

    simp_divider = 2

    while True:

        if(max_number([number, simp_divider]) == simp_divider): break
        if(number % simp_divider == 0 and max_number([number, simp_divider]) == number):
            multipliers += 1
            number = number/simp_divider
            continue

        simp_divider += 1
        while not (sympy.isprime(simp_divider)):
            simp_divider += 1

    return pow(-1, multipliers)


def pollards_rho_factorisation(number, c):

    def polynimial(number, x, c):
        return (pow(x, 2) + c) % number

    if (number == 1):
        return number
    if(number % 2 == 0):
        return 2

    x = Decimal(2)
    y = Decimal(2)

    while True:

        x = polynimial(number, x, c)
        y = polynimial(number, y, c)
        y = polynimial(number, y, c)
        difference = y - x

        if(greatest_common_divisor(difference, number) > 1):
            if(difference == number): return pollards_rho_factorisation(number, c + 1)
            return (greatest_common_divisor(difference, number))


def baby_step_giant_step(g, b, p):

    #g^x = b mod p
    m = round(math.sqrt(p))

    aj_values = []
    i = 0

    while i < m:
        aj_values.append(pow(g, i, p))
        i += 1

    a = pow(g, m * (p - 2), p)

    i = 0
    while i < m:

        ba_mi = b * pow(a, i, p) % p
        j = 0
        while j < m:
            if (ba_mi == aj_values[j]): return i * m + j
            j += 1

        i += 1

    return None


def legendre(a, p):

    if p < 3 or not sympy.isprime(int(p)):
        return None

    if a % p == 0: return 0

    if pow(a, (p - 1) // 2, p) == 1:
        result = 1
    else:
        result = -1

    return result


def jacobi(a, m):

    symbol = 1
    pjlist = []
    if(m % 2 == 0):
        return None

    i = math.floor(m / 2) + 1
    while i > 1:

        poww = 0
        new_numb = m

        if not (sympy.isprime(i) or new_numb % i == 0):
            i -= 1
            continue

        while new_numb >= i and new_numb % i == 0:
            new_numb = new_numb / i
            poww += 1

        if poww % 2 == 0:
            m = m / pow(i, poww)
        else:
            pjlist.append(i)

        i -= 1

    if len(pjlist) == 0:
        symbol = legendre(a, m)
    else:
        for i in range(len(pjlist)):
            if (legendre(a, pjlist[i]) == None): return None
            symbol *= legendre(a, pjlist[i])

    return symbol


def chipolla_algorithm(b, p):

    def field_multiplication(a, b, w):
        result = [0, 0]
        result[0] = (a[0] * b[0] + w * a[1] * b[1]) % p
        result[1] = (a[0] * b[1] + b[0] * a[1]) % p
        return result

    if legendre(b, p) != 1:
        return None

    a = 1
    while True:
        w_sq = (a * a - b) % p
        if legendre(w_sq, p) != 1:
            break
        a += 1

    exp = (p + 1) // 2

    if (exp % 2 == 0):
        res = [1, 0]
    else:
        exp -= 1
        res = [a, 1]

    a_sq = field_multiplication([a, 1], [a, 1], w_sq)

    i = 0
    while i < exp // 2:
        res = field_multiplication(res, a_sq, w_sq)
        i += 1

    return res[0]


def miller_rabin(a, iterations):

    if(greatest_common_divisor(a, 6) > 1):
        return False

    if a % 2 == 0:
        return False

    if a == 3 or a == 2:
        return True

    n = 0
    q = a - 1

    while True:
        if(q % 2 == 1): break
        n += 1
        q //= 2

    i = 0
    while i < iterations:

        x = random.randint(2, a - 2)
        b = pow(x, q, a)
        if b == 1 or b == a - 1:
            i += 1
            continue

        j = 0
        while j < n:
            b = pow(b, 2, a)
            if b == a - 1:
                break
            j += 1

        if(j == n):
            return False
        i += 1

    return True, 1 - 4**(1 - iterations)

def chinese_remainder_theorem(c_numbers, m_numbers):

    def y(m, n):
        i = 1
        while i < n:
            if ((m * i - 1) % n == 0): return i
            i += 1
        return 0

    if(len(c_numbers) != len(m_numbers)):
        print("Can`t solve, wrong input!")
        return None

    for i in range(len(m_numbers)):
        for j  in range(i, len(m_numbers)):
            if(i == j): continue
            if(greatest_common_divisor(m_numbers[i], m_numbers[j]) != 1):
                print("Can`t solve, please give prime numbers!")
                return None

    m = 1
    for i in range(len(m_numbers)):
        m *= m_numbers[i]

    x0 = 0
    for i in range(len(m_numbers)):
        x0 += c_numbers[i] * m/m_numbers[i] * y(m/m_numbers[i], m_numbers[i])

    return x0 % m