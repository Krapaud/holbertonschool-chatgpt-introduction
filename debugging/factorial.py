#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    # Problème résolu : La condition de la boucle est "n > 1" au lieu de "n >= 1"
    # Cela évite de multiplier par 1 inutilement et gère correctement
    # les cas où n = 0 ou n = 1 (tous deux égaux à 1 par définition)
    while n > 1:
        result *= n
        n -= 1
    return result

f = factorial(int(sys.argv[1]))
print(f)
