import number_theory_algorithms
from decimal import Decimal
import sympy
import random
from decimal import getcontext
getcontext().prec = 100

def mod_div(k, p):

    if k == 0:
        return None

    if k < 0:
        return p - mod_div(-k, p)

    a1, a2 = 0, 1
    b1, b2 = p, k

    while b1 != 0:

        q = b2 // b1
        b2, b1 = b1, b2 - q * b1
        a2, a1 = a1, a2 - q * a1

    return a2 % p


def field_add(p1, p2, a, p):

    if p1 == None:
        return p2
    if p2 == None:
        return p1

    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]

    if(x1 == x2 and y1 == 0 - y2):
        return None

    if (x1 == x2 and y1 == y2):
        if(mod_div(2 * y1, p) == None): return None
        l = (3 * x1 * x1 + a) * mod_div(2 * y1, p)
        x3 = (l * l - 2 * x1)

    else:
        if (mod_div(x2 - x1, p) == None): return None
        l = (y2 - y1) * mod_div(x2 - x1, p)
        x3 = (l * l - x1 - x2)

    result = [x3 % p, (l * (x1 - x3) - y1) % p]
    return result


def ecliptic_curves(message):

    #y^2 = x^3 + ax + b
    """
    p = 4451685225093714772084598273548427
    order = 4451685225093714776491891542548933  # DB7C2ABF62E35E7628DFAC6561C5
    a = 4451685225093714772084598273548424
    b = 2061118396808653202902996166388514
    x = 188281465057972534892223778713752  # 09487239995A5EE76B55F9C2F098
    y = 3419875491033170827167861896082688  # A89CE5AF8724C0A23E0E0FF77500
    """

    order = 40
    a = 2
    b = 34
    p = 1439
    x = 5  # 09487239995A5EE76B55F9C2F098
    y = 13  # A89CE5F8724C0A23E0E0FF77500

    k = random.randint(1, order - 1)
    p_point = [x, y]
    y_point = p_point

    for i in range(k - 1):
        y_point = field_add(y_point, p_point, a, p)

    y1 = -1
    x1 = message % p

    while True:
        for i in range(p):
            if i**2 % p == (x1**3 + a*x1 + b) % p:
                y1 = i
            continue
        if(y1 != -1): break
        x1 *= 2
        x1 %= p

    m_point = [x1, y1]
    r = random.randint(1, order - 1)

    d = y_point
    for i in range(r - 1):
        d = field_add(d, y_point, a, p)

    g = p_point
    for i in range(r - 1):
        g = field_add(g, p_point, a, p)

    h = field_add(m_point, d, a, p)

    s = g
    for i in range(k - 1):
        s = field_add(g, s, a, p)

    s1 = [s[0], -s[1]]
    decrypt = field_add(h, s1, a, p)

    return m_point, decrypt


def encrypt_rsa(message):

    encr = []
    decr = []
    before_enc = []
    for i in range(len(message)):
        before_enc.append(ord(message[i]))
        result = rsa(ord(message[i]))
        encr.append(result[0])
        decr.append(result[1])

    return before_enc, encr, decr


def encrypt_ec(message):

    encr = []
    decr = []
    before_enc = []
    for i in range(len(message)):
        before_enc.append(ord(message[i]))
        result = ecliptic_curves(ord(message[i]))
        encr.append(result[0])
        decr.append(result[1])

    return before_enc, encr, decr


def rsa(number):

    def generate_prime():
        while True:
            x = random.randint(300, 800)
            if sympy.isprime(x): return x

    p = generate_prime()
    q = generate_prime()

    n = p * q
    f = (p - 1) * (q - 1)

    while True:
        e = random.randint(2, f - 1)
        if(number_theory_algorithms.greatest_common_divisor(e, f) == 1): break

    while True:
        d = random.randint(2, f - 1)
        if(d * e % f == 1): break

    encr = pow(number, e, n)
    decr = pow(encr, d, n)

    return encr, decr

