import socket

def client():
    """ Fonction qui lance le client pour deviner la combinaison secrète. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))

    combinaison_secrete = client.recv(1024).decode()

    while True:
        proposition = input("Entrez une proposition (ou 'QUIT' pour quitter) : ").upper()
        client.send(proposition.encode())

        if proposition == "QUIT":
            print("Fin du jeu.")
            break

        reponse = client.recv(1024).decode()
        print(f"Réponse du serveur : {reponse}")

        if reponse == "Gagné !":
            print("Vous avez deviné la combinaison secrète ! Félicitations !")
            break

    client.close()