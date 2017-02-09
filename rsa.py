#!/usr/bin/python
import random
import sys
from Crypto.Util.number import isPrime
from math import gcd as bltin_gcd

sys.setrecursionlimit(1000000)  # long type,32bit OS 4B,64bit OS 8B(1bit for sign)

def coprime2(a, b):
    return bltin_gcd(a, b) == 1

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def convert_to_ascii(text):
    return " ".join(str(ord(char)) for char in text)

############## find prime numbers P and Q ###############
p = 1
q = 5000
FirstPrime = [i for i in range(p, q) if isPrime(i)]
P = random.choice(FirstPrime)
SecondPrime = [i for i in range(p, q) if isPrime(i)]
Q = random.choice(SecondPrime)
while(P > Q):
    FirstPrime = [i for i in range(p, q) if isPrime(i)]
    P = random.choice(FirstPrime)
    SecondPrime = [i for i in range(p, q) if isPrime(i)]
    Q = random.choice(SecondPrime)
print("P: {} and Q: {}".format(P, Q))  # prints prime numbers P and Q

############## Calculate N  by mulitplying P and Q ############
N = P * Q
print("N: {}".format(N))

############# M = (P - 1)*(Q - 1) ###################
M = (P - 1) * (Q - 1)
print("M: {}".format(M))

############# Finding Exponent E ####################
PublicExponent = [i for i in range(P, Q) if (1 < i < M) if (coprime2(i, M))]
E = random.choice(PublicExponent)
#while (len(str(E)) < 5):
#    PublicExponent = [i for i in range(p, q) if (i > 0) if (0 < i < M) if (gcd(M, i))]
#    E = random.choice(PublicExponent)
print("E: {}".format(E))

############# Finding D #############################
D = modinv(E, M)
print("D: {}".format(D))

############# Printing public and private keys ######
print("Public  key: ({},{})" .format(E, N))
print("Private key: ({},{})" .format(D, N))

############# Message to encrypt and decrypt#########
#MSG = 123

MSG = input("Enter your Message: ")
#MSG = convert_to_ascii(msg)
print("Message: {}" .format(MSG))

############# Ecnrypting Message ####################
ENCRYPTED = (pow(int(MSG), E) % N)
print("Encrypted: {}" .format(str(ENCRYPTED)))

############# Decrypting Message ####################
DECRYPTED = (pow(int(ENCRYPTED), D) % N)
print("Decrypted: {}" .format(DECRYPTED))
