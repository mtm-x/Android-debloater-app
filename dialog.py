from PySide6.QtCore import (QCoreApplication,
    QMetaObject, QRect, Qt)

from PySide6.QtWidgets import (QDialogButtonBox,
    QLabel)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(255, 112)
        Dialog.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(-130, 60, 341, 32))
        self.buttonBox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 30, 91, 21))
        self.label.setStyleSheet(u"font: 14pt \"FreeSans\";\n"
"color: rgb(255, 255, 255);")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Uninstall??", None))
    # retranslateUi

