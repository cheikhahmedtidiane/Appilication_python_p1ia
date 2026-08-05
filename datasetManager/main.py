# # Application python permettant de gerer des jeux de données.

# # Partie 1 : Types de base, variables, Entrées et sorties 
# #   3) Demandez à l’utilisateur de saisir les métadonnées d’un dataset :


# nom_dataset = input("Entrez le nom du dataset : ")
# domain = input("Entrez le domaine du dataset : Santé; Finance;Agriculture; Transport et Education : ")
# nb_lignes = int(input("Entrez le nombre de lignes du dataset : "))
# nb_colonnes = int(input("Entrez le nombre de colonnes du dataset : "))
# taille_mo = float(input("Entrez la taille du dataset en Mo : "))
# public = bool(input("Le dataset est-il public ? (True/False) : "))
# format_doc = ""
# while format_doc not in ["csv", "json"]:
#     format_doc = input("Choisissez le format du document (csv/json) : ").lower()

# # 4) Affichez ensuite un résumé formaté. 

# print(f"\nRésumé du dataset '{nom_dataset}':")
# print(f"Domaine: {domain}")
# print(f"Nombre de lignes: {nb_lignes}")
# print(f"Nombre de colonnes: {nb_colonnes}")
# print(f"Taille: {taille_mo} Mo")
# print(f"Public: {public}")
# print(f"Format: {format_doc}")

# Partie 2 : Structures de contrôle 
# 5) Créez un menu interactif (provisoire)

choix = "" # Initialisation pour entrer dans la boucle

while choix != "4": # Le programme reste actif TANT QUE choix n'est pas "4"
    print("\n----------------- MENU -----------------")
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher")
    print("4. Quitter")
    
    choix = input("Choisissez une option (1-4) : ").strip()
    
    if choix == "1":
        print("\n-> Option 1 : Ajout en cours...")
    elif choix == "2":
        print("\n-> Option 2 : Affichage en cours...")
    elif choix == "3":
        print("\n-> Option 3 : Recherche en cours...")
    elif choix == "4":
        print("\nFin du programme. Au revoir !")
    else:
        print("\nErreur : Option invalide. Recommencez.")


# Partie 3 – Dictionnaires
#6) Créez  un dictionnaire pour stocker les métadonnées de chaque dataset 

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

# Partie 6 – Compréhensions (Listes et Dictionnaires)
# 11) Affichez  les statistiques sur les datasets : nombre de datasets, nombre total de lignes, nombre moyens de colonnes, datasets publics, datasets privés, Nombre de datasets au format CSV et JSON, répartition par domaine.

print("\nStatistiques sur les datasets :")
print(f"Nombre de datasets : {len(datasets)}")
print(f"Nombre total de lignes : {sum(metadonnees['nb_lignes'] for metadonnees in datasets.values())}")
print(f"Nombre moyen de colonnes : {sum(metadonnees['nb_colonnes'] for metadonnees in datasets.values()) / len(datasets) if datasets else 0}")
print(f"Datasets publics : {sum(1 for metadonnees in datasets.values() if metadonnees['public'])}")
print(f"Datasets privés : {len(datasets) - sum(1 for metadonnees in datasets.values() if metadonnees['public'])}")
print(f"Datasets au format CSV : {sum(1 for metadonnees in datasets.values() if metadonnees['format'] == 'csv')}")
print(f"Datasets au format JSON : {sum(1 for metadonnees in datasets.values() if metadonnees['format'] == 'json')}")
for domaine in domaines_autorises:
    count = sum(1 for metadonnees in datasets.values() if metadonnees['domaine'] == domaine)
    print(f"Répartition par domaine '{domaine}' : {count}")

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

# Partie 8 – Exceptions
# 13) Gérez les exceptions pour les entrées utilisateur et les opérations sur les fichiers.
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

# Partie 9 – Fonctions
# 14) Refactorisez  le programme en créant les fonctions suivantes : afficher_menu(), ajouter_dataset(), trier_datasets(), rechercher_dataset(), modifier_dataset(), supprimer_dataset(), afficher_statistiques(), sauvegarder_donnees(), recharger_donnees() et safe_input().

def afficher_menu():
    print("\n----------------- MENU -----------------")
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher")
    print("4. Modifier un dataset")
    print("5. Supprimer un dataset")
    print("6. Afficher les statistiques")
    print("7. Sauvegarder les données")
    print("8. Recharger les données")
    print("9. Quitter")

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

def trier_datasets():
    datasets_list.sort(key=lambda x: x[0])
    print("\nDatasets triés par nom :")
    for nom, metadonnees in datasets_list:
        print(f"- {nom}")

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

def supprimer_dataset():
    nom_suppression = safe_input("Entrez le nom du dataset à supprimer : ", str)
    for i, (nom, metadonnees) in enumerate(datasets_list):
        if nom == nom_suppression:
            del datasets[nom]
            del datasets_list[i]
            print(f"\nDataset '{nom}' supprimé avec succès.")
            return
    print("Dataset non trouvé.")

def afficher_statistiques():
    print("\nStatistiques sur les datasets :")
    print(f"Nombre de datasets : {len(datasets)}")
    print(f"Nombre total de lignes : {sum(metadonnees['nb_lignes'] for metadonnees in datasets.values())}")
    print(f"Nombre moyen de colonnes : {sum(metadonnees['nb_colonnes'] for metadonnees in datasets.values()) / len(datasets) if datasets else 0}")
    print(f"Datasets publics : {sum(1 for metadonnees in datasets.values() if metadonnees['public'])}")
    print(f"Datasets privés : {len(datasets) - sum(1 for metadonnees in datasets.values() if metadonnees['public'])}")
    print(f"Datasets au format CSV : {sum(1 for metadonnees in datasets.values() if metadonnees['format'] == 'csv')}")
    print(f"Datasets au format JSON : {sum(1 for metadonnees in datasets.values() if metadonnees['format'] == 'json')}")
    for domaine in domaines_autorises:
        count = sum(1 for metadonnees in datasets.values() if metadonnees['domaine'] == domaine)
        print(f"Répartition par domaine '{domaine}' : {count}")

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



