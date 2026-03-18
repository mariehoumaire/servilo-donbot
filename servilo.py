COMPTE = 0


class Réponse:
    def __init__(self):
        self.texte = ""
        self.code = 200
        self.headers = {}


def réponse_pour_route(route, verbe):
    print(verbe, route)
    réponse = Réponse()

    texte = "Bonjour !"
    global COMPTE
    COMPTE += 1
    texte += f"\nVous avez rafraîchi cette page {COMPTE} fois 😇"

    réponse.texte = texte

    réponse.code = 200

    réponse.headers = {"Content-Type": "text/plain; charset=utf-8"}

    return réponse
