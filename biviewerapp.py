import sys
from bioimageit_viewer.display import BiDisplay
from bioimageit_viewer.containers import BiDisplayPlan

from PySide2.QtWidgets import QApplication

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)

    # load the file uri
    plan_uri = ""
    if len(sys.argv) > 1:
        plan_uri = sys.argv[1]
    if plan_uri == "":
        print("bi viewer: no input plan file")

    plan = BiDisplayPlan()
    plan.load(plan_uri)

    display = BiDisplay(plan)
    display.get_widget().show()

    sys.exit(app.exec_())
