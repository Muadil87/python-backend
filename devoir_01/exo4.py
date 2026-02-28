a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))

print("1 : Addition")
print("2 : Soustraction")
print("3 : Multiplication")
print("4 : Division")

choix = input("Votre choix : ")

if choix == "1":
    print("Résultat :", a + b)
elif choix == "2":
    print("Résultat :", a - b)
elif choix == "3":
    print("Résultat :", a * b)
elif choix == "4":
    if b == 0:
        print("Erreur : division par zéro impossible.")
    else:
        print("Résultat :", a / b)
else:
    print("Choix invalide.")