from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

application = QApplication(['Button ni harakatlantirish'])
application.setFont(QFont('Ubuntu', 25))
win = QMainWindow()
win.setGeometry(300, 300, 700, 700)
def setBtn(btn, val, x, y, chx, chy):
    btn.setText(val)
    btn.move(x, y)
    btn.setFont(QFont('Ubuntu', 50))
    btn.adjustSize()
    btn.clicked.connect(lambda: MainBtn.move(MainBtn.x()+chx,MainBtn.y()+chy))
posX, posY, step = 250, 250, 5
MainBtn = QPushButton(win)
setBtn(MainBtn, '👻', posX, posY, 0, 0)
btn1 = QPushButton(win)
setBtn(btn1, "←", 120, 600, -step, 0)
btn2 = QPushButton(win)
setBtn(btn2, "↓", 210, 600, 0, step)
btn3 = QPushButton(win)
setBtn(btn3, "→", 300, 600, step, 0)
btn4 = QPushButton(win)
setBtn(btn4, "↑", 210, 510, 0, -step)
win.show()
application.exec()