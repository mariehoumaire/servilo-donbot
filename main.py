import socket
from servilo import traite_requête

PORT = 5000
TAILLE_REQUÊTE = 1020


def main():
    serveur = socket.create_server(("localhost", PORT))
    print("Servilo écoute sur le port", PORT)
    with serveur:
        connection, adresse = serveur.accept()
        print(f"Connection reçue: {adresse=}")
        with connection:
            while True:
                données = connection.recv(TAILLE_REQUÊTE)
                if not données:
                    return
                requête = données.decode("UTF-8", errors="replace")
                print("--- Requête: ---")
                print(requête)
                print("---")
                réponse = traite_requête(requête)
                if réponse:
                    données = réponse.encode("UTF-8")
                    connection.sendall(données)


if __name__ == "__main__":
    main()
