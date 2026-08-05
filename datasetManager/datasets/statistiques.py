# Les statistiques sur les datasets
from datasets.gestion import ajouter_dataset


def afficher_statistiques():
    liste = ajouter_dataset()
    nom_dataset, domain, nb_lignes, nb_colonnes, taille_mo, public, format_doc = liste
    datasets[nom_dataset] = {
    "domaine": domain,
    "nb_lignes": nb_lignes,
    "nb_colonnes": nb_colonnes,
    "taille_mo": taille_mo,
    "public": public,
    "format": format_doc
    }
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