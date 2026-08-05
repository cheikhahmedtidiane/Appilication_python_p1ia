# Partie 3 – Dictionnaires
#6) Créez  un dictionnaire pour stocker les métadonnées de chaque dataset 

# Gestion des exeptions
def safe_input(prompt, expected_type):
    while True:
        try:
            value = input(prompt)
            if expected_type == int:
                return int(value)
            elif expected_type == float:
                return float(value)
            elif expected_type == bool:
                return value.lower() in ['true', '1', 'yes']
            else:
                return value
        except ValueError:
            print(f"Erreur : Veuillez entrer un {expected_type.__name__} valide.")


datasets = {}
for i in range(3):  # Exemple pour 3 datasets
    nom_dataset = safe_input(f"\nEntrez le nom du dataset {i+1} : ", str)
    domain = safe_input("Entrez le domaine du dataset : Santé; Finance;Agriculture; Transport et Education : ", str)
    nb_lignes = safe_input("Entrez le nombre de lignes du dataset : ", int)
    nb_colonnes = safe_input("Entrez le nombre de colonnes du dataset : ", int)
    taille_mo = safe_input("Entrez la taille du dataset en Mo : ", float)
    public = safe_input("Le dataset est-il public ? (True/False) : ", bool)
    format_doc = ""
    while format_doc not in ["csv", "json"]:
        format_doc = safe_input("Choisissez le format du document (csv/json) : ", str).lower()

    # Stockage des métadonnées dans un dictionnaire
    datasets[nom_dataset] = {
        "domaine": domain,
        "nb_lignes": nb_lignes,
        "nb_colonnes": nb_colonnes,
        "taille_mo": taille_mo,
        "public": public,
        "format": format_doc
    }
    # Affichage du résumé pour chaque dataset
    print(f"\nRésumé du dataset '{nom_dataset}':")
    print(f"Domaine: {domain}")
    print(f"Nombre de lignes: {nb_lignes}")
    print(f"Nombre de colonnes: {nb_colonnes}")
    print(f"Taille: {taille_mo} Mo")
    print(f"Public: {public}")
    print(f"Format: {format_doc}")
    
# Partie 4 – Tuples 
# 7) Créez  un tuple contenant les domaines autorisés. 
    
domaines_autorises = ("Santé", "Finance", "Agriculture", "Transport", "Education")

# 8) Vérifiez  que le domaine saisi, à la question 3, appartient au tuple. 
if domain not in domaines_autorises:
    print("Erreur : Le domaine saisi n'est pas autorisé.")
else:
    print("Le domaine saisi est autorisé.")




# Partie 5 – Listes
# 9) Créez  une liste contenant les datasets. Chaque ajout est enregistré dans la liste

datasets_list = []
for nom, metadonnees in datasets.items():
    datasets_list.append((nom, metadonnees))

# 10) Ajoutez  les fonctionnalités : ajouter ,trier, rechercher, modifier et supprimer
# Ajouter un dataset
def ajouter_dataset():
    nom_dataset = safe_input("Entrez le nom du dataset : ", str)
    domain = safe_input("Entrez le domaine du dataset : Santé; Finance;Agriculture; Transport et Education : ", str)
    nb_lignes = safe_input("Entrez le nombre de lignes du dataset : ", int)
    nb_colonnes = safe_input("Entrez le nombre de colonnes du dataset : ", int)
    taille_mo = safe_input("Entrez la taille du dataset en Mo : ", float)
    public = safe_input("Le dataset est-il public ? (True/False) : ", bool)
    format_doc = ""
    while format_doc not in ["csv", "json"]:
        format_doc = safe_input("Choisissez le format du document (csv/json) : ", str).lower()

    datasets[nom_dataset] = {
        "domaine": domain,
        "nb_lignes": nb_lignes,
        "nb_colonnes": nb_colonnes,
        "taille_mo": taille_mo,
        "public": public,
        "format": format_doc
    }
    datasets_list.append((nom_dataset, datasets[nom_dataset]))
    print(f"\nDataset '{nom_dataset}' ajouté avec succès.")
    
    return nom_dataset, domain, nb_lignes, nb_colonnes, taille_mo, public, format_doc

# Trier les datasets par nom
def trier_datasets():
    datasets_list.sort(key=lambda x: x[0])
    print("\nDatasets triés par nom :")
    for nom, metadonnees in datasets_list:
        print(f"- {nom}")

# Rechercher un dataset par nom
def rechercher_dataset():
    nom_recherche = safe_input("Entrez le nom du dataset à rechercher : ", str)
    for nom, metadonnees in datasets_list:
        if nom == nom_recherche:
            print(f"\nDataset trouvé : {nom}")
            print(f"Domaine: {metadonnees['domaine']}")
            print(f"Nombre de lignes: {metadonnees['nb_lignes']}")
            print(f"Nombre de colonnes: {metadonnees['nb_colonnes']}")
            print(f"Taille: {metadonnees['taille_mo']} Mo")
            print(f"Public: {metadonnees['public']}")
            print(f"Format: {metadonnees['format']}")
            return
    print("Dataset non trouvé.")

# Modifier un dataset
def modifier_dataset():
    nom_modification = safe_input("Entrez le nom du dataset à modifier : ", str)
    for i, (nom, metadonnees) in enumerate(datasets_list):
        if nom == nom_modification:
            print(f"\nDataset trouvé : {nom}")
            print(f"Domaine: {metadonnees['domaine']}")
            print(f"Nombre de lignes: {metadonnees['nb_lignes']}")
            print(f"Nombre de colonnes: {metadonnees['nb_colonnes']}")
            print(f"Taille: {metadonnees['taille_mo']} Mo")
            print(f"Public: {metadonnees['public']}")
            print(f"Format: {metadonnees['format']}")

            # Demander les nouvelles valeurs
            domain = safe_input("Entrez le nouveau domaine du dataset : ", str)
            nb_lignes = safe_input("Entrez le nouveau nombre de lignes du dataset : ", int)
            nb_colonnes = safe_input("Entrez le nouveau nombre de colonnes du dataset : ", int)
            taille_mo = safe_input("Entrez la nouvelle taille du dataset en Mo : ", float)
            public = safe_input("Le dataset est-il toujours public ? (True/False) : ", bool)
            format_doc = ""
            while format_doc not in ["csv", "json"]:
                format_doc = safe_input("Choisissez le nouveau format du document (csv/json) : ", str).lower()

            # Mettre à jour les métadonnées
            datasets[nom] = {
                "domaine": domain,
                "nb_lignes": nb_lignes,
                "nb_colonnes": nb_colonnes,
                "taille_mo": taille_mo,
                "public": public,
                "format": format_doc
            }
            datasets_list[i] = (nom, datasets[nom])
            print(f"\nDataset '{nom}' modifié avec succès.")
            return
    print("Dataset non trouvé.")

# Supprimer un dataset
def supprimer_dataset():
    nom_suppression = safe_input("Entrez le nom du dataset à supprimer : ", str)
    for i, (nom, metadonnees) in enumerate(datasets_list):
        if nom == nom_suppression:
            del datasets[nom]
            del datasets_list[i]
            print(f"\nDataset '{nom}' supprimé avec succès.")
            return
    print("Dataset non trouvé.")


def recharger_donnees():
    global datasets, datasets_list
    datasets = {}
    datasets_list = []
    try:
        with open("datasets.csv", "r") as f:
            next(f)  # Ignorer l'en-tête
            for line in f:
                nom, domaine, nb_lignes, nb_colonnes, taille_mo, public, format_doc = line.strip().split(",")
                datasets[nom] = {
                    "domaine": domaine,
                    "nb_lignes": int(nb_lignes),
                    "nb_colonnes": int(nb_colonnes),
                    "taille_mo": float(taille_mo),
                    "public": public == 'True',
                    "format": format_doc
                }
                datasets_list.append((nom, datasets[nom]))
        print("\nDonnées rechargées depuis le fichier datasets.csv avec succès.")
    except FileNotFoundError:
        print("Erreur : Le fichier datasets.csv n'existe pas.")




# Partie 7 - Les Fichiers : 
# 12) Créez  le fichier datasets.csv pour : sauvergarder les métadonnées des datasets, recharger et afficher les données.
with open("datasets.csv", "w") as f:
    f.write("nom,domaine,nb_lignes,nb_colonnes,taille_mo,public,format\n")
    for nom, metadonnees in datasets.items():
        f.write(f"{nom},{metadonnees['domaine']},{metadonnees['nb_lignes']},{metadonnees['nb_colonnes']},{metadonnees['taille_mo']},{metadonnees['public']},{metadonnees['format']}\n")

# Recharger les données depuis le fichier CSV
datasets_recharge = {}
with open("datasets.csv", "r") as f:
    next(f)  # Ignorer l'en-tête
    for line in f:
        nom, domaine, nb_lignes, nb_colonnes, taille_mo, public, format_doc = line.strip().split(",")
        datasets_recharge[nom] = {
            "domaine": domaine,
            "nb_lignes": int(nb_lignes),
            "nb_colonnes": int(nb_colonnes),
            "taille_mo": float(taille_mo),
            "public": public == 'True',
            "format": format_doc
        }

# Afficher les données rechargées
print("\nDonnées rechargées depuis le fichier datasets.csv :")
for nom, metadonnees in datasets_recharge.items():
    print(f"- {nom}: {metadonnees}")

