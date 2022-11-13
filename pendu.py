import string
import os
from random import choice
from unidecode import unidecode


def listeCaract():
    return string.ascii_letters[0:26]


def motAleatoire(categorie):
    absolutePath = os.path.dirname(__file__)
    relativePath = f"resources/filesTXT/{categorie}.txt"
    fullPath = os.path.join(absolutePath,relativePath)
    print(fullPath)
    if os.path.exists(fullPath):
        with open(fullPath, "r") as dico:
            listeMots = dico.readlines()
            dico.close()
            return unidecode(choice(listeMots).lower())
    else:
        print("Fichier n'existe pas.")
