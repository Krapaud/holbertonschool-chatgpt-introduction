#!/usr/bin/python3
import sys


def factorial(n):
    """
    Function description:
    Calcule la factorielle d'un nombre entier de manière récursive.
    La factorielle de n (notée n!) est le produit de tous les entiers positifs
    inférieurs ou égaux à n. Par définition, 0! = 1.

    Parameters:
    n (int): Le nombre entier non négatif dont on veut calculer la factorielle.
             Doit être >= 0.

    Returns:
    int: La factorielle de n. Retourne 1 si n = 0, sinon retourne n * (n-1)!
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


f = factorial(int(sys.argv[1]))
print(f)
