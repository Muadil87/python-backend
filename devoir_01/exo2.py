carnet_adresses = []

while True:
    print("1. Ajouter un contact")
    print("2. Afficher les contacts")
    print("3. Quitter")

    choix = input("Votre choix : ")
    if choix == "1":
        contact = str(input("Entrez le nom du contact : "))
        carnet_adresses.append(contact)
        print("Contact ajouté.")
    elif choix == "2":
        if not carnet_adresses:
            print("Aucun contact.")
        else:
            for i, contact in enumerate(carnet_adresses, start=1):
                print(f"{i}. {contact}")
    elif choix == "3":
        print("Fin du programme.")
        break
    else:
        print("Choix invalide.")
