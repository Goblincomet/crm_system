from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BackEnd import ChangeCompanyPasswordLogic

class ChangeCompanyPassword(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Change company password')
        self.setGeometry(0, 0, 600, 450)

        self.widget = self

        self.setupUI()

    def clear(self):
        self.passwort.setText('')
        self.new_passwort.setText('')

    def changePassword(self):
        ChangeCompanyPasswordLogic.changePasswordFinal(self.firma, self.passwort.text(), self.new_passwort.text(), self)

    def addItemsToCompany(self):
        ChangeCompanyPasswordLogic.addItems(self.firma)

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Change company password')
        title.setFont(QFont('Montserrat', 30))

        firmen_note = QLabel(parent=self, text='Company: ')
        self.firma = QComboBox(parent=self)
        self.addItemsToCompany()

        passwort_note = QLabel(parent=self, text='Old password: ')
        self.passwort = QLineEdit(parent=self)
        self.passwort.setEchoMode(QLineEdit.Password)
        self.passwort.returnPressed.connect(self.changePassword)

        new_passwort_note = QLabel(parent=self, text='New password: ')
        self.new_passwort = QLineEdit(parent=self)
        self.new_passwort.setEchoMode(QLineEdit.Password)
        self.new_passwort.returnPressed.connect(self.changePassword)

        submit = QPushButton(parent=self, text='Change')
        submit.clicked.connect(self.changePassword)

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(firmen_note, 2, 0, Qt.AlignLeft)
        self.layout.addWidget(self.firma, 2, 1, Qt.AlignRight)

        self.layout.addWidget(passwort_note, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.passwort, 3, 1, Qt.AlignRight)

        self.layout.addWidget(new_passwort_note, 4, 0, Qt.AlignLeft)
        self.layout.addWidget(self.new_passwort, 4, 1, Qt.AlignRight)

        self.layout.addWidget(submit, 5, 0, 1, 0, Qt.AlignCenter)