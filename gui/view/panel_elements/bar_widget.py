from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

from gui.view.panel_elements.abstract_panel_elements.abstract_gauge_widget import AbstractGaugeWidget

class BarWidget(AbstractGaugeWidget):
    def __init__(self, height, width,  tresholds, colors, isVertical):
        super().__init__(height, width,  tresholds, colors)

        self.isVertical = isVertical
        self.padding = 10
        self.value = 0

        #todo
        min_label = QLabel("10")
        max_label = QLabel("100")

        self.canvas_label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(width, height)
        canvas.fill(Qt.GlobalColor.transparent)
        self.canvas_label.setPixmap(canvas)

        # Create main layout
        if self.isVertical:
            main_layout = QVBoxLayout(self)
            self.normalize_value = (self.canvas_height - 2 * self.padding) / (tresholds[-1] - tresholds[0])
            main_layout.addWidget(max_label)
            main_layout.addWidget(self.canvas_label)
            main_layout.addWidget(min_label)

        else:
            main_layout = QHBoxLayout(self)
            self.normalize_value = (self.canvas_width - 2 * self.padding) / (tresholds[-1] - tresholds[0])
            main_layout.addWidget(min_label)
            main_layout.addWidget(self.canvas_label)
            main_layout.addWidget(max_label)

      

   

        

        
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
        pen.setWidth(1)
        painter.setPen(pen)
        painter.scale(1, -1)

        # mirror the graphicsview around the y-axis.
        if self.isVertical:
            x = self.padding
            width = 30
            for i in range (0, len(self.tresholds) - 1):
                y = self.normalize_value * (self.tresholds[i] - self.tresholds[0]) + self.padding - self.canvas_height
                height = self.normalize_value * (self.tresholds[i + 1] - self.tresholds[i])
                color = self.colors[i]
                painter.drawRect(x, y, width, height)
            #painter.fillRect(x, y, width, height, color)

        else:
            y = self.padding
            height = 30
            painter.scale(1, -1)
            for i in range (0, len(self.tresholds) - 1):
                x = self.normalize_value * (self.tresholds[i] - self.tresholds[0]) 
                width = self.normalize_value * (self.tresholds[i + 1] - self.tresholds[i]) 
                color = self.colors[i]
                painter.drawRect(x, y, width, height)
        
        painter.end()
        self.canvas_label.setPixmap(canvas)

    def paintEvent(self, event):
        canvas = self.canvas_label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(1)
        painter.setPen(pen)
        # mirror the graphicsview around the y-axis.
        if self.isVertical:
            painter.scale(1, -1)
            x = 0
            y = self.normalize_value * self.value - self.canvas_height
            width = 50
            height = 5
            # color = self.colors[i]
            painter.drawRect(x, y, width, height)
            # painter.fillRect(x, y, width, height, color)
        else:
            x = self.normalize_value * self.value
            y = 0
            width = 5
            height = 50
            # color = self.colors[i]
            painter.drawRect(x, y, width, height)
            # painter.fillRect(x, y, width, height, color)

        
        
        painter.end()
        self.canvas_label.setPixmap(canvas)
       
    
