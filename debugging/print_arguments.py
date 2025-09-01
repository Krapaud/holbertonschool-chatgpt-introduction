#!/usr/bin/python3
import sys

# Problème résolu : La boucle commence à l'index 1 au lieu de 0
# pour éviter d'afficher le nom du script (sys.argv[0])
# Seuls les arguments passés au script sont affichés
for i in range(1, len(sys.argv)):
    print(sys.argv[i])
