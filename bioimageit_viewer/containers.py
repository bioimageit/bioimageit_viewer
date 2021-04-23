import os
import json


class BiData:
    """Container interface for a readed data

    The interface only contains a name of the container to identify the data

    Attributes
    ----------
    name: str
        Data name

    """
    def __init__(self, name=''):
        self.name = name


class BiFormat:
    """Container for a data format information

    Attributes
    ----------
    name: str
        Name (ID) of the format
    extension: str
        extension of the file format
    reader: str
        Name of the reader dedicated to this format
    viewer: str
        Name of the viewer widget dedicated to this format

    """
    def __init__(self, name='', extension='', reader='', viewer=''):
        self.name = name
        self.extension = extension
        self.reader = reader
        self.viewer = viewer


class BiFormats:
    """Dictionary container for the data formats

    Attributes
    ----------
    formats: dict
        Dictionary of formats: self.formats['formatname'] = BiFormat

    """
    def __init__(self):
        self.formats = dict()

    def load(self, file):
        """Load the available formats from a json file

        Parameters
        ----------
        file: str
            URI of the json file containing the formats list

        """
        if os.path.getsize(file) > 0:
            with open(file) as json_file:
                formats_json = json.load(json_file)
                for form in formats_json['formats']:
                    self.formats[form['name']] = BiFormat(form['name'],
                                                          form['extension'],
                                                          form['reader'],
                                                          form['viewer'])


class BiDisplayData:
    """Container for a data information

    Attributes
    ----------
    uri: str
        URI of the data file
    format_: str
        Name of the data format (needed to get the write reader and viewer)

    """
    def __init__(self, uri='', format_=''):
        self.uri = uri
        self.format_ = format_


class BiDisplayRegion:
    """Container for a display region information

    Attributes
    ----------
    position: list
        Position of the region in the grid layout. It is a list of 4 int:
        x position, y position, x span, y span
    widget: str
        Name of the widget 'BiViewer' displayed in this region
    data_list: list
        List of the data 'BiDisplayData' to display in this region

    """
    def __init__(self):
        self.position = [0, 0, 1, 1]
        self.widget = ''
        self.data_list = []


class BiDisplayPlan:
    """Container for a display plan

    The display plan contains all the data needed to build the BiDisplay window

    Attributes
    ----------
    regions: list
        List of 'BiDisplayRegion' that constitutes the display

    """
    def __init__(self):
        self.regions = []

    def load(self, file):
        """Load a json plan

        Parameters
        ----------
        file: str
            URI of the file to load

        """
        if os.path.getsize(file) > 0:
            with open(file) as json_file:
                plan_json = json.load(json_file)
                for region_json in plan_json['plan']:
                    region = BiDisplayRegion()
                    print('region=', region_json)
                    region.position = region_json['position']
                    region.widget = region_json['widget']
                    for data_json in region_json['data']:
                        print(data_json)
                        region.data_list.append(
                            BiDisplayData(data_json['uri'],
                                          data_json['format']))
                    self.regions.append(region)
