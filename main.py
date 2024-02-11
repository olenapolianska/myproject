from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
window.resize(500, 200)
language1 = QPushButton("Мова введення")
language2 = QPushButton("Мова перекладу")
text_ed1 = QTextEdit()
text_ed1.setPlaceholderText('Введіть текст...')

mainline = QVBoxLayout()
line = QHBoxLayout()
line2 = QHBoxLayout()
mainline.addLayout(line)
mainline.addLayout(line2)
line.addWidget(language1)
line.addWidget(language2)
line2.addWidget(text_ed1)


window.setLayout(mainline)
window.show()
app.exec()

