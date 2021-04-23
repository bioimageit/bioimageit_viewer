import numpy as np
from skimage import io

from bioimageit_viewer.containers import BiData
from bioimageit_viewer.definitions import BiReader


class ImageTiffReaderBuilder:
    """Service builder for the csv table reader service"""

    def __init__(self):
        self._instance = None

    def __call__(self, **_ignored):
        if not self._instance:
            self._instance = ImageTiffReader()
        return self._instance


class ImageTiffReader(BiReader):
    def __init__(self):
        super().__init__()
        self.root = None
        self.tracks = None

    def read(self, file):
        self.file = file
        bidata = BiData()
        bidata.name = 'imagetiff'
        bidata.array = io.imread(self.file)
        return bidata
