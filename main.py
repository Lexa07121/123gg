import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        uic.loadUi("UI.ui, self")
        flag = False

    # Метод срабатывает, когда виджету надо
    # перерисовать свое содержимое,
    # например, при создании формы
    def paintEvent(self, event):
        if self.flag:
            # Создаем объект QPainter для рисования
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            self.draw_flag(qp)
            # Завершаем рисование
            qp.end()
            self.flag = False

    def draw_flag(self, qp):
        self.flag = True
        # Задаем кисть
        qp.setBrush(QColor(255, 255, 0))
        x,  y = randint(0, 230), randint(0, 160)
        d = randint(10, 30)
        # Рисуем прямоугольник заданной кистью
        qp.drawEllipse(x, y, d, d)
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())