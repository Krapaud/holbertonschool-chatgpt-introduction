#!/usr/bin/python3
import sys


def factorial(n):
    """Calcule la factorielle d'un nombre entier non négatif"""
    if n < 0:
        raise ValueError(
            "La factorielle n'est pas définie pour les nombres négatifs")

    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


def main():
    """Fonction principale avec gestion d'erreurs"""
    if len(sys.argv) != 2:
        print("Usage: python3 factorial.py <nombre_entier>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        result = factorial(n)
        print(result)
    except ValueError as e:
        if "invalid literal" in str(e):
            print("Erreur: Veuillez entrer un nombre entier valide")
        else:
            print(f"Erreur: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
