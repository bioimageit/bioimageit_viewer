# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='bioimageit_viewer',
    version="0.2.0",
    author="Sylvain Prigent and BioImageIT team",
    author_email="bioimageit@gmail.com",
    description='Gui application for BioImageIT data viewer',
    long_description=readme,
    url='https://github.com/bioimageit/bioimageit_viewer',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        "bioimageit_framework>=0.2.0",
        "bioimageit_formats>=0.2.0",
        "napari",
        "pandas",
        "scikit-image>=0.18.3"
    ],
    )
