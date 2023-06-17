from PySide2.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel 
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt, QRect
from PySide2.QtGui import QPainter, QColor, QPen, QFont
from gui.view.colors import Colors
from data.sensor import SensorState


from gui.view.panel_elements.abstract_panel_elements.abstract_gauge_widget import AbstractGaugeWidget

class CircularGaugeWidget(AbstractGaugeWidget):
    def __init__(self, height, width,  tresholds, colors, unit, name):
        super().__init__(height, width,  tresholds, colors, unit, name)

        self.padding = 15
        self.value = 70
        self.min_value = tresholds[0]
        self.max_value = tresholds[-1]
        self.text_color = Colors.WHITE
        self.sensor_state = SensorState.NORMAL
        self.canvas_height = height
        self.normalize_value = 260 / (tresholds[-1] - tresholds[0])


        self.canvas_label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(self.canvas_width, self.canvas_height)
        canvas.fill(Qt.GlobalColor.transparent)
        self.canvas_label.setPixmap(canvas)
        # self.canvas_pointer_label = QtWidgets.QLabel()
        # canvas = QtGui.QPixmap(self.canvas_width, self.canvas_height)
        # canvas.fill(Qt.GlobalColor.transparent)
        # self.canvas_pointer_label.setPixmap(canvas)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.canvas_label)
        # main_layout.addWidget(self.canvas_pointer_label)
        
        self.draw_gauge()
 
    def sensor_state_changed(self, state: SensorState):
        if(state == SensorState.MISSING_DATA):
            self.text_color = Colors.RED
        elif(state == SensorState.NO_DATA):
            self.text_color = Colors.GREY
        else:
            self.text_color = Colors.WHITE
        self.update()

    def sensor_value_changed(self, value):
        if(value):
            self.value = value
            self.update()
    
    def draw_gauge(self):
        canvas = self.canvas_label.pixmap()
        canvas.fill(Qt.GlobalColor.transparent)
        painter = QtGui.QPainter(canvas)
        # painter.begin(canvas)
        # painter = QtGui.QPainter(self.canvas_label.pixmap())        
        pen = QtGui.QPen(self.text_color.value)
        pen.setWidth(20)
        pen.setCapStyle(Qt.PenCapStyle.FlatCap)
        painter.setPen(pen)
        painter.setRenderHint(QPainter.Antialiasing, True)

        strat_arc = 140
        x = self.padding
        y = self.padding
        width = self.canvas_width - (2 * self.padding)
        height = self.canvas_width - (2 * self.padding)
        for i in range (0, len(self.tresholds) - 1):
            arc_start = 16 * ((self.tresholds[i] - self.tresholds[0]) * self.normalize_value + strat_arc)
            arc_span = - 16 * (self.tresholds[i + 1] - self.tresholds[i]) * self.normalize_value
            pen.setColor(self.normal_colors[i].value)
            painter.setPen(pen)
            painter.drawArc(QRect(x, y, width, height), -arc_start, arc_span)
        pen = QtGui.QPen(self.text_color.value)
        painter.setPen(pen)
        painter.setFont(QFont('Arial', 8))
        painter.drawText(QRect(x/2, y, self.canvas_width - self.padding, self.canvas_height *0.8), Qt.AlignLeft|Qt.AlignBottom, str(self.tresholds[0]))
        painter.drawText(QRect(x/2, y, self.canvas_width - self.padding, self.canvas_height * 0.8), Qt.AlignRight|Qt.AlignBottom, str(self.tresholds[-1]))
        painter.setFont(QFont('Arial', 8))
        painter.drawText(QRect(0, y, self.canvas_width, self.canvas_height- 2 * self.padding), Qt.AlignHCenter|Qt.AlignBottom, self.name)
        self.canvas_label.setPixmap(canvas)
        painter.end()

    def draw_pointer(self, value):
        canvas = self.canvas_label.pixmap()
        # canvas = QtGui.QPixmap(self.canvas_width, self.canvas_height)
        painter = QtGui.QPainter(canvas)
        
        # qp.setPen(QColor(168, 34, 3))
        # qp.setFont(QFont('Decorative', 10))
        # qp.drawText(event.rect(), Qt.Alignment.AlignCenter, "szoveg")
        # qp.end()
        pointer_value = self.value
        if(self.value < self.min_value):
            pointer_value = self.min_value
        if(self.value > self.max_value):
            pointer_value = self.max_value
        # painter = QtGui.QPainter(self.canvas_label.pixmap())
        # painter.begin(self)
        pen = QtGui.QPen(self.text_color.value)


        pen.setWidth(30)
        pen.setCapStyle(Qt.PenCapStyle.FlatCap)
        painter.setPen(pen)
        #  todo miert nem mukodik
        painter.setRenderHints( QtGui.QPainter.Antialiasing )   
        # painter.fillRect(QRect(0, 0, self.canvas_width, self.canvas_height), Colors.BLACK.value)   
        strat_arc = 140
        x = self.padding
        y = self.padding
        width = self.canvas_width - (2 * self.padding)
        height = self.canvas_width - (2 * self.padding)
        arc_start = 16 * ((pointer_value - self.tresholds[0]) * self.normalize_value + strat_arc)
        arc_span = - 16 * 5
        # painter.drawArc(x, y, width, height, -arc_start, arc_span)  
        # painter.begin(self)
        painter.drawArc(QRect(x, y, width, height), -arc_start, arc_span)  

        painter.setFont(QFont('Arial', self.canvas_height / 5))
        painter.drawText(QRect(0,0,self.canvas_width,self.canvas_height), Qt.AlignCenter, str(self.value))
        painter.drawPixmap(QtCore.QPoint(), canvas)
        painter.end()

        # self.canvas_label.clear()   
        self.canvas_label.setPixmap(canvas)   

               

    def paintEvent(self, event):
       self.draw_gauge()
       self.draw_pointer(self.value)