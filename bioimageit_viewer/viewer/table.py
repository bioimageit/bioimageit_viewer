from qtpy.QtWidgets import (QVBoxLayout, QWidget, QTabWidget, 
                            QTableWidget, QTableWidgetItem)

from bioimageit_framework.widgets import BiWidget
from bioimageit_formats import FormatsAccess, formatsServices


class BiTableViewer(BiWidget):
    def __init__(self):
        super().__init__()
        
        # napari widget
        self.viewer = QTabWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.widget.setLayout(layout)
        layout.addWidget(self.viewer)

    def add_loaded_data(self, container, data_name):
        """add a python data to the viewer

        Parameters
        ----------
        container: Pandas.DataFrame
            Loaded data into a DataFrame
        data_name: str
            Name of the data. This is displayed in the widget title

        """
        # analys the content of the table
        tableWidget = QTableWidget()

        tableHeader = container.columns.values.tolist()

        # data frame case
        col_count = len(tableHeader)
        tableWidget.setColumnCount(col_count)
        tableWidget.setHorizontalHeaderLabels(tableHeader)

        tableWidget.setRowCount(len(container))
        for i in range(len(container)):
            for j in range(col_count):
                tableWidget.setItem(i, j, QTableWidgetItem(str(container.iloc[i,j])))
        self.viewer.addTab(tableWidget, data_name)

    def add_data(self, uri: str, data_name: str, format_name: str):
        format_info = FormatsAccess.instance().get(format_name) 
        data = formatsServices.get(format_info.reader).read(uri)

        # analys the content of the table
        tableWidget = QTableWidget()

        # data frame case
        df = data
        col_count = len(df.head())
        tableWidget.setColumnCount(col_count+1)
        tableWidget.setHorizontalHeaderLabels(df.head())

        tableWidget.setRowCount(len(df))
        for i in range(len(df)):
            for j in range(col_count+1):
                tableWidget.setItem(i, j, QTableWidgetItem(str(df.iloc[i,j])))
        self.viewer.addTab(tableWidget, data_name)
