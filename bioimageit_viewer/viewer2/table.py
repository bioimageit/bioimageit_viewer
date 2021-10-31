from PySide2.QtWidgets import (QVBoxLayout, QWidget, QTabWidget, 
                               QTableWidget, QTableWidgetItem)

from bioimageit_formats import FormatsAccess, formatsServices

class BiTableViewer(QWidget):
    def __init__(self):
        super().__init__()
        
        # napari widget
        self.viewer = QTabWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        layout.addWidget(self.viewer)

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
