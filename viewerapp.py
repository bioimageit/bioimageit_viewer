import sys
from bioimageit_viewer.display import BiDisplay
from bioimageit_viewer.containers import BiDisplayPlan

from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)

    plan = BiDisplayPlan()
    plan.load('data/plan_trackmate.json')

    display = BiDisplay(plan)
    #display.render()
    display.get_widget().show()

    sys.exit(app.exec_())