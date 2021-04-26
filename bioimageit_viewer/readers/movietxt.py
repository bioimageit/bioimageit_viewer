import os
import numpy as np
from skimage import io

from bioimageit_viewer.containers import BiData
from bioimageit_viewer.definitions import BiReader


class MovieTxtReaderBuilder:
    """Service builder for the movie

    The movie represented with a list of tiff file listed
    in a txt file

    """

    def __init__(self):
        self._instance = None

    def __call__(self, **_ignored):
        if not self._instance:
            self._instance = MovieTxtReader()
        return self._instance


class MovieTxtReader(BiReader):
    def __init__(self):
        super().__init__()

    def read(self, file):
        self.file = file
        dir_path = os.path.dirname(file)
        frames = []
        with open(file) as my_file:
            frames = my_file.read().splitlines()

        num_frames = len(frames)

        # load the first frame to get the size
        data0 = io.imread(os.path.join(dir_path, frames[0]))

        dims = list(data0.shape)
        dims.insert(0, num_frames)
        data = np.empty(dims)
        data[0, ...] = data0

        if num_frames > 1:
            for i in range(1, num_frames):
                data[i, ...] = io.imread(os.path.join(dir_path, frames[i]))

        bidata = BiData()
        bidata.name = 'ndimage'
        bidata.array = data
        return bidata
