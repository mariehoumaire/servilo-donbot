import user_agents

PROTOCOLE = "HTTP/1.1"


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

    if protocole != PROTOCOLE:
        print("Protocole inconnu:", PROTOCOLE)
        return

    print(f"{verbe=}, {route=}, {protocole=}")

    headers = traite_entête_requête(lignes[1:])

    user_agent = headers.get("user-agent")
    if user_agent:
        print("Votre user agent est", user_agent)
        if "Linux" in user_agent:
            print("Et vous utilisez Linux :)")

        agent = user_agents.parse(user_agent)
        print(agent)

    return envoie_réponse(
        200,
        "0K",
        {"Content-Type": "text/plain", "Connection": "close"},
        "Bonjour, monde",
    )


def traite_entête_requête(lignes):
    headers = {}
    for ligne in lignes:
        if ":" not in ligne:
            continue
        clé, valeur = ligne.split(":", maxsplit=1)
        clé = clé.lower()
        headers[clé] = valeur.strip()

    return headers


def envoie_réponse(code, reason, headers, contenu):
    lignes = []
    première_ligne = f"{PROTOCOLE} {code} {reason}"
    lignes.append(première_ligne)

    for clé, valeur in headers.items():
        lignes.append(f"{clé}: {valeur}")

    taille = len(contenu)
    lignes.append(f"Content-Length: {taille}")

    en_tête = "\r\n".join(lignes)

    return en_tête + "\r\n\r\n" + contenu + "\r\n\r\n"
