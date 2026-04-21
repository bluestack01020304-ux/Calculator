import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

import Utility.Calculator as cal

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.calText = ''
        self.plug = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')
        self.setFixedSize(300, 400)

        layout = QVBoxLayout()

        self.display = QLineEdit()
        self.display.setFixedHeight(50)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFont(QFont('Arial', 20))
        self.display.setReadOnly(True)
        layout.addWidget(self.display)

        grid = QGridLayout()
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        pos = [(i, j) for i in range(4) for j in range(4)]

        for text, position in zip(buttons, pos):
            btn = QPushButton(text)
            btn.setFixedSize(60, 60)
            btn.setFont(QFont('Arial', 14))
            btn.clicked.connect(self.on_click)
            grid.addWidget(btn, *position)

        layout.addLayout(grid)
        self.setLayout(layout)
        self.show()

    def on_click(self):
        btn = self.sender()
        text = btn.text()

        if self.plug == True:
            self.calText = ''
            self.display.clear()
            self.plug = False

        if text == 'C':
            self.calText = ''
            self.display.clear()  
            self.plug = False
        elif text == '=': 
            result = cal.calcul(self.calText)
            self.display.setText(str(result))
            self.calText = str(result)
            self.plug = True
            pass
        else:
            # 변수 없이 직접 15글자 미만일 때만 텍스트를 추가하도록 수정했습니다.
            if len(self.calText) < 15:
                self.calText += text 
                self.display.setText(self.calText)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())