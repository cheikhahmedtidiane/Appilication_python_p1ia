# Partie 2 : Structures de contrôle 
# 5) Créez un menu interactif (provisoire)


from datasets.gestion import *
from datasets.statistiques import afficher_statistiques


def afficher_menu():
    choix = "" # Initialisation pour entrer dans la boucle

    while choix != "9": # Le programme reste actif TANT QUE choix n'est pas "9"
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
    
        choix = input("Choisissez une option (1-9) : ").strip()
        
        if choix == "1":
            ajouter_dataset()
            print("\n-> Option 1 : Données ajoutées")
        elif choix == "2":
            afficher_datasets()
            print("\n-> Option 2 : Affichage")
        elif choix == "3":
            rechercher_dataset()
            print("\n-> Option 3 : Recherche terminée")
        elif choix == "4":
            modifier_dataset()
            print("\n-> Option 4 : Modification terminée")
        elif choix == "5":
            supprimer_dataset()
            print("\n-> Option 5 : Suppression terminée")
        elif choix == "6":
            afficher_statistiques()
            print("\n-> Option 6 : Affichage des statistiques terminé")
        elif choix == "7":
            sauvegarder_donnees()
            print("\n-> Option 7 : Sauvegarde des données terminée")
        elif choix == "8":
            recharger_donnees()
            print("\n-> Option 8 : Rechargement des données terminé")
        elif choix == "9":
            print("\nFin du programme. Au revoir !")
        else:
            print("\nErreur : Option invalide. Recommencez.")