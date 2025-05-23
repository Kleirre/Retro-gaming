import random
import os

def charger_mots(fichier):
    """Charge les mots de 6 lettres depuis le fichier"""
    mots = []
    with open(fichier, 'r') as python:
        for ligne in python:
            mot = ligne.strip().upper()
            if len(mot) == 6:
                mots.append(mot)
    return mots

def extraire_syllabes(mot):
    """Extrait des syllabes d'un mot en divisant en groupes de 3 lettres"""
    return [mot[i:i+3] for i in range(0, len(mot), 3)]

def generer_mots_a_deviner(mots, nombre):
    """Sélectionne 24 mots"""
    random.shuffle(mots)
    return mots[:nombre]

def obtenir_syllabes_restantes(mots_a_deviner, mots_trouves):
    """Retourne la liste des syllabes des mots qui ne sont pas encore trouvés"""
    syllabes = set()
    for mot in mots_a_deviner:
        if mot not in mots_trouves:
            syllabes.update(extraire_syllabes(mot))
    return list(syllabes)

def sauvegarder_score(score, fichier="scores.txt"):
    """Sauvegarde le score du joueur sur un fichier"""
    nom = input("Entrez votre nom pour sauvegarder votre score : ")
    with open(fichier, 'a', encoding='ISO-8859-1') as python:
        python.write(f"{nom}: {score}\n")
    print("Score enregistré !")

def jouer(mots_a_deviner):
    """Lance le jeu et compte le score de la partie"""
    score = 0
    mots_trouves = set()
    print("Bienvenue dans le jeu des mots couplés de Raphaël et Maël! Tapez 'STOP' pour quitter.")

    while len(mots_trouves) < len(mots_a_deviner):
        print("\nSyllabes disponibles :", ', '.join(obtenir_syllabes_restantes(mots_a_deviner, mots_trouves)))
        mot = input("Entrez un mot de 6 lettres : ").upper()

        if mot == "STOP":
            print("Mots à deviner :", mots_a_deviner)
            break
        elif mot in mots_a_deviner and mot not in mots_trouves:
            mots_trouves.add(mot)
            score += 10
            print(f"Bravo ! Score: {score}")
        else:
            print("Mot invalide ou déjà trouvé.")

    print(f"Fin du jeu ! Score final: {score}")
    sauvegarder_score(score)

if __name__ == "__main__":
    fichier = "scrabble.txt"
    if not os.path.exists(fichier):
        print("Fichier de mots introuvable !")
    else:
        mots = charger_mots(fichier)
        mots_a_deviner = generer_mots_a_deviner(mots,24)
        jouer(mots_a_deviner)



