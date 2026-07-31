# Application python permettant de gerer des jeux de données.

# Partie 1 : Types de base, variables, Entrées et sorties 
#   3) Demandez à l’utilisateur de saisir les métadonnées d’un dataset :


nom_dataset = input("Entrez le nom du dataset : ")
domain = input("Entrez le domaine du dataset : Santé; Agriculture; Environnement... etc : ")
nb_lignes = int(input("Entrez le nombre de lignes du dataset : "))
nb_colonnes = int(input("Entrez le nombre de colonnes du dataset : "))
taille_mo = float(input("Entrez la taille du dataset en Mo : "))
public = bool(input("Le dataset est-il public ? (True/False) : "))
format_doc = ""
while format_doc not in ["csv", "json"]:
    format_doc = input("Choisissez le format du document (csv/json) : ").lower()

# 4) Affichez ensuite un résumé formaté. 

print(f"\nRésumé du dataset '{nom_dataset}':")
print(f"Domaine: {domain}")
print(f"Nombre de lignes: {nb_lignes}")
print(f"Nombre de colonnes: {nb_colonnes}")
print(f"Taille: {taille_mo} Mo")
print(f"Public: {public}")
print(f"Format: {format_doc}")

# Partie 2 : Structures de contrôle 
# 5) Créez  un menu interactif (provisoire) 

# 1. Ajouter un dataset 
# 2. Afficher les datasets 
# 3. Rechercher 
# 4. Quitter 


