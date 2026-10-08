from outils import convertir_note, moyenne, mention


# Liste des notes données
notes_brutes = ["12,5", "15", "abc", "9", "18,25"]


# Liste pour stocker les notes valides
notes_valides = []

# Compteur pour les notes invalides
notes_invalides = 0


# Parcourir toutes les notes
for note in notes_brutes:

    # Convertir la note en nombre
    note_convertie = convertir_note(note)

    # Vérifier si la note est valide
    if note_convertie is not None:
        notes_valides.append(note_convertie)
    else:
        notes_invalides += 1


# Calculer la moyenne
moyenne_notes = moyenne(notes_valides)


# Trouver la mention
resultat_mention = mention(moyenne_notes)


# Afficher les résultats
print(f"Notes ignorées : {notes_invalides}")
print(f"Moyenne : {moyenne_notes:.2f}")
print(f"Mention : {resultat_mention}")