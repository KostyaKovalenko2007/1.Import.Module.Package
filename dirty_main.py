from PyQt5.QtWidgets import *
from application import *
#from application.db import *
from datetime import date

if __name__ == '__main__':

    app = QApplication([])
    window = QWidget()
    window.setFixedWidth(300)
    text = QLabel()
    text.setText(f'{get_employees()} \n {calculate_salary()} \n {date.today()}')
    vbox = QVBoxLayout()
    vbox.addWidget(text)
    window.setLayout(vbox)
    window.setWindowTitle('HomeWork')
    window.show()
    app.exec_()