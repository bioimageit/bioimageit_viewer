import pandas as pd
from bioimageit_viewer.containers import BiData
from bioimageit_viewer.definitions import BiReader


class ArrayCsvReaderBuilder:
    """Service builder for the csv table reader service"""

    def __init__(self):
        self._instance = None

    def __call__(self, **_ignored):
        if not self._instance:
            self._instance = ArrayCsvReader()
        return self._instance


class ArrayCsvReader(BiReader):
    def __init__(self):
        super().__init__()

    def read(self, file):
        self.file = file
        array = pd.read_csv(file, nrows=1)
        data = BiData()
        data.name = 'pandasseries'
        data.data = array
        return data
