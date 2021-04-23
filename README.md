# BioImageIT-Viewer

BioImageIT-Viewer is a GUI application to display scientific data using python libraries (Qt, matplotlib, napari)

This application is based on a list of data formats as a json file. Each format is associated with a data reader and a data viewer.
Then, the main application can display simultaniuously several data views using a viewer plan.

# Documentation

The documentation is available [here](https://bioimage-it.gitlabpages.inria.fr/bioimageit_viewer/)

# Build the documentation

The documentation is written with Sphinx. To build is run the commands:
```bash
cd docs
mkdir build
sphinx-build -b html ./source ./build
```




