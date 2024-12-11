import sys
import subprocess
from PySide6.QtWidgets import QApplication, QMainWindow , QDialog
from ui_form import Ui_Debloater 
from dialog import Ui_Dialog
import webbrowser

class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Debloater()
        self.dialog = None
        self.ui.setupUi(self) 
        self.ui.searchbut.clicked.connect(self.search_but_clicked)
        self.ui.listWidget.itemPressed.connect(self.pressed_list_item)
        self.setWindowTitle("Android Debloater")
        self.ui.exitbut.clicked.connect(self.close)
        self.ui.infobut.clicked.connect(self.web)
        try:
            process = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if "device"  in process.stdout:
                self.ui.listWidget_2.addItem(process.stdout)
                
        except FileNotFoundError:
            self.ui.listWidget_2.addItem("ADB not found.")

    def search_but_clicked(self):
        self.ui.listWidget.clear()
        self.app_name=self.ui.lineEdit.text()
        package_list=subprocess.run(['adb','shell','pm','list','packages','|','grep',self.app_name],stdout=subprocess.PIPE,text=True).stdout.splitlines()
        cleaned_package_list = [pkg.replace("package:", "") for pkg in package_list]
        for package in cleaned_package_list:
            self.ui.listWidget.addItem(package)
            
    def pressed_list_item(self,test):
        self.item_text = test.text()
        self.dialog = Dialog(self)
        self.dialog.ui.buttonBox.accepted.connect(self.dialog_accepted)
        self.dialog.ui.buttonBox.rejected.connect(self.dialog_rejected)
        self.dialog.exec()
    def dialog_accepted(self):
        subprocess.run(['adb','shell','pm','uninstall','--user','0',self.item_text])
        self.dialog.close()
    def dialog_rejected(self):
        self.dialog.close()
    def web(self):
        webbrowser.open("https://github.com/mtm-x")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
