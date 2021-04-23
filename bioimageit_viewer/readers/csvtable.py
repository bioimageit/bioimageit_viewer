import pandas as pd
from bioimageit_viewer.containers import BiData
from bioimageit_viewer.definitions import BiReader


class CSVTableReader(BiReader):
    def __init__(self, file):
        super().__init__(file)

    def read(self):
        df = pd.read_csv(self.file)
        data = BiData()
        data.df = df
        return data
