from pathlib import Path


COMPTE = 0


class Réponse:
    def __init__(self):
        self.texte = ""
        self.code = 200
        self.headers = {}


def réponse_pour_route(route, verbe, headers):
    print(verbe, route)

    if verbe == "GET":
        return servir_fichier(route)
    else:
        return Réponse(texte=f"verbe inconnu: {verbe}", code=405)


def servir_fichier(route):
    réponse = Réponse()

    if route == "/":
        chemin = Path("index.html")
    else:
        chemin = Path(route[1:])

    if not chemin.exists():
        réponse.code = 404
        return réponse

    texte = chemin.read_text()

    réponse.texte = texte

    réponse.code = 200

    réponse.headers = {"Content-Type": "text/html; charset=utf-8"}

    return réponse
