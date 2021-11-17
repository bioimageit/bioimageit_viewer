import PySide2.QtCore
from PySide2.QtWidgets import (QVBoxLayout, QWidget, QTabWidget)

import napari
from bioimageit_formats import FormatsAccess, formatsServices

class BiNapariViewer(QWidget):
    def __init__(self):
        super().__init__()
        
        # napari widget
        self.viewer = napari.Viewer(show=False)

        # move doc layers
        dock_widget = self.viewer._window.qt_viewer.dockLayerControls
        self.viewer._window._qt_window.addDockWidget(PySide2.QtCore.Qt.RightDockWidgetArea, dock_widget)

        dock_widget_list = self.viewer._window.qt_viewer.dockLayerList
        self.viewer._window._qt_window.addDockWidget(PySide2.QtCore.Qt.RightDockWidgetArea, dock_widget_list)

        # add napari to widget
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        layout.addWidget(self.viewer._window._qt_window)

    def add_data(self, uri: str, data_name: str, format_name: str):
        format_info = FormatsAccess.instance().get(format_name) 
        data = formatsServices.get(format_info.reader).read(uri)

        image_formats = ['imagetiff', 'movietxt']    
        if format_info.name in image_formats:
            self.viewer.add_image(data, name=data_name)
        elif format_info.name == 'trackmatemodel':
            self.viewer.add_tracks(data, name=data_name)
        else:
            print('error NapariViewer cannot display the format ' + format_info.name)  