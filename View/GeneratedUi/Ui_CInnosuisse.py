# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CInnosuissePFMdoP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.10
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pbn_click_me = QPushButton(Dialog)
        self.pbn_click_me.setObjectName(u"pbn_click_me")

        self.horizontalLayout_3.addWidget(self.pbn_click_me)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 190, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lab_edit = QLabel(Dialog)
        self.lab_edit.setObjectName(u"lab_edit")

        self.horizontalLayout_2.addWidget(self.lab_edit)

        self.led_text = QLineEdit(Dialog)
        self.led_text.setObjectName(u"led_text")

        self.horizontalLayout_2.addWidget(self.led_text)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pbn_click = QPushButton(Dialog)
        self.pbn_click.setObjectName(u"pbn_click")

        self.horizontalLayout.addWidget(self.pbn_click)

        self.pbn_cancel = QPushButton(Dialog)
        self.pbn_cancel.setObjectName(u"pbn_cancel")

        self.horizontalLayout.addWidget(self.pbn_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)
        self.pbn_cancel.clicked.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pbn_click_me.setText(QCoreApplication.translate("Dialog", u"click", None))
        self.lab_edit.setText(QCoreApplication.translate("Dialog", u"enter somethihng", None))
        self.pbn_click.setText(QCoreApplication.translate("Dialog", u"click me", None))
        self.pbn_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

