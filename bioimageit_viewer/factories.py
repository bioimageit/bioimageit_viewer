from bioimageit_viewer.readers.csvtable import CSVTableReaderBuilder
from bioimageit_viewer.viewers.table import TableViewerBuilder


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

viewerService = ViewerServiceProvider()
viewerService.register_builder('table', TableViewerBuilder())
