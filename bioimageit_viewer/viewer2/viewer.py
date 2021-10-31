from PySide2.QtWidgets import (QVBoxLayout, QWidget, QTabWidget)

from bioimageit_formats import FormatsAccess
from .napari import BiNapariViewer
from .table import BiTableViewer


class BiMultiViewer(QWidget):
    def __init__(self):
        super().__init__()
        
        # viewers
        self.napari_viewer = None
        self.table_viewer = None

        # widget
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget()
        layout.addWidget(self.tabWidget)
        self.setLayout(layout)

    def add_data(self, uri, data_name, format_name):

        format_info = FormatsAccess.instance().get(format_name) 
        viewer_name = format_info.viewer

        if viewer_name == 'napari':
            if not self.napari_viewer:
                self.napari_viewer = BiNapariViewer()
                self.tabWidget.addTab(self.napari_viewer, 'Images')
            self.napari_viewer.add_data(uri, data_name, format_name)    

        elif viewer_name == 'table':
            if not self.table_viewer:
                self.table_viewer = BiTableViewer()
                self.tabWidget.addTab(self.table_viewer, 'Tables')
            self.table_viewer.add_data(uri, data_name, format_name)     
