from qtpy.QtWidgets import (QVBoxLayout, QWidget, QTabWidget)

from bioimageit_formats import FormatsAccess
from bioimageit_framework.widgets import BiWidget, BiTabWidget
from .napari import BiNapariViewer
from .table import BiTableViewer


class BiMultiViewer(BiWidget):
    def __init__(self):
        super().__init__()
        
        # viewers
        self.napari_viewer = None
        self.table_viewer = None

        layout = QVBoxLayout()
        self.widget.setLayout(layout)
        layout.setContentsMargins(0, 0, 0, 0)
        self.tab = BiTabWidget()
        layout.addWidget(self.tab.widget)

    def add_loaded_data(self, container, data_name, format_name):
        format_info = FormatsAccess.instance().get(format_name) 
        viewer_name = format_info.viewer

        if viewer_name == 'napari':
            if self.napari_viewer is None:
                self.napari_viewer = BiNapariViewer()
                self.tab.add_tab(self.napari_viewer, 'Images', 'Data of type image')
            self.napari_viewer.add_loaded_data(container, data_name, format_name) 
            self.tab.switch_tab('Images') 

        elif viewer_name == 'table':
            if self.table_viewer is None:
                self.table_viewer = BiTableViewer()
                self.tab.add_tab(self.table_viewer, 'Tables', 'Data of type table')
            self.table_viewer.add_loaded_data(container, data_name) 
            self.tab.switch_tab('Tables') 

    def add_data(self, uri, data_name, format_name):

        format_info = FormatsAccess.instance().get(format_name) 
        viewer_name = format_info.viewer

        if viewer_name == 'napari':
            if self.napari_viewer is None:
                self.napari_viewer = BiNapariViewer()
                self.tab.add_tab(self.napari_viewer, 'Images', 'Data of type image')
            self.napari_viewer.add_data(uri, data_name, format_name) 
            self.tab.switch_tab('Images')   

        elif viewer_name == 'table':
            if self.table_viewer is None:
                self.table_viewer = BiTableViewer()
                self.tab.add_tab(self.table_viewer, 'Tables', 'Data of type table')
            self.table_viewer.add_data(uri, data_name, format_name) 
            self.tab.switch_tab('Tables')    
