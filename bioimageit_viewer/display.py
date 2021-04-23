from PyQt5.QtWidgets import QWidget, QGridLayout

from bioimageit_viewer.factories import readerService, viewerService


class BiDisplay:
    """Class that create the main Viewer

    Attributes
    ----------
    plan: BiDisplayPlan
        Plan to be displayed

    """
    def __init__(self, plan=None):
        self.plan = plan
        self.widget = QWidget()

        if self.plan:
            self.render()

    def render(self):
        """Render the display"""
        layout = QGridLayout()
        self.widget.setLayout(layout)
        for region in self.plan.regions:
            viewer = viewerService.get(region.widget)
            for data in region.data_list:
                reader = readerService.get(data.format_)
                bidata = reader.read(data.uri)
                viewer.data_list.append(bidata)
            viewer.refresh()
            layout.addWidget(viewer.get_widget(), region.position[0],
                             region.position[1], region.position[2],
                             region.position[3])

    def get_widget(self):
        return self.widget
