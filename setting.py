
from PyQt5.QtWidgets import *

from settheme import app


def settings():

    window = QDialog()

    settheme = []
    tema = QLabel("Тема")
    group1= QButtonGroup()
    tema1 = QRadioButton("")
    tema2 = QRadioButton("тема2")
    tema3 = QRadioButton("тема3")
    tema4 = QRadioButton("тема4")
    tema5 = QRadioButton("тема5")
    tema6 = QRadioButton("тема6")
    group1.addButton(tema1)
    group1.addButton(tema2)
    group1.addButton(tema3)
    group1.addButton(tema4)
    group1.addButton(tema5)
    group1.addButton(tema6)




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
    line3 = QHBoxLayout()
    line4 = QHBoxLayout()
    mainline.addLayout(line3)
    mainline.addLayout(line4)

    def settheme1():
        app.setStyleSheet("""
                QWidget {
                    background: #EFEFEF;
                    font-size: 15px;
                    font-family:Courier New;
                    color: #848484;
                    border-style: solide;
                    border-width: 2px;
                    border-color:#B5B5B5
                    border-radius: 5px;
                }
                QPushButton {
                    background: #FF9F9F;
                }
                QRadioButton {
                    background: #FF9F9F;
                   
                }
                QComboBox {
                    background: #9B9B9B;
                    color: maroon;
                    border-color: crimson;
                }
                """)

    def settheme2():
        app.setStyleSheet("""
               QWidget {
                    background: #FF8181;
                    font-size: 15px;
                    font-family:Courier New;
                    color: maroon;
                    border-style: ridge;
                    border-width: 2px;
                    border-color:indianred;
                    
               }
               QPushButton {
                    background: #FD7676;
                    border-color: crimson;
               }
               QRadioButton {
                    background: #FD7676;
                    border-color: crimson;
               }
               QComboBox {
                    background: #FF6161;
                    color: maroon;
                    border-color: #A52A2A;
               }
               """)


    def settheme3():
        app.setStyleSheet("""
                QWidget {
                    background: #DAE2FF;
                    font-size: 15px;
                    font-family: Courier New;
                    color: teal;
                    border-style: outset;
                    border-width: 2px;
                    border-color: cornflowerblue;
                    border-radius: 5px;
                }
                QPushButton {
                    background: #BDCBFF;

                }
                QComboBox {
                    background: #7692FF;
                    color: midnightblue;
                    border-style: outset;
                    border-color: royalblue;
                }
                """)

    def settheme4 ():
        app.setStyleSheet("""
                QWidget {
                    background: #FDFFAB;
                    font-size: 15px;
                    font-family: Courier New;
                    color: Dark yellow1;
                    border-style: inset;
                    border-width: 2px;
                    border-color: #CCCC00;
                    border-radius: 5px;
                }
                QPushButton {
                    background: #FFEC8A;
                    border-color: #999900;
                    color: #666600;
                }
                QComboBox {
                    background: #FFEA5A;
                    color: Dark yellow1;
                    border-color: #999900;
                }
                """)

    def settheme5():
        app.setStyleSheet("""
                QWidget {
                    background:#C7FFAB;
                    font-size:15px;
                    font-family:Courier New;
                    color:limegreen;
                    border-style:groove;
                    border-width:3px;
                    border-color:lime;
                    
                }
                QPushButton {
                    background:#98FF7F;
                    border-color:limegreen;
                    color:forestgreen;
               }
                QRadioButton {
                    background:#98FF7F;
                    border-color:limegreen;
                    color:forestgreen;
                }
                QComboBox {
                    background:#29FF4D;
                    color:darkgreen;
                    border-color:#00CC00;
                }
                """)

    def settheme6():
        app.setStyleSheet("""
                QWidget {
                    background:#D5CAFF;
                    font-size:15px;
                    font-family:Courier New;
                    color:#8C69FF;
                    border-style:double;
                    border-width:2px;
                    border-color:#A88DFF;
                    border-radius: 5px;

                }
                QPushButton {
                    background:#C9B9FF;
                    border-color:#8C69FF;
                    color:#552BFF;
                    border-radius: 2px;
                }
                QRadioButton {
                    background:#C9B9FF;
                    border-color:#8C69FF;
                    color:#552BFF;
                    border-radius: 2px;
                }
                QComboBox {
                    background:#B69FFF;
                    color:#4111FF;
                    border-color:#6841FF;
                    border-radius: 2px;
                }
                """)
    tema1.clicked.connect(settheme1)
    tema2.clicked.connect(settheme2)
    tema3.clicked.connect(settheme3)
    tema4.clicked.connect(settheme4)
    tema5.clicked.connect(settheme5)
    tema6.clicked.connect(settheme6)
    window.setLayout(mainline)
    window.show()
    window.exec()