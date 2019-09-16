# Problème : Etant donné une variable a et b, on demande de mettre la valeur de a dans b et celle de b dans a
# Contraintes : Ne pas utiliser de valeurs numériques.
# Données : les variables a et b

a = 11
b = 42
a_temp = a

a = b
b = a_temp

print("Valeur de a :", a)
print("Valeur de b :", b)
