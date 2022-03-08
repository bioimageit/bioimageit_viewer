Install
=======

This section contains the instructions to install ``bioimageit_viewer`` for developers.

.. code-block:: bash

    mkdir bioimageit
    cd bioimageit 
    python -m env .env
    source .env/bin/activate
    git clone https://github.com/bioimageit/bioimageit_formats.git
    pip install -e ./bioimageit_formats
    git clone https://github.com/bioimageit/bioimageit_viewer.git
    pip install -e ./bioimageit_viewer

