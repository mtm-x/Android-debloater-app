from PySide6.QtCore import (QCoreApplication,
    QMetaObject, QRect,
    QSize)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import ( QLabel, QLineEdit, QListWidget, QPushButton,
    QWidget)

class Ui_Debloater(object):
    def setupUi(self, Debloater):
        if not Debloater.objectName():
            Debloater.setObjectName(u"Debloater")
        Debloater.resize(400, 508)
        Debloater.setMinimumSize(QSize(400, 508))
        Debloater.setMaximumSize(QSize(400, 508))
        Debloater.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"")
        self.centralwidget = QWidget(Debloater)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 180, 211, 41))
        self.lineEdit.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);\n"
"font: regular 11pt \"FreeSans\";")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 160, 191, 17))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 600 9pt \"FreeSans\";")
        self.searchbut = QPushButton(self.centralwidget)
        self.searchbut.setObjectName(u"searchbut")
        self.searchbut.setGeometry(QRect(250, 180, 51, 41))
        self.searchbut.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditFind))
        self.searchbut.setIcon(icon)
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(30, 280, 341, 151))
        self.listWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 600 9pt \"FreeSans\";")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 250, 231, 17))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 600 9pt \"FreeSans\";\n"
"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 40, 191, 17))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 600 9pt \"FreeSans\";")
        self.listWidget_2 = QListWidget(self.centralwidget)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(30, 60, 261, 71))
        self.listWidget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 600 9pt \"FreeSans\";")
        self.exitbut = QPushButton(self.centralwidget)
        self.exitbut.setObjectName(u"exitbut")
        self.exitbut.setGeometry(QRect(240, 460, 51, 41))
        self.exitbut.setStyleSheet(u"font: 9pt \"FreeSans\";\n"
"color: rgb(255, 255, 255);")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WindowClose))
        self.exitbut.setIcon(icon1)
        self.infobut = QPushButton(self.centralwidget)
        self.infobut.setObjectName(u"infobut")
        self.infobut.setGeometry(QRect(110, 460, 51, 41))
        self.infobut.setStyleSheet(u"font: 9pt \"FreeSans\";\n"
"color: rgb(255, 255, 255);")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout))
        self.infobut.setIcon(icon2)
        Debloater.setCentralWidget(self.centralwidget)

        self.retranslateUi(Debloater)

        QMetaObject.connectSlotsByName(Debloater)
    # setupUi

    def retranslateUi(self, Debloater):
        Debloater.setWindowTitle(QCoreApplication.translate("Debloater", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Debloater", u"Enter the application name:", None))
        self.searchbut.setText("")
        self.label_2.setText(QCoreApplication.translate("Debloater", u"Click the package you want to remove", None))
        self.label_3.setText(QCoreApplication.translate("Debloater", u"Connected device info", None))
        self.exitbut.setText(QCoreApplication.translate("Debloater", u"EXIT", None))
        self.infobut.setText(QCoreApplication.translate("Debloater", u"INFO", None))
    # retranslateUi

