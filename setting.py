from PyQt5.QtWidgets import *
app = QApplication([])
def settings():

    window = QDialog()

    tema = QLabel("Тема")
    group1= QButtonGroup()
    tema1 = QRadioButton("тема1")
    tema2 = QRadioButton("тема2")
    tema3 = QRadioButton("тема3")
    tema4 = QRadioButton("тема4")
    tema5 = QRadioButton("тема5")
    tema6 = QRadioButton("тема6")
    group1.addButton(tema1)


    text = QLabel("Шрифт")
    group2 = QButtonGroup()
    text1 = QRadioButton("шрифт1")
    text2 = QRadioButton("шрифт2")
    text3 = QRadioButton("шрифт3")
    text4 = QRadioButton("шрифт4")
    text5 = QRadioButton("шрифт5")
    text6 = QRadioButton("шрифт6")
    group2.addButton(text1)
    mainline = QVBoxLayout()
    line1 = QHBoxLayout()
    line2 = QHBoxLayout()
    mainline.addWidget(tema)
    mainline.addLayout(line1)
    mainline.addLayout(line2)
    line1.addWidget(tema1)
    line1.addWidget(tema2)
    line1.addWidget(tema3)
    line2.addWidget(tema4)
    line2.addWidget(tema5)
    line2.addWidget(tema6)
    mainline.addWidget(text)
    line3 = QHBoxLayout()
    line4 = QHBoxLayout()
    mainline.addLayout(line3)
    mainline.addLayout(line4)
    line3.addWidget(text1)
    line3.addWidget(text2)
    line3.addWidget(text3)
    line4.addWidget(text4)
    line4.addWidget(text5)
    line4.addWidget(text6)




    window.setLayout(mainline)
    window.show()
    window.exec()