from pathlib import Path


class Réponse:
    def __init__(self, texte="", code=200, headers=None):
        self.texte = texte
        self.code = code
        self.headers = headers or {}


def réponse_pour_route(route, verbe, headers, form):
    réponse = Réponse()

    chemin = Path("index.html")
    réponse.texte = chemin.read_text()
    réponse.headers["Content-Type"] = "text/html;charset=utf-8"

    return réponse
