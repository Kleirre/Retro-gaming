"""Ce programme est un jeu du démineur (partie 2/3).
Il consiste à proposer à l'utilisateur de trouver l'emplacement de mines placées aléatoirement dans une grille.
Ce programme a été écrit par Salomé Bergeron et Claire Oudot.
Rendu prévu le 15/03/2025.
Il est disponible sous la licence CC-by-nc-sa"""

import random

#################################### Grille

def creer_grille(taille) :
    """création de la grille du jeu au départ"""
    grille = [[{"mine": False, "adj": 0, "revelee": False, "drapeau": False} for i in range(taille)] for j in range(taille)]
    return grille



####################################### Mines

def mines (grille, nombre_mines):
    """place les mines dans la grille"""
    mines_places = 0

    while mines_places < nombre_mines:
        x = random.randint(0, len(grille) - 1)
        y = random.randint(0, len(grille) - 1)

        if not grille[x][y]["mine"]:
            grille[x][y]["mine"] = True
            mines_places += 1
    return grille

##################################### Cases non minées

def valeur_case(grille, x, y):
    """calcule le nombre de mines autour d'une case"""
    valeur = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for elt in directions:
        case_x, case_y = elt[0], elt[1]
        case_x, case_y = case_x + x, case_y + y

        if 0 <= case_x < len(grille) and 0 <= case_y < len(grille):
            if grille[case_x][case_y]["mine"]:
                valeur += 1
    return valeur


def valeurs_grille(grille):
    """Remplit la grille avec le nombre de mines autour de chaque case """
    for x in range(len(grille)):
        for y in range(len(grille)):
            if not grille[x][y]["mine"]:  # pas mine
                grille[x][y]["adj"] = valeur_case(grille, x, y)

    return grille
