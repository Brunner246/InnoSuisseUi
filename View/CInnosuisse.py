from PySide2 import QtWidgets
from PySide2.QtCore import (Slot,
                            Signal)
from View.GeneratedUi.Ui_CInnosuisse import Ui_Dialog
from Interfaces.IController import IController


class CInnosuisseDialog(QtWidgets.QDialog):
    textChanged = Signal(str)

    def __init__(self, a_controller: IController, aParent=None):
        super().__init__(aParent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.lab_edit.setText("Hello World")

        if a_controller is None:
            raise ValueError("controller is nullptr")

        self._m_controller = a_controller

        self.ui.pbn_click_me.clicked.connect(self._do_something)
        self.ui.pbn_click.clicked.connect(lambda: (print(self.ui.lab_edit.text()),
                                                   print(self.ui.led_text.text())))
        self.ui.led_text.textChanged.connect(self._print_some_text)
        self.textChanged.connect(lambda data: print(data))

    @Slot(str)
    def _print_some_text(self, some_text: str):
        print(some_text)
        self.textChanged.emit("got edited")

    def _do_something(self):
        self._m_controller.do_something()
