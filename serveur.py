import socket

def serveur():
    """ Fonction qui lance le serveur pour le jeu Mastermind. """
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveur.bind(('localhost', 12345))
    serveur.listen(1)
    print("Serveur en attente de connexion...")

    connexion, adresse = serveur.accept()
    print(f"Connexion établie avec {adresse}")

    taille = 5
    symboles = "0123456789"
    combinaison_secrete = generer_combinaison(taille, symboles)

    connexion.send("".join(combinaison_secrete).encode())

    while True:
        proposition = connexion.recv(1024).decode()
        if proposition == "QUIT":
            print("Déconnexion demandée par le client.")
            break

        print(f"Proposition reçue : {proposition}")
        bien_places, mal_places = analyser_proposition(combinaison_secrete, proposition)
        print(f"{bien_places} bien placé(s), {mal_places} mal placé(s)")

        if bien_places == taille:
            connexion.send("Gagné !".encode())
        else:
            connexion.send(f"{bien_places} bien(s) placé(s), {mal_places} mal(s) placé(s)".encode())

    connexion.close()
    serveur.close()