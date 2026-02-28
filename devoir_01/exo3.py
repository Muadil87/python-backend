mot_passe="python123"
new_passe=input("saisir votre mot de passe :")
while mot_passe != new_passe :
    print("Mot de passe incorrect.")
    new_passe=input("saisir votre mot de passe :")

    print("Mot de passe correct. Accès autorisé.")