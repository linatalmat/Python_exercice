def convertir_note(texte):
    try:
        return float(texte.replace(",", "."))
    except ValueError:
        return None


def moyenne(valeurs):
    if len(valeurs) == 0:
        return 0

    return sum(valeurs) / len(valeurs)


def mention(note):
    if note < 10:
        return "Insuffisant"
    elif note < 12:
        return "Passable"
    elif note < 14:
        return "Assez bien"
    elif note < 16:
        return "Bien"
    else:
        return "Très bien"