import napari
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QTableWidget,
                               QTableWidgetItem)

from bioimageit_viewer.definitions import BiViewer
from bioimageit_viewer.containers import BiData

class NapariViewerBuilder:
    """Service builder for the table viewer service"""

    def __init__(self):
        self._instance = None

    def __call__(self, **_ignored):
        if not self._instance:
            self._instance = NapariViewer()
        return self._instance


class NapariViewer(BiViewer):
    def __init__(self):
        super().__init__()

    def refresh(self):

        viewer = napari.Viewer(show=False)
        for bidata in self.data_list:
            if bidata.name == 'imagetiff':
                viewer.add_image(bidata.array, name=bidata.name)
            elif bidata.name == 'trackmatemodel':
                viewer.add_tracks(bidata.tracks, name='trackmatemodel')
            else:
                print('error NapariViewer cannot display ' + bidata.name)
        self.widget = viewer._window._qt_window
