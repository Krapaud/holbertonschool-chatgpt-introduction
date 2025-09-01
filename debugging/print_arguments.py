#!/usr/bin/python3
"""Script qui affiche tous les arguments passés en ligne de commande."""
import sys

# Vérifier s'il y a des arguments à afficher
if len(sys.argv) > 1:
    # Commencer à partir de l'index 1 pour exclure le nom du fichier
    for i in range(1, len(sys.argv)):
        print(sys.argv[i])
else:
    print("Aucun argument fourni.")
