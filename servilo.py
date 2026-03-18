class Réponse:
    def __init__(self, texte="", code=200, headers=None):
        self.texte = texte
        self.code = code
        self.headers = headers or {}


def réponse_pour_route(route, verbe, headers, form):
    réponse = Réponse()

    réponse.texte = "Bonjour monde"

    return réponse
