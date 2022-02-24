import os
import sys

from bioimageit_core import ConfigAccess
from bioimageit_formats import FormatsAccess
from bioimageit_framework.theme import BiThemeAccess, BiThemeSheets
from bioimageit_viewer.viewer import BiMultiViewer

from PySide2.QtWidgets import QApplication

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(["BioImageIT"])
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # load and set the theme
    BiThemeAccess(os.path.join(dir_path, '..', 'theme', 'dark'))
    BiThemeAccess.instance().set_stylesheet(app, BiThemeSheets.sheets())

    # settings
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path_parent = os.path.abspath(os.path.join(dir_path, os.pardir))
    ConfigAccess(os.path.join(dir_path_parent, '..', 'config.json'))
    FormatsAccess(ConfigAccess.instance().get('formats')['file'])

    # viewer
    viewer = BiMultiViewer()

    # image data
    file = '/Users/sprigent/Documents/data/spinning3_denoising/MAX_CELL01.tif'
    file_name = 'MAX_CELL01'
    file_format = 'imagetiff'
    #viewer.add_data(file, file_name, file_format)

    file = '/Users/sprigent/Documents/data/spinning3_denoising/MAX_CELL01.tif'
    file_name = 'MAX_CELL02'
    file_format = 'imagetiff'
    #viewer.add_data(file, file_name, file_format)

    file = '/Users/sprigent/Documents/data/spinning3_denoising/CELL01_crop/CELL01_HELA_MPR42_GFP_20ms_0s_22 steps_0.4um_120.txt'
    file_name = 'CELL01_HELA_MPR42'
    file_format = 'movietxt'
    viewer.add_data(file, file_name, file_format)

    file = '/Users/sprigent/Documents/data/spinning3_denoising/table.csv'
    file_name = 'test'
    file_format = 'tablecsv'
    viewer.add_data(file, file_name, file_format)

    file = '/Users/sprigent/Documents/data/spinning3_denoising/table.csv'
    file_name = 'test2'
    file_format = 'tablecsv'
    viewer.add_data(file, file_name, file_format)


    viewer.widget.show()
    sys.exit(app.exec_())
