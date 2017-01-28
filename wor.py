import sys

from PyQt5 import  QtCore,QtGui,QtWidgets,uic
from PyQt5.QtWidgets import  QApplication



import serial,random
import time
import multiprocessing

form_class, QMainWindow = uic.loadUiType("gui.ui")
import os_project,wi
from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE

#ser = serial.Serial('com3',9600)
global p


class ddisplay(QMainWindow, form_class):
    c=0
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.entry)
        self.pushButton_4.clicked.connect(self.kille)
        self.pushButton_3.clicked.connect(self.bluethooth)
        
        
    def entry(self):
        os_project.mouse()
    def kille(self):
        wi.killer_bee()
    def bluethooth(self):
        os_project.blue()
  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dv = ddisplay()
    dv.show()
    app.exec_()

