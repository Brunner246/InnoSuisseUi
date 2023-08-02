import sys

from PySide2 import QtWidgets

from Controller.CController import CController, CDummyController
from Interfaces.IController import IController
from View.CInnosuisse import CInnosuisseDialog

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    lBusinessLogic: IController = CController()
    lDummyLogic: IController = CDummyController()
    lDummyLogic("controller instanced")
    try:
        lDialog = CInnosuisseDialog(lDummyLogic)
        lDialog.show()
        sys.exit(app.exec_())
    except ValueError as e:
        print(e)
        sys.exit(1)