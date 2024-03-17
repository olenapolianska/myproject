from PyQt5.QtWidgets import *
from googletrans import Translator

from setting import settings

app = QApplication([])

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

window = QWidget()
window.resize(500, 200)
language1 = QComboBox()
language2 = QComboBox()
translatebtn = QPushButton("Перекласти")
settingsbtn = QPushButton("налаштування")
languages = {
    "Українська": "uk",
    "Англійська": "en",
    'Африканська': 'af',
    'Арабська': 'ar',
    'Американська': 'hy',
    'Азербайджанська': 'az',
    'Болгарська': 'bg',
    'Китайська (спрощена)':'zh-cn',
    'Китайська (традиційна)':'zh-tw',
    'Есперанто': 'eo',
    'Естонська': 'et',
    'Фінська': 'fi',
    'Французька': 'fr',
    'Західно-фризька': 'fy',
    'Галісійська': 'gl',
    'Грузинська': 'ka',
    'Німецька': 'de',
    'Грецька': 'el',
    'Гуджараті': 'gu',
    'Гаїтянська': 'ht',
    'Хауса': 'ha',
    'Гавайська': 'haw',
    'Іврит': 'he',
    'Гінді': 'hi',
    'Угорська': 'hu',
    'Ісландська': 'is',
    'Ігбо': 'ig',
    'Індонезійська': 'id',
    'Ірландська': 'ga',
    'Італійська': 'it',
    'Японська': 'ja',
    'Каннада': 'kn',
    'Казахська': 'kk',
    'Корейська': 'ko',
    'Киргиська': 'ky',
    'Лаоська': 'lo',
    'Латинська': 'la',
    'Латиська': 'lv',
    'Македонська': 'mk',
    'Малайська': 'ms',
    'Монгольська': 'mn',
    'Непалі': 'ne',
    'Норвезька': 'no',
    'Перська': 'fa',
    'Польська': 'pl',
    'Португальська': 'pt',
    'Сербська': 'sr',
    'Словацька': 'sk',
    'Словенська': 'sl',
    'Сомалі': 'so',
    'Іспанська': 'es',
    'Суданська': 'su',
    'Шведська': 'sv',
    'Таджицька': 'tg',
    'Тайська': 'th',
    'Турецька': 'tr',
    'Узбецька': 'uz',
    "В'єтнамська": 'vi',


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
line.addWidget(settingsbtn)
line2.addWidget(text_ed1)
mainline.addWidget(translatebtn)
mainline.addWidget(text_ed2)

def translate():
    a = text_ed1.toPlainText()
    b = language1.currentText()
    c = language2.currentText()
    translator = Translator()
    a = translator.translate(a, dest=languages[c])

    text_ed2.setText(a.text)

def change():
    a = text_ed2.toPlainText()
    b = text_ed1.toPlainText()
    h = language1.currentText()
    d = language2.currentText()

    language1.setCurrentText(d)
    language2.setCurrentText(h)

    text_ed2.setText(b)
    text_ed1.setText(a)
settingsbtn.clicked.connect(settings)
changebtn.clicked.connect(change)
translatebtn.clicked.connect(translate)
window.setLayout(mainline)
window.show()
app.exec()

