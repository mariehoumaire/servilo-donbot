from pathlib import Path


COMPTE = 0

EXTENSIONS_CONNUES = {
    ".html": "text/html; charset=UTF-8",
    ".txt": "text/plain; charset=UTF-8",
    ".css": "text/css",
}


class Réponse:
    def __init__(self):
        self.texte = ""
        self.code = 200
        self.headers = {}


def réponse_pour_route(route, verbe, headers):
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

    extension = chemin.suffix
    content_type = EXTENSIONS_CONNUES.get(extension)

    texte = chemin.read_text()

    réponse.texte = texte

    réponse.code = 200

    if content_type:
        réponse.headers["Content-Type"] = content_type

    return réponse
