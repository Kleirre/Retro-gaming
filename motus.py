"""Ce programme est un jeu motus basé sur le jeu télévisé à succès.
Il consiste à proposer à l'utilisateur de retrouver un mot dont il ne connait
au début que la première lettre, au fur et à mesure qu'il propose des mots,
les lettres s'affichent si elles sont justes.
Ce programme a été écrit par Salomé Bergeron et Claire Oudot.
Rendu prévu le 23/11/2024."""

import random

def met_majuscule_premiere_lettre(mot, numero_entre):
    """affiche la première lettre du mot en majuscule"""
    nombre_tirets = (int(numero_entre)-1) * '-'
    premiere_lettre = (mot[0]).upper()
    affichage = premiere_lettre + nombre_tirets
    print(affichage)
    return affichage


def change_caracteres_speciaux(mot):
    """vérifie si le mot choisi aléatoirement par le dictionnnaire comporte des
    caractères avec accents ou cédilles et les change en lettres classiques"""
    mot = mot.replace('é', 'e')
    mot = mot.replace('è', 'e')
    mot = mot.replace('ê', 'e')
    mot = mot.replace('ë', 'e')

    mot = mot.replace('à', 'a')
    mot = mot.replace('â', 'a')

    mot = mot.replace('ù', 'u')
    mot = mot.replace('û', 'u')

    mot = mot.replace('î', 'i')
    mot = mot.replace('ï', 'i')

    mot = mot.replace('ö', 'o')
    mot = mot.replace('ô', 'o')

    mot = mot.replace('ç', 'c')
    return mot

def lecture_dico(nom_fichier, nombre_lettres):
    """renvoie un mot aléatoire du dictionnnaire"""
    with open(nom_fichier, 'r', encoding="UTF-8") as fichier :
        mots = fichier.readlines()
    nouvelle_liste = []
    for mot in mots :
        mot_nettoye = mot.strip()
        if len(mot_nettoye) == int(nombre_lettres):
            nouvelle_liste.append(mot_nettoye)

    mot_choisi = random.choices(nouvelle_liste)
    mot_choisi = ''.join(mot_choisi)
    mot_gagnant = change_caracteres_speciaux(mot_choisi)
    resultat = met_majuscule_premiere_lettre(mot_gagnant, nombre_lettres)
    return(mot_gagnant, resultat)


def test_mot(essai_en_cours, mot_gagnant):
    """vérifie si le mot proposé est le bon"""
    if mot_gagnant == essai_en_cours :
        return True
    return False


def test_lettre(essai_actuel, mot_gagnant, resultat, lettres_restantes):
    """teste si le mot entré par l'utilisateur et le mot à trouver on des
    lettres en commun"""
    essai_actuel = list(essai_actuel)
    mot_juste = list(mot_gagnant)
    resultat = list(resultat)
    resultat_final = ''
    index = 0
    lettres_restantes = list(lettres_restantes)

    for lettre in essai_actuel :
        if lettre == mot_juste[index]:
          #vérifie si la lettre est bien positionnée dans le mot
            resultat[index] = lettre.upper()
            if lettre in lettres_restantes :
                lettres_restantes.remove(lettre)
        index += 1

    for lettre in range (len(essai_actuel)) :
        if essai_actuel[lettre] != mot_juste[lettre] and essai_actuel[lettre] in mot_juste :
            if essai_actuel[lettre] in lettres_restantes :
                resultat[lettre] = (essai_actuel[lettre]).lower()

    for elt in resultat:
        resultat_final = resultat_final + str(elt)

    print(resultat_final)
    return (resultat_final, lettres_restantes)


def affiche_message_defaite(mot_choisit):
    """message si l'utilisateur est arrivé à la fin des tentatives"""
    message_d = input("""Désolé, vous avez épuisé toutes vos tentatives et """ +
    """n'avez pas trouvé le mot mystère. C'était : """ + str(mot_choisit) +
    """. Courage, vous y arriverez la prochaine fois ! Si vous voulez """ +
    """réessayer tapez 'oui', sinon, tapez n'importe quoi d'autre : """)
    if message_d  == 'oui':
        print(main())
    else :
        print("""Merci d'avoir joué !! À bientôt !""")


def affiche_message_victoire(nombre, mot_choisit):
    """message de victoire"""
    message = input("""Félicitations, vous avez gagné en """+ str(nombre) +
    """ tentative(s) ! Le mot gagnant était : """ +  str(mot_choisit)  +
    """. Gagnerez-vous en moins de tentatives ? Réessayez pour le savoir. """ +
    """Tapez 'oui' si vous voulez réessayer, sinon, tapez n'importe """ +
    """quoi d'autre : """)
    if message  == 'oui':
        print(main())
    else :
        print("""Merci d'avoir joué !! À bientôt !""")


def verification_essai(mot_juste):
    """demande un mot à l'utilisateur et vérifie si celui ci est de la bonne
    longueur et si il est bien composé uniquement de lettres"""
    essai = input('essayez un mot :')
    while not essai.isalpha() or len(essai) != len(mot_juste):
        essai = input(""" Il faut que vous entriez un mot qui doit avoir""" +
        """ le même nombre de lettres que celui que vous cherchez : """)
    return essai


def tentative(mot_gagnant, resultat, nombre_tentatives):
    """déroulé de chaque tentative"""
    lettres_restantes_a_trouver = mot_gagnant

    for numero_tentative in range(nombre_tentatives):
        essai = (verification_essai(mot_gagnant)).lower()
        if test_mot(essai, mot_gagnant) :
            affiche_message_victoire(numero_tentative, mot_gagnant)
            break
        sortie_test_lettre = test_lettre(essai, mot_gagnant, resultat,
        lettres_restantes_a_trouver)
        resultat = sortie_test_lettre[0]
        lettres_restantes_a_trouver = sortie_test_lettre[1]
    if (numero_tentative +1 ) == nombre_tentatives :
        affiche_message_defaite(mot_gagnant)



def choix_nombre_lettres():
    """l'utilisateur entre un nombre de lettres, vérification que l'entrée
    de l'utilisateur est bien valide"""
    nombre_lettres = input(""" ************
Pour commencer, choisissez le nombre de lettres du mot à deviner : """ )
    while not nombre_lettres.isdigit() or int(nombre_lettres) > 25 or int(nombre_lettres) <= 0:
        nombre_lettres = input("""Cette entrée n'est pas valide : Veuillez""" +
        """ entrer un nombre inférieur ou égal à 25 et supérieur à 0 : """)
    return nombre_lettres


def choix_tentatives():
    """l'utilisateur entre un nombre de tentatives, vérification que l'entrée
    de l'utilisateur est bien numérale"""
    nombre_tentatives = input(""" ************
Bien, encore une chose, et vous pourrez commencer à jouer ! """ +
"""Choisissez le nombre de tentatives maximum que vous voulez : """)
    while not nombre_tentatives.isdigit():
        nombre_tentatives = input("""Cette entrée n'est pas valide. """ +
        """Veuillez entrer un nombre : """)
    return nombre_tentatives

def affiche_regles_du_jeu():
    """affiche les règles du jeu si l'utilisateur le demande"""
    choix_utilisateur = input("""Si vous voulez un rappel des règles du jeu """
    + """tapez 'aide' sinon tapez n'importe quoi d'autre : """)
    if choix_utilisateur == 'aide':
        print("""______________________________________________________""" +
        """_________
        Voici les règles du motus :
        But : deviner le mot mystère.
        Vous allez choisir un nombre de lettres pour le mot que vous devrez """ +
        """deviner ainsi que le nombre de tentatives maximum que vous aurez """
        + """pour le deviner.
        Le mot sera affiché sous cette forme (exemple pour 5 lettres):
        " M---- "
        Ensuite il vous sera demandé de rentrer un mot. Il doit """ +
        """impérativement contenir le même nombre de lettres que le mot à """ +
        """deviner. Ici, si vous entrez 'musee', l'affichage en sortie sera """
        + """le suivant :
        " Mus-- " --> les lettres correctement placées sont affichées en """ +
        """majuscules, tandis que les lettres qui sont dans le mot mais pas""" +
        """ bien placées s'afficheront en minuscules.
        entrée = malus :
        " M--US "
        entrée = motus
        Vous avez gagné ! Le message de victoire s'affichera et vous pourrez """
        + """choisir de rejouer avec des paramètres différents.

        Attention : les mots ne contiennent pas de caracctères spéciaux """ +
        """(accents, cédilles) donc ne rentrez pas de mots qui en contiennent"""
        +""" (vous pouvez mais ce ne sera pas compté comme juste.

        Bon jeu !!
        _______________________________________________________________""")

def main():
    """main function : appelle les autres fonction si nécessaire,
    lance et arrête le jeu"""
    print("""
*
*
*
*
>>>>>>> Bonjour ! Et bienvenue sur Motus ! A l'image du grand jeu télévisé """ +
"""qui a fait ses débuts sur Antenne 2 en France, venez essayer de deviner """ +
"""le mot mysère. Alors... prêts ?

Pour jouer, il vous suffira de rentrer un mot. Et ensuite, les lettres """ +
"""s'afficheront en majuscule si elles sont bien placées et en minuscules """ +
"""si elles sont dans le mot mais sont mal placées. """)
    affiche_regles_du_jeu()
    nombre_lettres = choix_nombre_lettres()
    nombre_tentatives = choix_tentatives()
    resultats_lecture_dico = lecture_dico('dictionnaire_motus.txt', nombre_lettres)
    tentative(resultats_lecture_dico[0], resultats_lecture_dico[1], int(nombre_tentatives))
    return """***"""



print(main())