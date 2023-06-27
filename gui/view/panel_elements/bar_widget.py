from PySide2.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt, QRect
from PySide2.QtGui import QPainter, QColor, QPen, QFont
import math

from gui.view.panel_elements.abstract_panel_elements.abstract_gauge_widget import AbstractGaugeWidget
from gui.view.colors import Colors
from data.sensor import SensorState

class BarWidget(AbstractGaugeWidget):
    refresh = QtCore.Signal()
    def __init__(self, height, width,  tresholds, colors, unit, name, isVertical):
        super().__init__(height, width,  tresholds, colors, unit, name)

        self.isVertical = isVertical
        self.padding = 5
        self.bar_width = 30
        self.value_text_height = self.bar_width
        self.value_text_width = 4 * self.padding + self.bar_width
        self.min_value = tresholds[0]
        self.max_value = tresholds[-1]

        self.canvas_label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(width, height)
        canvas.fill(Qt.GlobalColor.transparent)
        self.canvas_label.setPixmap(canvas)
        self.canvas_label.setContentsMargins(0, 0, 0, 0)

        # Create main layout
        if self.isVertical:
            main_layout = QVBoxLayout(self)
            self.normalize_value = (self.canvas_height - 3 * self.padding - 2 * self.value_text_height) / (self.max_value - self.min_value)
            main_layout.addWidget(self.canvas_label)

        else:
            main_layout = QHBoxLayout(self)
            self.normalize_value = (self.canvas_width - 3 * self.padding - self.value_text_width) / (self.max_value - self.min_value)
            main_layout.addWidget(self.canvas_label)
        
        self.refresh.connect(self.update)
        self.draw_gauge()
 
    def sensor_state_changed(self, state):
        if(state == SensorState.MISSING_DATA):
            self.text_color = Colors.RED
            self.colors = self.red_colors
        elif(state == SensorState.NO_DATA):
            self.text_color = Colors.LIGHT_GREY
            self.colors = self.gray_colors
        else:
            self.text_color = Colors.WHITE
            self.colors = self.normal_colors
        
        self.refresh.emit()

    def sensor_value_changed(self, value):
        if value is not None:
            self.value = value
            self.refresh.emit()
    
    def draw_gauge(self):
        canvas = self.canvas_label.pixmap()
        painter = QtGui.QPainter(canvas)
        canvas.fill(Qt.GlobalColor.transparent)
        pen = QtGui.QPen(self.text_color.value)
        pen.setWidth(1)
        pen.setCapStyle(Qt.PenCapStyle.FlatCap)
        text_width = 30
        text_height = 15
        painter.setFont(QFont('Arial', 8))
        painter.setPen(pen)
        painter.setRenderHint(QPainter.Antialiasing, True)

        # mirror the graphicsview around the y-axis.
        if self.isVertical:
            x = self.padding
            width = self.bar_width

            for i in range(len(self.tresholds) - 1, 0, -1):
                y = math.ceil(self.normalize_value * (self.tresholds[-1] - self.tresholds[i])) + self.padding
                height = math.ceil(self.normalize_value * abs(self.tresholds[i] - self.tresholds[i - 1]))
                color = self.colors[i - 1]
                # painter.drawRect(x, y, width, height)
                painter.fillRect(x, y, width, height, color)
                painter.drawText(QRect(self.padding + width + 5, y-text_height/2, text_width, text_height), Qt.AlignLeft|Qt.AlignVCenter, str(self.tresholds[i]))
            y = self.normalize_value * (self.tresholds[-1]  - self.tresholds[0]) + self.padding
            painter.drawText(QRect(self.padding + width + 5, y-text_height/2, text_width, text_height), Qt.AlignLeft|Qt.AlignVCenter, str(self.tresholds[0]))
            x = 0
            y = self.normalize_value * (self.tresholds[-1]  - self.tresholds[0]) + 2 * self.padding + self.value_text_height
            painter.drawText(QRect(x,y,self.value_text_width, self.value_text_height), Qt.AlignCenter, str(self.title))
            
        else:
            y = self.padding
            height = self.bar_width
            painter.scale(1, -1)
            painter.scale(1, -1)
            for i in range (0, len(self.tresholds) - 1):
                x = math.ceil(self.normalize_value * (self.tresholds[i] - self.tresholds[0])) + 2* self.padding + self.value_text_width
                width = math.ceil(self.normalize_value * (self.tresholds[i + 1] - self.tresholds[i])) 
                color = self.colors[i]
                # painter.drawRect(x, y, width, height)
                painter.fillRect(x, y, width, height, color)
                painter.drawText(QRect(x-text_width/2, y + height + 5, text_width, text_height), Qt.AlignHCenter|Qt.AlignTop, str(self.tresholds[i]))
            x = self.normalize_value * (self.tresholds[-1] - self.tresholds[0]) + 2 * self.padding + self.value_text_width
            painter.drawText(QRect(x-text_width/2 - 5, y + height + 5, text_width, text_height), Qt.AlignHCenter|Qt.AlignTop, str(self.tresholds[-1]))
            
            y = 2 * self.padding + self.bar_width + text_height
            x = 2 * self.padding + self.value_text_width
            # painter.drawText(QRect(x,y, 2* self.value_text_width, self.value_text_height), Qt.AlignCenter, str(self.name))
            painter.drawText(QRect(x,y, 2* self.value_text_width, self.value_text_height), Qt.AlignLeft|Qt.AlignTop, str(self.title))
        
        painter.end()
        self.canvas_label.setPixmap(canvas)

    def draw_pointer(self, event):    
        if self.value is None:
            return
        # ertek amit mutat a mutato
        pointer_value = self.value
        text_value = round(self.value)
        if(self.value < self.min_value):
            pointer_value = self.min_value
        if(self.value > self.max_value):
            pointer_value = self.max_value
        canvas = self.canvas_label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen(self.text_color.value)
        pen.setWidth(1)
        pen.setCapStyle(Qt.PenCapStyle.FlatCap)
        painter.setFont(QFont('Arial', 20))
        painter.setPen(pen)
        painter.setRenderHint(QPainter.Antialiasing, True)
        
        if self.isVertical:
            width = self.bar_width + 2 * self.padding
            height = 5
            x = 0
            y = self.normalize_value * (self.tresholds[-1] - pointer_value) - (height / 2) + self.padding
            # painter.drawRect(x, y, width, height)
            painter.fillRect(x, y, width, height, self.text_color.value)
            y = self.normalize_value * (self.tresholds[-1]  - self.tresholds[0]) + 2* self.padding
            painter.drawText(QRect(0,y,self.value_text_width, self.value_text_height), Qt.AlignCenter, str(text_value))
        else:
            width = 5
            height = self.bar_width + 2 * self.padding
            x = self.normalize_value * (pointer_value - self.tresholds[0]) - (width / 2) + 2 * self.padding + self.value_text_width
            y = 0
            # painter.drawRect(x, y, width, height)
            painter.scale(1, -1)
            painter.scale(1, -1)
            painter.fillRect(x, y, width, height, self.text_color.value)
            painter.drawText(QRect(0, self.padding, self.value_text_width, self.value_text_height), Qt.AlignCenter, str(text_value))
        painter.end()
        self.canvas_label.setPixmap(canvas)
    
    def paintEvent(self, event):
       self.draw_gauge()
       self.draw_pointer(self.value)