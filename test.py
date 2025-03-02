import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QWidget,  QComboBox


class Client:
    def __init__(self, tel):
        self.name = None
        self.tel = tel
        self.adress = None
        self.istoriya = [f'sozdali akount dlya {tel}']
        self.balans = 0

    def changeName(self, name):
        self.name = name
        self.istoriya.append(f'pomenyal imya na {name}')

    def changeAdress(self, adress):
        self.adress = adress
        self.istoriya.append(f'pomenyal adress na {adress}')

    def changeBalans(self, balans):
        self.balans = balans
        self.istoriya.append(f'izmenil balans na {balans}')


class MBank:
    def __init__(self):
        self.klienti = {}
    
    def addKlient(self, tel):
        self.klienti[tel] = Client(tel)
    
    def perevod(self, otkogo, komu, summa):
        a = self.klienti[otkogo].balans
        b = self.klienti[komu].balans

        self.klienti[otkogo].changeBalans(a - summa)
        self.klienti[komu].changeBalans(b + summa)

    def pokajiIstoriyu(self):
        s = ''
        for k, v in self.klienti.items():
            s += k + '\n'
            for i in v.istoriya:
                s += i + '\n'
            s += '*'*20 + '\n'

        return s

b = MBank()
b.addKlient('0777')
b.addKlient('0555')
b.addKlient('0999')
b.addKlient('0666')

b.klienti['0777'].changeName('Aijan')
b.klienti['0777'].changeAdress('batken')
b.klienti['0777'].changeBalans(1000)
b.klienti['0999'].changeName('Aliya')
b.klienti['0999'].changeBalans(5000)

b.klienti['0666'].changeName('Aidar')
b.klienti['0666'].changeBalans(2000)

b.klienti['0555'].changeName('Timur')
b.klienti['0555'].changeBalans(8000)


b.perevod('0777', '0555', 100)
b.perevod('0555', '0666', 200)
b.perevod('0777', '0999', 500)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.v = QVBoxLayout()
        k = QLabel('Klient')
        self.otkogo = QComboBox()
        self.otkogo.addItems(['0777', '0555', '0999', '0666'])
        

        self.v.addWidget(k)
        self.v.addWidget(self.otkogo)

        self.istoria = QTextEdit()
        self.v.addWidget(self.istoria)
        self.button = QPushButton("Pokaji istoriyu")
        self.button.clicked.connect(self.pomenay)
        self.v.addWidget(self.button)

        widget = QWidget()
        widget.setLayout(self.v)
        self.setCentralWidget(widget)

    def pomenay(self):
        #b.klienti[self.otkogo.currentText()].istoria
        #self.button.setText(f'{self.otkogo.text()} perevyol {self.komu.text()} dengi')
        x = '\n'.join(b.klienti[self.otkogo.currentText()].istoriya)
        self.istoria.setText(x)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
