Introduction
============

``bioimageit_viewer`` is a desktop graphical user interface to visualize scientific data. It is
based on ``bioimageit_formats`` to manage the data formats and the visualisation is displayed using
python viewers like QtTableView or napari

Context
-------
``bioimageit_viewer`` has been developed by **Sylvain Prigent** in a project funded by
`France-BioImaging <https://france-bioimaging.org/>`_
``bioimageit_viewer`` is part of the BioImageIT project. Please find all the other developed tools
`here <https://github.com/bioimageit>`_

BioImageIT Viewer
-----------------
BioImageIT Viewer is a python3 Qt application. It provides a graphical user interface for scientific
data visualisation.
It is made of a main widget called ``BiMultiViewer`` that can visualize the data format available in
``bioimageit_formats``:

.. code-block:: python

    from bioimageit_formats import FormatsAccess
    from bioimageit_viewer.viewer import BiMultiViewer

    # initialize the formats
    FormatsAccess('formats.json')

    # add an image
    viewer.add_data('myimagefile.tif', 'myimage', 'imagetiff')

    # start the viewer
    app = QApplication(["BioImageIT viewer"])
    viewer.show()
    sys.exit(app.exec_())
