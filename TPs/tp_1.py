donnees = [
    ("Sara", "Math", 12, "G1"), ("Sara", "Info", 14, "G1"),
    ("Ahmed", "Math", 9, "G2"), ("Adam", "Chimie", 18, "G1"),
    ("Sara", "Math", 11, "G1"), ("Bouchra", "Info", "abc", "G2"),
    ("", "Math", 10, "G1"), ("Yassine", "Info", 22, "G2"),
    ("Ahmed", "Info", 13, "G2"), ("Adam", "Math", None, "G1"),
    ("Sara", "Chimie", 16, "G1"), ("Adam", "Info", 7, "G1"),
    ("Ahmed", "Math", 9, "G2"), ("Hana", "Physique", 15, "G3"),
    ("Hana", "Math", 8, "G3")
]
def valider(enregistrement):
    nom, matiere, note, groupe = enregistrement
    
    if not nom or not matiere or not groupe:
        return False, "raison: nom, matière ou groupe vide"
    
    if type(note) not in [int, float]:
        return False, "raison: note non numérique"
        
    if not (0 <= note <= 20):
        return False, "raison: note hors intervalle 0, 20"
        
    return True, ""


valides = []
erreurs = []
doublons_exact = set()

enregistrements_vus = set() 

for donne in donnees:
    if donne in enregistrements_vus:
        doublons_exact.add(donne)
        continue 
    
    enregistrements_vus.add(donne)
    
    est_valide, message = valider(donne)
    
    if est_valide:
        valides.append((donne[0], donne[1], float(donne[2]), donne[3]))
    else:
        erreurs.append({"ligne": donne, "raison": message})

print("Valides:", len(valides))
print("Erreurs:", len(erreurs))
print("Doublons:", len(doublons_exact))

#Partie 2 : Structuration
matieres_distinctes = set()

infos_etudiants = {}

groupes_pedagogiques = {}

for nom, matiere, note, groupe in valides:
    matieres_distinctes.add(matiere)
    
    if nom not in infos_etudiants:
        infos_etudiants[nom] = {}
    if matiere not in infos_etudiants[nom]:
        infos_etudiants[nom][matiere] = []
    infos_etudiants[nom][matiere].append(note)
    
    if groupe not in groupes_pedagogiques:
        groupes_pedagogiques[groupe] = set()
    groupes_pedagogiques[groupe].add(nom)
#Partie 3 : Calculs et statistiques
def somme_recursive(liste_notes):
    if not liste_notes: 
        return 0
    return liste_notes[0] + somme_recursive(liste_notes[1:])

def calculer_moyenne(liste_notes):
    if not liste_notes:
        return 0
    return somme_recursive(liste_notes) / len(liste_notes)

moyennes_etudiants = {}

for etudiant, matieres in infos_etudiants.items():
    toutes_les_notes = []
    moyennes_par_matiere = {}
    
    for matiere, notes in matieres.items():
        moyennes_par_matiere[matiere] = calculer_moyenne(notes)
        toutes_les_notes.extend(notes)
        
    moyenne_generale = calculer_moyenne(toutes_les_notes)
    
    moyennes_etudiants[etudiant] = {
        "moyennes_matieres": moyennes_par_matiere,
        "moyenne_generale": moyenne_generale
    }
#Partie 4 : Analyse avancée et détection d’anomalies
alertes = {
    "plusieurs_notes_meme_matiere": [],
    "profil_incomplet": [],            
    "groupe_faible": [],               
    "ecart_important": []              
}

SEUIL_GROUPE = 10.0
SEUIL_ECART = 5.0 

total_matieres = len(matieres_distinctes)

for etudiant, matieres in infos_etudiants.items():
    if len(matieres) < total_matieres:
        alertes["profil_incomplet"].append(etudiant)
        
    toutes_les_notes_etudiant = []
    
    for matiere, notes in matieres.items():
        toutes_les_notes_etudiant.extend(notes)
        if len(notes) > 1:
            alertes["plusieurs_notes_meme_matiere"].append((etudiant, matiere))
            
    if toutes_les_notes_etudiant:
        ecart = max(toutes_les_notes_etudiant) - min(toutes_les_notes_etudiant)
        if ecart >= SEUIL_ECART:
            alertes["ecart_important"].append((etudiant, ecart))

for groupe, etudiants_du_groupe in groupes_pedagogiques.items():
    notes_groupe = []
    for etudiant in etudiants_du_groupe:
        for notes_matiere in infos_etudiants.get(etudiant, {}).values():
            notes_groupe.extend(notes_matiere)
            
    moyenne_groupe = calculer_moyenne(notes_groupe)
    if moyenne_groupe < SEUIL_GROUPE:
         alertes["groupe_faible"].append((groupe, moyenne_groupe))