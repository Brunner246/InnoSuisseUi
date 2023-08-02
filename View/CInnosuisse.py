from PySide2 import QtWidgets

from GeneratedUi.Ui_CInnosuisse import Ui_Dialog
from Interfaces.IController import IController


class CInnosuisseDialog(QtWidgets.QDialog):
    def __init__(self, aController: IController, aParent=None):
        super().__init__(aParent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.label.setText("Hello World")
        self.mController = aController

        self.ui.pushButton.clicked.connect(self.mController.do_something)
        self.ui.pushButton_2.clicked.connect(lambda: print(self.ui.label.text()))
