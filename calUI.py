import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

import Utility.Calculator as cal

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.calText = ''
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

        if(text == "="): return
        self.calText += text #  clear 전에 처리해서 clear 전에 남아있음

        if text == 'C':
            self.display.clear()  # 화면만 지움, calText엔 "123+C"가 남아있음
        elif text == '=': # 위에서 이미 처리된 상태인지 확인
            # 여기는 친구가 만든 로직을 넣을 자리입니다.
            print(self.calText)
            pass
        else:
            self.display.setText(self.calText)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())

    