from bioimageit_viewer.readers.csvtable import CSVTableReaderBuilder
from bioimageit_viewer.readers.trackmatemodel import TrackmateModelReaderBuilder
from bioimageit_viewer.readers.imagetiff import ImageTiffReaderBuilder

from bioimageit_viewer.viewers.tableviewer import TableViewerBuilder
from bioimageit_viewer.viewers.napariviewer import NapariViewerBuilder

class ObjectFactory:
    def __init__(self):
        self._builders = {}

    def register_builder(self, key, builder):
        self._builders[key] = builder

    def create(self, key, **kwargs):
        builder = self._builders.get(key)
        if not builder:
            raise ValueError(key)
        return builder(**kwargs)


class ReaderServiceProvider(ObjectFactory):
    def get(self, service_id, **kwargs):
        return self.create(service_id, **kwargs)


class ViewerServiceProvider(ObjectFactory):
    def get(self, service_id, **kwargs):
        return self.create(service_id, **kwargs)


readerService = ReaderServiceProvider()
readerService.register_builder('csvtable', CSVTableReaderBuilder())
readerService.register_builder('trackmatemodel', TrackmateModelReaderBuilder())
readerService.register_builder('imagetiff', ImageTiffReaderBuilder())

viewerService = ViewerServiceProvider()
viewerService.register_builder('table', TableViewerBuilder())
viewerService.register_builder('napari', NapariViewerBuilder())