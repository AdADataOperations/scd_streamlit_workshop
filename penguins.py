import kagglehub
import pandas as pd


class Penguins:
    def __init__(self):
        self.data = self._read_data()
        self.species = list(self.data["species"].unique())
        # self.islands = list(self.data["Species"].unique())

    @staticmethod
    def _read_data():
        try:
            return pd.read_csv("./Data/penguins.csv")
        except FileNotFoundError:
            # Download latest version
            path = kagglehub.dataset_download("satyajeetrai/palmer-penguins-dataset-for-eda")
            return pd.read_csv(path + "/penguins.csv").set_index("id")