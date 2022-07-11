import pandas as pd

from datetime import datetime
from pathlib import Path

from utils.my_utils import open_json, histo_update


def first():

    param_file = Path("input", "param.json")

    histo_file = Path("input", "histo_dispo.csv")
    dispo_file = Path("input", "dispo.csv")
    # forma_file = Path("input", f"TR_PERSFORM.{datetime.now().strftime('%Y%m%d')}0015")
    forma_file = Path("input", f"TR_PERSFORM.202207030015") # Test seulement

    param = open_json(param_file)

    """
    Mise à jour des compétences et des personnels du fichier historique
    """
    histo_update(histo_file, forma_file)

    """
    Mise à jour des candidatures par ajout de date à la liste
    """

    df_dispo = pd.read_csv(dispo_file)    # Lecture du fichier de dispo déclarées







    # my_date = datetime.strptime(param["DEBUT"], "%d/%m/%Y")
    #
    # my_list = []
    # for i in df_dispo['Matricule']:
    #     my_list.append(i)
    #
    # for j in df_forma.itertuples():
    #     print(f"{j.Matricule} - {j.Competence}")


if __name__ == '__main__':
    first()
