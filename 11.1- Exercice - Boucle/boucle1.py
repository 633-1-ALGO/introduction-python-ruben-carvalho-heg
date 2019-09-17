# Problème : Etant donné un tableau A de "n" nombres réels, on demande la moyenne des nombres du tableau
# Données : un tableau A de n nombre réels
# Résultat attendu : Moyenne des nombres réels du tableau A
A = [1, 5, 15, 25, 10, 55, 50, 35]

i = 0
sum = 0

while i < len(A):
    sum += A[i]
    i += 1
moy = sum / len(A)
print(moy)
