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

        # 최대 글자 수 제한 설정
        max_length = 15

        if text == 'C':
            self.calText = ''
            self.display.clear()
        elif text == '=':
            # 친구분이 만든 calcul 함수를 호출하여 결과 반영
            try:
                result = cal.calcul(self.calText)
                self.display.setText(str(result))
                self.calText = str(result)
            except:
                self.display.setText("Error")
                self.calText = ""
        else:
            # 글자 수 제한: 현재 입력된 글자가 max_length보다 작을 때만 추가 허용
            if len(self.calText) < max_length:
                self.calText += text
                self.display.setText(self.calText)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())