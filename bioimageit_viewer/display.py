from PySide2.QtWidgets import QWidget


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
        pass

    def get_widget(self):
        return self.widget
