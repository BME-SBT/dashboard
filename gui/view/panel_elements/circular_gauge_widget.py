from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel 
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter, QColor, QPen, QFont


from gui.view.panel_elements.abstract_panel_elements.abstract_gauge_widget import AbstractGaugeWidget

class CircularGaugeWidget(AbstractGaugeWidget):
    def __init__(self, height, width,  tresholds, colors, unit):
        super().__init__(height, width,  tresholds, colors, unit)

        self.padding = 20
        self.value = 70

        #todo
        min_label = QLabel("10")
        max_label = QLabel("100")

        self.canvas_label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(width, height)
        canvas.fill(Qt.GlobalColor.transparent)
        self.canvas_label.setPixmap(canvas)


        main_layout = QVBoxLayout(self)
        self.normalize_value = 260 / (tresholds[-1] - tresholds[0])
        # main_layout.addWidget(max_label)
        main_layout.addWidget(self.canvas_label)
        # main_layout.addWidget(min_label)
        
        self.draw_gauge()
 
    def sensor_state_changed(self, state):
        raise NotImplementedError('sensor_state_changed must be implemented!')

    def sensor_value_changed(self, value):
        self.value = value
        self.update()
    
    def draw_gauge(self):
        canvas = self.canvas_label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(20)
        pen.setCapStyle(Qt.PenCapStyle.FlatCap)
        painter.setPen(pen)
        painter.setRenderHint(QPainter.Antialiasing, True)
        strat_arc = 140
        x = self.padding
        y = self.padding
        width = self.canvas_width - 2 * self.padding
        height = self.canvas_height - 2 * self.padding
        for i in range (0, len(self.tresholds) - 1):
            arc_start = 16 * ((self.tresholds[i] - self.tresholds[0]) * self.normalize_value + strat_arc)
            arc_span = - 16 * (self.tresholds[i + 1] - self.tresholds[i]) * self.normalize_value
            print(self.colors[i].value)
            pen.setColor(self.colors[i].value)
            painter.setPen(pen)
            painter.drawArc(QRect(x, y, width, height), -arc_start, arc_span)

        text_pen = QtGui.QPen()
        text_pen.setWidth(30)
        text_pen.setCapStyle(Qt.PenCapStyle.FlatCap)
        painter.setFont(QFont('Arial', self.canvas_height / 12))
        painter.setPen(text_pen)

        painter.drawText(QRect(0,y,self.canvas_width,height), Qt.AlignLeft|Qt.AlignBottom, str(self.tresholds[0]))
        painter.drawText(QRect(0, y,self.canvas_width,height), Qt.AlignRight|Qt.AlignBottom, str(self.tresholds[-1]))
        painter.end()
        self.canvas_label.setPixmap(canvas)

    def paintEvent(self, event):
        canvas = self.canvas_label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(30)
        pen.setCapStyle(Qt.PenCapStyle.FlatCap)
        painter.setPen(pen)
        #  todo miert nem mukodik
        painter.setRenderHints( QtGui.QPainter.Antialiasing )        
        strat_arc = 140
        x = self.padding
        y = self.padding
        width = self.canvas_width - 2 * self.padding
        height = self.canvas_height - 2 * self.padding
        arc_start = 16 * ((self.value - self.tresholds[0]) * self.normalize_value + strat_arc)
        arc_span = - 16 * 5
        # painter.drawArc(x, y, width, height, -arc_start, arc_span)  
        painter.drawArc(QRect(x, y, width, height), -arc_start, arc_span)  

        text_pen = QtGui.QPen()
        text_pen.setWidth(30)
        text_pen.setCapStyle(Qt.PenCapStyle.FlatCap)
        painter.setFont(QFont('Arial', self.canvas_height / 5))
        painter.setPen(text_pen)
        painter.drawText(QRect(0,0,self.canvas_width,self.canvas_height), Qt.AlignCenter|Qt.AlignCenter, str(self.value))
        
        painter.end()
        self.canvas_label.setPixmap(canvas)
       
    
