import webbrowser

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                              QVBoxLayout, QHBoxLayout)

def get_barbi():
    return webbrowser.open('https://www.kinopoisk.ru/film/478052/?utm_referrer=www.google.com')

def get_random_film():
    if len(lst_film) > 0:
        url = lst_films[randint(0, len(lst_films)-1)]
        lst_films.remove(url)
    else:
        box = QMessageBox()
        box.setText('Фильмов больше/не осталось!!!')
        box.exec()

lts_films = [ #
    'https://hd.kinopoisk.ru/film/645fc42baa8048f58f0142eec0258a85?source=kinopoisk_kp_main&from_position=1'
    'https://hd.kinopoisk.ru/film/4155a88009824db685e260a1a611d17c?source=kinopoisk_kp_main&from_position=2'
    'https://hd.kinopoisk.ru/film/68f1690e67774eca994197bccfe08927?source=kinopoisk_kp_main&from_position=3'
    'https://hd.kinopoisk.ru/film/7ec2d8f9554241eba3ea4c9c5c9590b6?source=kinopoisk_kp_main&from_position=6'
] #    

def open_kinopoisk_url(url):
    return webbrowser.open(url)

app = QApplication([])

window = QWidget()
window.setFixedSize(400, 250) 
window.setWindowTitle('Кинопоиск')

text = QLabel('Выберите фильм:')
text.setStyleSheet("font-weight: bold; border:")

layout = QVBoxLayout()
layout_h1 = QHBoxLayout()
layout_h2 = QHBoxLayout()
layout_h3 = QHBoxLayout()

btn1 = QPushButton('Барби (2023)')
btn2 = QPushButton('Бойцовский Клуб (1993)')
btn3 = QPushButton('Интерстеллар (2014)')
btn4 = QPushButton('Драйв (2011)')
btn5 = QPushButton('Зеленая миля (1999)') 
btn6 = QPushButton('Титаник (1997)')

btn1.clicked.connect(lambda: open_kinopoisk_url('https://www.kinopoisk.ru/film/478052/?utm_referrer=www.google.com'))
btn2.clicked.connect(lambda: open_kinopoisk_url('https://www.kinopoisk.ru/film/361/'))
btn3.clicked.connect(lambda: open_kinopoisk_url('https://www.kinopoisk.ru/film/258687/'))
btn4.clicked.connect(lambda: open_kinopoisk_url('https://www.kinopoisk.ru/film/276598/'))
btn5.clicked.connect(lambda: open_kinopoisk_url('https://www.kinopoisk.ru/film/435/?utm_referrer=www.google'))
btn6.clicked.connect(lambda: open_kinopoisk_url('https://www.kinopoisk.ru/film/2213/'))

layout_h1.addWidget(btn1, alignment=Qt.AlignCenter)
layout_h1.addWidget(btn2, alignment=Qt.AlignCenter)
layout_h2.addWidget(btn3, alignment=Qt.AlignCenter)
layout_h2.addWidget(btn4, alignment=Qt.AlignCenter)
layout_h3.addWidget(btn5, alignment=Qt.AlignCenter)

layout.addWidget(text, alignment=Qt.AlignCenter)
layout.addLayout(layout_h1)
layout.addLayout(layout_h2)
layout.addLayout(layout_h3)

window.setStyleSheet("background-color: #5c4f4f;")

window.setLayout(layout)
window.show()
app.exec()