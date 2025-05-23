"""Le jeu du Mastermind"""

import random
import itertools
import time
import matplotlib.pyplot as plt

### Fonctions
def generer_combinaison(taille=5, symboles="0123456789"):
    """ Génère une combinaison secrète aléatoire. """
    return random.choices(symboles, k=taille)

def analyser_proposition(combinaison_secrete, proposition):
    """ Analyse la proposition et retourne le nombre de chiffres bien et mal placés. """
    bien_places = sum(1 for i in range(len(proposition)) if proposition[i] == combinaison_secrete[i])

    copie_secrete = list(combinaison_secrete)
    copie_proposition = list(proposition)

    for i in range(len(proposition)):
        if copie_proposition[i] == copie_secrete[i]:
            copie_secrete[i] = copie_proposition[i] = None  # Supprime les bien placés pour éviter les doublons

    mal_places = 0
    for i in range(len(proposition)):
        if copie_proposition[i] and copie_proposition[i] in copie_secrete:
            mal_places += 1
            copie_secrete[copie_secrete.index(copie_proposition[i])] = None

    return bien_places, mal_places

##Paramétrage
def demander_parametres():
    """ Demande à l'utilisateur les paramètres du jeu. """
    print("\nConfiguration du jeu Mastermind :")

    while True:
        try:
            taille = int(input("Longueur de la combinaison (ex: 5) : "))
            if taille > 0:
                break
            print("⚠️ La longueur doit être un nombre positif.")
        except ValueError:
            print("⚠️ Entrée invalide. Veuillez entrer un nombre valide.")

    while True:
        symboles = input("Caractères autorisés (ex: 0123456789 ou ABCDEF) : ").upper()
        if len(symboles) >= 2:
            break
        print("⚠️ Il doit y avoir au moins deux symboles.")

    while True:
        try:
            tentatives_max = int(input("Nombre maximum de tentatives : "))
            if tentatives_max > 0:
                break
            print("⚠️ Doit être un nombre positif.")
        except ValueError:
            print("⚠️ Entrée invalide.")

    return taille, symboles, tentatives_max

###Bots
def bot_naif(taille, symboles, tentatives_max, combinaison_secrete):
    """ Stratégie aléatoire pour deviner la combinaison. """
    essais = 0
    possibilites = [list(p) for p in itertools.product(symboles, repeat=taille)]
    random.shuffle(possibilites)

    for i in range(tentatives_max):
        if not possibilites:
            break
        essais = i+1
        proposition = possibilites.pop()
        bien_places, mal_places = analyser_proposition(combinaison_secrete, proposition)
        print(f"Essai {essais}: {''.join(proposition)} -> {bien_places} bien placés, {mal_places} mal placés")

        if bien_places == taille:
            print(f"\nLe bot naïf a trouvé la combinaison en {essais} essais !")
            return essais
        time.sleep(1)

    print(f"\nÉchec. La solution était {''.join(combinaison_secrete)}")
    return essais

def bot_knuth(taille, symboles, tentatives_max, combinaison_secrete):
    """ Stratégie de Knuth pour deviner la combinaison. """
    essais = 0
    possibilites = [list(p) for p in itertools.product(symboles, repeat=taille)]

    if taille == 4 and len(symboles) >= 6:
        proposition = list("1122")
    else:
        proposition = possibilites[0]

    while essais < tentatives_max:
        essais += 1
        bien_places, mal_places = analyser_proposition(combinaison_secrete, proposition)

        print(f"Essai {essais}: {''.join(proposition)} -> {bien_places} bien placés, {mal_places} mal placés")

        if bien_places == taille:
            print(f"\nLe bot Knuth a trouvé la combinaison en {essais} essais !")
            return essais

        possibilites = [
            p for p in possibilites
            if analyser_proposition(proposition, p) == (bien_places, mal_places)
        ]

        if not possibilites:
            break

        scores = {}
        for candidat in possibilites:

            score = sum(
                1 for p in possibilites if analyser_proposition(candidat, p) != analyser_proposition(proposition, p)
            )
            scores[tuple(candidat)] = score

        proposition = list(min(scores, key=scores.get))

        time.sleep(1)

    print(f"\nÉchec. La solution était {''.join(combinaison_secrete)}")
    return essais

### Mode de Jeu
def mastermind_m2m():
    """ Mode où un bot essaie de deviner la combinaison. """
    print("\nSimulation M2M (Machine-to-Machine)")

    taille, symboles, tentatives_max = demander_parametres()
    combinaison_secrete = generer_combinaison(taille, symboles)

    while True:
        choix_bot = input("\nChoisissez un bot :\n1. Bot naïf\n2. Bot Knuth (bot intelligent)\nVotre choix : ").strip()
        if choix_bot in ("1", "2"):
            break
        print("⚠️ Choix invalide.")

    if choix_bot == "1":
        essais = bot_naif(taille, symboles, tentatives_max, combinaison_secrete)
    else:
        essais = bot_knuth(taille, symboles, tentatives_max, combinaison_secrete)

    print(f"\nLe bot a terminé en {essais} essais.")

def main():
    """Fonction principale du jeu Mastermind."""
    print("Bienvenue dans le jeu du Mastermind !\n")

    while True:
        while True:
            choix = input("\n1. Jouer contre un bot\n2. Mode Machine-to-Machine (M2M)\nVotre choix : ").strip()
            if choix in ("1", "2", "3"):
                break
            print("⚠️ Entrée invalide ! Tapez '1' pour jouer contre un bot ou '2' pour le mode M2M")

        if choix == "1":
            taille, symboles, tentatives_max = demander_parametres()
            combinaison_secrete = generer_combinaison(taille, symboles)
            print("\nLa combinaison secrète a été générée. Essayez de la deviner !")

            for tentative in range(1, tentatives_max + 1):
                while True:
                    proposition = input(f"\nTentative {tentative}/{tentatives_max} - Entrez {taille} caractères : ").upper()
                    if proposition == "QUITTER":
                        print("Vous avez choisi de quitter la partie. À bientôt !")
                        return

                    if len(proposition) == taille and all(c in symboles for c in proposition):
                        break
                    print("⚠️ Entrée invalide ! Respectez la longueur et les symboles autorisés.")

                bien_places, mal_places = analyser_proposition(combinaison_secrete, proposition)
                print(f"{bien_places} bien placé(s), {mal_places} mal placé(s)")

                if bien_places == taille:
                    print("\nFélicitations ! Vous avez gagné !")
                    break

            if bien_places != taille:
                print(f"\nFin du jeu ! La combinaison secrète était {''.join(combinaison_secrete)}.")

        elif choix == "2":
            mastermind_m2m()

        rejouer = input("\nVoulez-vous rejouer ? (oui/non (tapez autre chose que oui)) : ").strip().lower()
        if rejouer != "oui":
            print("Merci d'avoir joué !")
            break

## Graphique
def simuler_essais(max_taille=5, max_symboles=10, tentatives_max=100):
    """Simule des essais pour le tracé du graphique"""
    tailles = range(1, max_taille + 1)
    essais_par_taille_naif = []
    essais_par_taille_knuth = []

    for taille in tailles:
        essais_naif = []
        essais_knuth = []

        for symboles_count in range(2, max_symboles + 1):
            symboles = "0123456789"[:symboles_count]
            combinaison_secrete = generer_combinaison(taille, symboles)

            essais_naif.append(bot_naif(taille, symboles, tentatives_max, combinaison_secrete))
            essais_knuth.append(bot_knuth(taille, symboles, tentatives_max, combinaison_secrete))

        essais_par_taille_naif.append(essais_naif)
        essais_par_taille_knuth.append(essais_knuth)

    return tailles, essais_par_taille_naif, essais_par_taille_knuth

def tracer_graphique_simple():
    """Trace un graphique comparant les bots naïf et Knuth."""
    tailles = [1, 2, 3, 4, 5]
    essais_naif = [10, 12, 14, 16, 18]
    essais_knuth = [6, 8, 10, 12, 14]

    plt.figure(figsize=(10, 6))
    plt.plot(tailles, essais_naif, label="Bot Naïf", color="blue")
    plt.plot(tailles, essais_knuth, label="Bot Knuth", color="red", linestyle="--")
    plt.xlabel("Taille de la combinaison")
    plt.ylabel("Nombre d'essais")
    plt.title("Comparaison entre Bot Naïf et Bot Knuth")
    plt.legend()
    plt.grid(True)
    plt.show()

tracer_graphique_simple()

###Lancement du jeu
if __name__ == "__main__":
    main()