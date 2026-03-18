def traite_requête(message):
    """
    Recoit un message

    Renvoie une réponse
    """
    lignes = message.splitlines()

    première_ligne = lignes[0]
    mots = première_ligne.split()
    if len(mots) != 3:
        print("Première ligne invalide")
        return ""

    verbe, route, protocole = mots

    print(f"{verbe=}, {route=}, {protocole=}")

    headers = traite_entête_requête(lignes[1:])

    user_agent = headers.get("user-agent")
    if user_agent:
        print("Votre user agent est", user_agent)
        if "Linux" in user_agent:
            print("Et vous utilisez Linux :)")


def traite_entête_requête(lignes):
    headers = {}
    for ligne in lignes:
        if ":" not in ligne:
            continue
        clé, valeur = ligne.split(":", maxsplit=1)
        clé = clé.lower()
        headers[clé] = valeur.strip()

    return headers
