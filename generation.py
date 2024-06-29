import random

print("hello world")
from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()

winner_lbl = QLabel("Переможець")
generation_winner_bth = QPushButton("Отримати переможця")

main_line = QVBoxLayout()
main_line.addWidget(winner_lbl)
main_line.addWidget(generation_winner_bth)


def winner_func():
    num = random.randint(1,4)
    winner_lbl.setText("Переможець" + str(num))

generation_winner_bth.clicked.connect(winner_func)

window.setLayout(main_line)
window.show()
app.exec()