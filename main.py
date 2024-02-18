from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
window.resize(500, 200)
language1 = QComboBox()
language2 = QComboBox()
translatebtn = QPushButton("Перекласти")
language1.addItems(['Українська', 'Англійська', 'Французька'])
language2.addItems(['Англійська', 'Французька', 'Українська'])
text_ed1 = QTextEdit()
text_ed1.setPlaceholderText('Введіть текст...')
text_ed2 = QTextEdit()
text_ed2.setPlaceholderText('Переклад...')
changebtn = QPushButton("")

mainline = QVBoxLayout()
line = QHBoxLayout()
line2 = QHBoxLayout()
mainline.addLayout(line)
mainline.addLayout(line2)
line.addWidget(language1)
line.addWidget(changebtn)
line.addWidget(language2)
line2.addWidget(text_ed1)
mainline.addWidget(translatebtn)
mainline.addWidget(text_ed2)

def translate():
    a = text_ed1.toPlainText()
    a = a.upper()
    text_ed2.setText(a)

def change():
    a = text_ed2.toPlainText()
    b = text_ed1.toPlainText()

    text_ed2.setText(b)
    text_ed1.setText(a)

changebtn.clicked.connect(change)
translatebtn.clicked.connect(translate)
window.setLayout(mainline)
window.show()
app.exec()

