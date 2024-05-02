# CON IL MODULO TKINTER
# from tkinter import *
#
# ___________________________________________________________________________________________
# CON IL MODULO KIVY

# ___________________________________________________________________________________________
# CON IL MODULO WxPython


# ___________________________________________________________________________________________
# CON IL MODULO PyGUI


# ___________________________________________________________________________________________
# CON IL MODULO PYQT

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

# def window():
# 	app = QApplication(sys.argv)
# 	w = QWidget()
# 	b = QLabel(w)
# 	b.setText("Hello World!")
# 	w.setGeometry(100,100,200,50)
# 	b.move(50,20)
# 	w.setWindowTitle("PyQt")
# 	w.show()
# 	sys.exit(app.exec_())
#
# if __name__ == '__main__':
# 	window()
#
#
#
# # oppure soluzioni con tasti...
from PyQt5.QtWidgets import QApplication, QWidget, 	QPushButton, QVBoxLayout

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec()
# #
#
# from PyQt5.QtWidgets import QHBoxLayout
#
# Infine il concetto di layouts pyqt
# app = QApplication([])
# layout = QHBoxLayout()
# # Add widgets to the layout
# layout.addWidget(QPushButton("Left-Most"))
# layout.addWidget(QPushButton("Center"), 1)
# layout.addWidget(QPushButton("Right-Most"), 2)
# # Set the layout on the application's window
# self.setLayout(layout)
