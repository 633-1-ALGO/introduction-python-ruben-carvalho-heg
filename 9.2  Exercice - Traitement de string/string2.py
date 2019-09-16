# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."
o_count = str.count(texte, "exemple", 0, len(texte))
print("Nombre d'occurences du mot 'exemple' :", o_count)
print("Chaine original : ", texte)
print("Chaine modifié : ", str.replace(texte, "est", "représente", len(texte)))
print("Chaine inversé : ", texte[::-1])

