from PyQt5.uic import loadUi
from PyQt5.QtWidgets import * 
from interface import Ui_MainWindow 
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from cryptography.fernet import Fernet
import sys


class main(QMainWindow) : 
    def __init__(self) : 
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button.clicked.connect(self.clickme)
        self.ui.pushButton.clicked.connect(self.pushclick)

    def clickme (self): 
        self.text = self.ui.textEdit.toPlainText()
        self.key = Fernet.generate_key()
        f = Fernet(self.key)
        texts = self.text.encode("utf-8")
        self.token = f.encrypt(texts)
        self.ui.textEdit_2.setText(str(self.token))
    
    def pushclick(self) : 
        f = Fernet(self.key)
        dec = f.decrypt(self.token)
        decode = dec.decode()
        self.ui.textEdit_2.setText(str(decode))
        
if __name__ == "__main__" : 
    app = QApplication([])
    win = main()
    win.show()
    app.exec_()
