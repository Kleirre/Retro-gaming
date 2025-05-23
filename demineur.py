"""Ce programme est un jeu du démineur (partie 1/3).
Il consiste à proposer à l'utilisateur de trouver l'emplacement de mines placées aléatoirement dans une grille.
Ce programme a été écrit par Salomé Bergeron et Claire Oudot.
Rendu prévu le 15/03/2025.
Il est disponible sous la licence CC-by-nc-sa"""


import initialisation
import jeu


def affichage_grille(grille, perdu = False):
    """affiche la grille"""
    for ligne in grille:
        print(" ".join(
            "*" if case["mine"] and perdu
            else "△" if case["drapeau"]
            else str(case["adj"]) if case["revelee"]
            else "."
            for case in ligne
        ))
    print()


def regles_jeu():
    """affiche mes règles du jeu si demandé par l'utilisateur"""
    reponse = input("Voulez-vous un rapide rappel des règles de ce jeu légendaire ? Si c'est le cas tapez 'aide', sinon tapez n'importe quoi d'autre :")
    if reponse.lower() == 'aide' :
        print()
        print("""--------------------------------------------------------
Voici les règles du jeu du démineur :

Vous disposez d'une grille dans laquelle se cachent des mines (vous pouvez choisir le nombre de cases de cette grille et le nombre de mines qui doit être supérieur à 2 et inférieur à 30):
. . . . .
. . . . .
. . . . .
. . . . .
. . . . .

Votre but : les retrouver toutes sans exploser !
***
Vous pouvez exécuter deux actions : révéler une case (R) ou poser un drpeau pour signaler une mine (D). Dans les deux cas vous devrez entrer le numéro de colonne et de ligne de la case concernée (Attention : la première ligne correspond à 0).

- Révéler une case :  il s'agit de creuser, si vous creuser sur une mine vous avez perdu, sinon, le numéro sur la case indique le nombre de mines autour de cette case :
1 . . . .
. . . . .
. . . . .
. . . . .
. . . . .
Si il n'y a pas de mines autoure (et sur) cette case, les cases adjacentes sont révélées également:

- Poser un drapeau : Si vous pensez qu'une mine se cache à un endroit donné, vous pouvez le signaler par un drapeau (attention : si vous voulez creuser sur cette case, il faudra retirer le drapeau) :
1 △ . . .
. . . . .
. . . . .
. . . . .
. . . . .

La partie s'arrête lorsque vous creusez sur une mine(perdu) ou bien lorsque vous avez posé un drapeau sur toutes les mines et/ou avez révélé toutes les cases sans mines(gagné).

Symboles :
* = mine
△ = drapeau que vous avez posé
. = case non révélée
0, 1, 2 = nombre de mines autour de cette case
***
Bonne chance !
--------------------------------------------------------""")
        print()


def parametres_grille ():
    """permet à l'utilisateur de choisir les dimensions de la grille et le nombre de mines et initialise la grille"""
    nom = input("Quel est votre nom ? ")
    while True :
        try:
            taille = int(input("Commençons, "+ nom + " ! Entrez le nombre de cases que doit avoir votre grille de jeu par côté :"))
            if taille < 2 or taille > 30 :
                print("La grille ne peut pas faire moins de deux ou plus de 30 cases de long")
                continue
            break
        except ValueError :
            print("Veuillez entrer un nombre entier")

    while True :
        try:
            nombre_mines = int(input("Encore une dernière chose et vous pourrez commencer ! Combien de mines voulez vous ? "))
            if nombre_mines < 1 or nombre_mines >= taille * taille:
                print("Il doit y avoir au moins une mine et il ne peut pas en avoir plus que le nombre de cases de la grille.")
                continue
            break
        except ValueError :
            print("Veuillez entrer un nombre entier")
    print("C'est parti " + nom +" ! Bonne chance!")

    parametres = str(taille) + ' ' + str(nombre_mines)
    grille = initialisation.creer_grille(taille)
    grille = initialisation.mines(grille, nombre_mines)
    grille = initialisation.valeurs_grille(grille)

    return grille, nom, parametres

def message_fin (defaite, victoire):
    """adapte le message en fonction de la victoire de l'utilisateur et propose de rejouer"""
    print("Fin de la partie !")
    if defaite :
        print("Vous avez perdu ! Vous ferez mieux la prochaine fois ! ")
    if victoire :
        print("Bravoooooo ! Vous avez gagné !")

    fiche_score = input("Voulez vous consulter la fiche de score ? Si c'est le cas, tapez 'oui', sinon tapez n'importe quoi d'autre :")
    if fiche_score == 'oui':
        affiche_fiche_score()

def inscrit_score(prenom, coups, parametres, defaite):
    """inscrit dans le fichier les informations de la partie"""
    if defaite is True :
        ligne_a_inscrire = prenom + ' ' + str(coups) + ' ' + parametres + " perdu \n"
    else :
        ligne_a_inscrire = prenom + ' ' + str(coups) + ' ' + parametres + " gagné \n"
    with open("scores.txt", "a") as fichier:
        fichier.write(ligne_a_inscrire)

def affiche_fiche_score():
    """affiche l'entiereté du fichier de score"""
    try:
        with open("scores.txt", "r") as fichier:
            scores = fichier.readlines()
            if scores:
                print("Voici les scores, ils sont affichés sous la forme [nom du joueur, nombre de coups qu'il a utilisés, nombre de cases par côté dans sa grille, nombre de mines, statut(gagné ou perdu)]: ")
                for ligne in scores:
                    print(ligne.strip())
            else:
                print("Aucun score enregistré pour l'instant.")
    except FileNotFoundError:
        print("Aucun score enregistré pour l'instant.")
    print()


def main():
    """fonction de base, gère l'affichage du jeu"""
    print()
    print("***")
    print("Bonjour et bienvenue sur Démineur ! ")
    regles_jeu()

    grille, prenom, parametres = parametres_grille()

    coups = 0
    defaite = False
    victoire = False
    while not defaite and not victoire:
        affichage_grille(grille)
        grille, defaite = jeu.tentative(grille)
        if not defaite:
            victoire = jeu.verifier_victoire(grille)
        coups += 1
    inscrit_score(prenom, coups, parametres, defaite)
    affichage_grille(grille, perdu=True)
    message_fin(defaite, victoire)
    nouvelle_partie = input("Voulez-vous rejouer ? Si c'est le cas tapez 'oui', sinon tapez n'importe quoi d'autre :")
    if nouvelle_partie == 'oui' :
        main()

main()