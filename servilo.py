COMPTE = 0


class Réponse:
    def __init__(self):
        self.texte = ""
        self.code = 200
        self.headers = {}


def réponse_pour_route(route, verbe, headers):
    print(verbe, route)
    réponse = Réponse()

    global COMPTE
    COMPTE += 1
    texte = f"""<!DOCTYPE html>
<html>
<head>
    <title>Servilo :) </title>
</head>

<body>
<h2>Bonjour monde!</h2>

Vous avez rafraîchi cette page <code>{COMPTE}</code> fois

</body>
</html>
    """

    réponse.texte = texte

    réponse.code = 200

    réponse.headers = {"Content-Type": "text/html; charset=utf-8"}

    return réponse
