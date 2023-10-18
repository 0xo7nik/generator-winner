from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout 
from random import randint


def generator():
    text.setText('Победитель:')
    winner.setNum(randint(1, 100))
  
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Определитель победителя')
main_win.resize(500, 250)

button = QPushButton('Сгенерировать')
text = QLabel('Нажми, чтобы узнать победителя')
winner = QLabel('?')
line = QVBoxLayout()

button.clicked.connect(generator)
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)

main_win.setLayout(line)
main_win.show()
app.exec_()
