#!/usr/bin/python3
"""
Script pour calculer le factoriel d'un nombre entier positif.

Le factoriel de n (noté n!) est le produit de tous les entiers positifs
inférieurs ou égaux à n. Par exemple : 5! = 5 × 4 × 3 × 2 × 1 = 120

Usage: python3 factorial.py <number>
Exemple: python3 factorial.py 5

Auteur: Développeur
Date: Septembre 2025
"""
import sys

def factorial(n):
    """
    Calcule le factoriel d'un nombre entier positif.
    
    Args:
        n (int): Le nombre dont on veut calculer le factoriel (n >= 0)
        
    Returns:
        int: Le factoriel de n (n!)
        
    Note:
        Le factoriel de 0 est défini comme 1 par convention.
    """
    result = 1  # Initialise le résultat à 1
    while n > 1:  # Boucle tant que n est supérieur à 1
        result *= n  # Multiplie le résultat par la valeur actuelle de n
        n -= 1  # Décrémente n pour passer au nombre suivant
    return result  # Retourne le factoriel calculé

def main():
    """
    Fonction principale avec gestion d'erreurs pour les arguments de ligne de commande.
    
    Vérifie que l'utilisateur a fourni exactement un argument, que cet argument
    est un entier valide et non négatif, puis calcule et affiche son factoriel.
    """
    # Vérifie que l'utilisateur a fourni exactement un argument
    if len(sys.argv) != 2:
        print("Usage: python3 factorial.py <number>")
        print("Example: python3 factorial.py 5")
        sys.exit(1)  # Sort du programme avec un code d'erreur
    
    try:
        # Tente de convertir l'argument en entier
        n = int(sys.argv[1])
        
        # Vérifie que le nombre n'est pas négatif
        if n < 0:
            print("Error: Please enter a non-negative integer")
            sys.exit(1)
        
        # Calcule le factoriel et affiche le résultat
        result = factorial(n)
        print(f"Factorial of {n} is: {result}")
    
    except ValueError:
        # Gère le cas où l'argument n'est pas un entier valide
        print("Error: Please enter a valid integer")
        sys.exit(1)

if __name__ == "__main__":
    # Exécute la fonction main seulement si le script est lancé directement
    main()