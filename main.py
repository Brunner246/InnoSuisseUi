import sys

from PySide2 import QtWidgets
from PySide2.QtCore import QTranslator

from Controller.CController import CController, CDummyController
from Interfaces.IController import IController
from View.CInnosuisse import CInnosuisseDialog

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    lTranslator = QTranslator()
    if not lTranslator:
        sys.exit(1)

    if lTranslator.load("./View/Translation/Translation_de.qm"):
        if app.installTranslator(lTranslator):
            print("Translator installed")
        else:
            print("Translator not installed")
    else:
        print("Translator not loaded")

    lController: IController = CDummyController()  # CController()
    try:
        lDialog = CInnosuisseDialog(lController)
        lDialog.show()
        sys.exit(app.exec_())
    except ValueError as e:
        print(e)
        sys.exit(1)
