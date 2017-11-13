#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import turtle
import sys
from PySide.QtCore import *
from PySide.QtGui import *

class TurtleControl(QWidget):
    def __init__(self,turtle):
        super(TurtleControl,self).__init__()
        self.turtle = turtle
        
        self.left_btn = QPushButton("Left",self )
        self.right_bt = QPushButton("Right",self)
        self.move_btn = QPushButton("move",self)

        self.controlsLayout = QGridLayout()
        self.controlsLayout.addWidget(self.left_btn,0,0)
        self.controlsLayout.addWidget(self.right_btn,0,1)
        self.controlsLayout.addWidget(self.distance_spin,1,0)
        self.controlsLayout.addWidget(self.move_btn,1,1)
        self.setLayout(self.controlsLayout)

        self.distance_spin.setRange(0,100)
        self.distance_spin.setSingleStep(5)
        self.distance_spin.setValue(20)

#set up turtle
window = turtle.Screen()
babbage = turtle.Turtle()

#Create a Qt application
app = QApplication(sys.argv)
control_window = TurtleControl(babbage)
control_window.show()

#Enter Qt application main loop
app.exec_()
sys.exit()
