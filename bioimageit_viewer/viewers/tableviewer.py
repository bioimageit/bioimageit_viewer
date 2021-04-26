from bioimageit_viewer.definitions import BiViewer
from bioimageit_viewer.containers import BiData

from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QTableWidget,
                               QTableWidgetItem)


class TableViewerBuilder:
    """Service builder for the table viewer service"""

    def __init__(self):
        self._instance = None

    def __call__(self, **_ignored):
        self._instance = TableViewer()
        return self._instance
        #if not self._instance:
        #    self._instance = TableViewer()
        #return self._instance


class TableViewer(BiViewer):
    def __init__(self):
        super().__init__()

    def refresh(self):

        self.widget.setObjectName('BiWidget')
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.widget.setLayout(layout)

        tableWidget = QTableWidget()
        layout.addWidget(tableWidget)

        bidata = self.data_list[0]
        if bidata.name == 'pandasdataframe':
            df = bidata.df
            col_count = len(df.head())
            tableWidget.setColumnCount(col_count)

            tableWidget.setHorizontalHeaderLabels(df.head())

            tableWidget.setRowCount(len(df))
            for i in range(len(df)):
                for j in range(col_count):
                    tableWidget.setItem(i, j, QTableWidgetItem(str(df.iloc[i,j])))
        elif bidata.name == 'pandasserie':
            data = bidata.data

            tableWidget.setColumnCount(data.size)
            tableWidget.setRowCount(1)

            j = -1
            for _, val in data.iteritems():
                j += 1
                tableWidget.setItem(0, j, QTableWidgetItem(str(val)))
        else:
            print('error TableViewer cannot display ' + bidata.name)    
