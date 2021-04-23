from PyQt5.QtWidgets import QWidget


class BiReader:
    """Define a reader interface

    Attributes
    ----------
    file: str
        file to read

    """
    def __init__(self):
        self.file = ''

    def read(self, file):
        """Read the data into a BiData object

        Return
        ------
        a BiData object
        """
        self.file = file
        print("default reader for file", self.file)


class BiViewer:
    """Define a viewer interface

    Attributes
    ----------
    data_list: list
        List of BiDisplayData to display in the viewer

    """
    def __init__(self):
        self.data_list = []
        self.widget = QWidget()

    def refresh(self):
        """Implement this method to refresh the viewer

        Needed when the data change

        """
        print("You are calling the refresh of the abstract viewer on data",
              self.data_list[0].uri)

    def get_widget(self):
        """Get the QWidget that is the viewer

        Return
        ------
        QWidget containing the view

        """
        return self.widget
