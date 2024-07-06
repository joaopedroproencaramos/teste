from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)


from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    //função 7 precisa ser alterada
    def set_appear(self): 
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.hello_text = QLabel( txt_hello )
        self.instruction = QLabel( txt_instruction )
        self.button = QPushButton( txt_next )
        self.layout = QVBoxLayout()
        self.hello_text.addWidget(self.layout)
        self.instruction.addWidget(self.layout)
        self.button.addWidget(self.layout)
    def connects(self): 
        self.btn_next.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = TestWin()

app = QApplication([])
mw = MainWin()
app.exec_()

