"""Ce programme est un jeu du démineur (partie 3/3).
Il consiste à proposer à l'utilisateur de trouver l'emplacement de mines placées aléatoirement dans une grille.
Ce programme a été écrit par Salomé Bergeron et Claire Oudot.
Rendu prévu le 15/03/2025.
Il est disponible sous la licence CC-by-nc-sa"""


def verifier_victoire(grille):
    """Vérifie si toutes les cases sans mine sont révélées ou que toutes les mines sont marquées"""
    toutes_cases_revelees = True
    cases_mines_marquees = True
    for ligne in grille:
        for case in ligne:
            if not case["mine"] and not case["revelee"]:
                toutes_cases_revelees = False
            if case["mine"] and not case["drapeau"]:
                cases_mines_marquees = False

    return toutes_cases_revelees or cases_mines_marquees


def demander_action():
    """Demande au joueur une action (révéler ou poser un drapeau)."""
    while True:
        action = input("Tapez R si vous voulez révéler une case et D si vous voulez poser ou enlever un drapeau pour signaler une mine : ").upper()
        if action in ["R", "D"]:
            return action
        print("Cette entrée est invalide, réessayez.")

def demander_coordonnees(grille):
    """Demande au joueur des coordonnées valides."""
    while True:
        try:
            x = int(input("Entrez la colonne : "))
            y = int(input("Entrez la ligne : "))
            if 0 <= x < len(grille) and 0 <= y < len(grille):
                return x, y
            print("Coordonnées invalides. Essayez encore :")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def tentative(grille):
    """Permet au joueur de choisir une case."""
    action = demander_action()
    coord_x, coord_y = demander_coordonnees(grille)
    case = grille[coord_y][coord_x]

    if action == "D":
        if case["revelee"]:
            print("Désolé, vous ne pouvez pas mettre un drapeau sur une case révélée.")
        else:
            case["drapeau"] = not case["drapeau"]
        return grille, False

    if case["drapeau"]:
        print("Cette case est marquée d'un drapeau ! Retirez-le d'abord pour la révéler.")
        return grille, False

    grille, etat_partie = reveler_case(grille, coord_x, coord_y)
    return grille, etat_partie == "perdu"



def reveler_case(grille, x, y):
    """Révèle une case et celles d'à côté si besoin"""
    if grille[y][x]["revelee"]:
        print("Sélectionnez une case que vous n'avez pas encore révélé :")
        return grille, "pas perdu"

    grille[y][x]["revelee"] = True

    if grille[y][x]["mine"]:
        print("BOOM !")
        return grille, "perdu"

    if grille[y][x]["adj"] == 0 :
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dir_x, dir_y in directions:
            case_x, case_y = x + dir_x, y + dir_y
            if 0 <= case_x < len(grille) and 0 <= case_y < len(grille) and not grille[case_y][case_x]["revelee"] and not grille[case_y][case_x]["mine"]:
                reveler_case(grille, case_x, case_y)

    return grille, "pas perdu"
