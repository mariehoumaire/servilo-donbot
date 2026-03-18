import socket
from servilo import réponse_pour_route
from http import HTTPStatus

PORT = 5000
TAILLE_REQUÊTE = 1020
PROTOCOLE = "HTTP/1.1"


def traite_requête(message):
    """
    Recoit un message

    Renvoie une réponse
    """
    lignes = message.splitlines()

    première_ligne = lignes[0]
    verbe, route, _protocole = première_ligne.split()

    réponse = réponse_pour_route(route, verbe)

    status = HTTPStatus(réponse.code)

    taille = len(réponse.texte.encode()) + 4
    headers = réponse.headers

    headers["Content-Length"] = taille
    headers["Connection"] = "keep-alive"

    return envoie_réponse(
        status.value,
        status.phrase,
        headers,
        réponse.texte,
    )


def envoie_réponse(code, reason, headers, contenu):
    lignes = []
    première_ligne = f"{PROTOCOLE} {code} {reason}"
    lignes.append(première_ligne)

    for clé, valeur in headers.items():
        lignes.append(f"{clé}: {valeur}")

    en_tête = "\r\n".join(lignes)

    return en_tête + "\r\n\r\n" + contenu + "\r\n\r\n"


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
                réponse = traite_requête(requête)
                if réponse:
                    données = réponse.encode("UTF-8")
                    connection.sendall(données)


if __name__ == "__main__":
    main()
