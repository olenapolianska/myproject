from PyQt5.QtWidgets import *

app = QApplication([])

app.setStyleSheet("""
        QWidget {
            background: #B6FFD6;
        }
        """)

window = QWidget()
window.resize(500, 200)
language1 = QComboBox()
language2 = QComboBox()
translatebtn = QPushButton("Перекласти")
languages = {
    "Українська": "uk",
    "Англійська": "en",
    "Француька": "fr"

}
language1.addItems(languages)
language2.addItems(languages)
text_ed1 = QTextEdit()
text_ed1.setPlaceholderText('Введіть текст...')
text_ed2 = QTextEdit()
text_ed2.setPlaceholderText('Переклад...')
changebtn = QPushButton("<>")

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
    b = language1.currentText()

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

