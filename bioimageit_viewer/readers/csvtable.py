import pandas as pd
from bioimageit_viewer.containers import BiData
from bioimageit_viewer.definitions import BiReader


class CSVTableReaderBuilder:
    """Service builder for the csv table reader service"""

    def __init__(self):
        self._instance = None

    def __call__(self, **_ignored):
        if not self._instance:
            self._instance = CSVTableReader()
        return self._instance


class CSVTableReader(BiReader):
    def __init__(self):
        super().__init__()

    def read(self, file):
        self.file = file
        df = pd.read_csv(self.file)
        data = BiData()
        data.name = 'CSVTable'
        data.df = df
        return data
