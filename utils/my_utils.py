import json
import pandas as pd

def open_json(filepath):
    with open(filepath) as file:
        return json.load(file)


def histo_update(histo_file, forma_file):
    """
    Mise à jour du fichier csv de l'historique des dispos. Les compétences des personnels présents dans le fichier sont seulement mises à jour.
    Les personnels absents du fichier d'historique sont rajoutées sur la base du fichier des compétences.
    Le fichier mis à jour est sauvegardé
    :return: None
    """

    df_histo = pd.read_csv(histo_file)  # Lecture du fichier d'historique'

    df_forma = pd.read_csv(forma_file,
                           sep=";",
                           header=None,
                           usecols=[0, 1],
                           names=["Matricule", "Competence"]
                           )

    forma_dict = {}
    for i in df_forma.itertuples():
        if forma_dict.get(i.Matricule):
            if i.Competence not in forma_dict[i.Matricule][4]:
                forma_dict[i.Matricule][4].append(i.Competence)
        else:
            forma_dict[i.Matricule] = (i.Matricule, [], [], [], [i.Competence,])

    """
    Création d'une liste des matricules des personnels actifs depuis le fichier des compétences
    """
    mat_forma_list = []
    for i in forma_dict.keys():
        mat_forma_list.append(i)

    """
    Création d'une liste des matricules des personnels présents dans le fichier historique
    Mise à jour de la liste des compétences si le personnel existe déja dans le fichier
    Sppression des personnels absents du fichier des compétences
    """
    data = []
    mat_histo_list = []
    for i in df_histo.itertuples():
        mat_histo_list.append(i.Matricule)
        if i.Matricule in mat_forma_list:
            data.append((i.Matricule,i.Dispo,i.Presel,i.Enga, forma_dict[i.Matricule][4]))

    """
    Ajout des personnels présents dans le fichier des compétences mais absent du fichier d'historique
    """
    for i in mat_forma_list:
        if i not in mat_histo_list:
            data.append((forma_dict[i][0], [], [], [],forma_dict[i][4]))

    """
    Création du DataFrame
    Sauvegarde en .csv
    """
    df = pd.DataFrame(data, columns=["Matricule", "Dispo", "Presel", "Enga", "Comp"])
    df.to_csv(histo_file, index=False, columns=["Matricule","Dispo","Presel","Enga","Comp"])