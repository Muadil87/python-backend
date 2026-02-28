age = int(input("Entrez votre âge : "))

if age < 0:
    print("Age invalide.")
elif age <= 12:
    print("Enfant")
elif age <= 17:
    print("Adolescent")
elif age <= 64:
    print("Adulte")
else:
    print("Senior")