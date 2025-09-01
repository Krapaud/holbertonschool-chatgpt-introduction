#!/usr/bin/python3
import sys

# Correction: commencer à partir de l'index 1 pour exclure le nom du fichier Python
for i in range(1, len(sys.argv)):
    print(sys.argv[i])