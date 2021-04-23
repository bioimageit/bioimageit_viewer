from bioimageit_viewer.definitions import BiViewer
from bioimageit_viewer.containers import BiData

from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QTableWidget,
                               QTableWidgetItem)


class TableViewer(BiViewer):

    def __init__(self):
        super().__init__(self)

    def refresh(self):

        self.widget.setObjectName('BiWidget')
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.widget.setLayout(layout)

        tableWidget = QTableWidget()
        layout.addWidget(tableWidget)



            tableWidget.setRowCount(len(rows))
            if len(rows) > 0:
                tableWidget.setColumnCount(len(rows[0]))
            row_idx = 0
            for row in rows:
                col_idx = 0
                for el in range(len(row)):
                    tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(row[el]))
                    col_idx += 1
                row_idx += 1