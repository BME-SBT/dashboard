from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QColor
from gui.view.colors import Colors
from data.sensor import SensorState


class AbstractGaugeWidget(QWidget):
    def __init__(self, height, width, tresholds, colors, unit, title, rounding):
        super().__init__()
        self.tresholds = tresholds
        self.normal_colors = []
        for c in colors:
            self.normal_colors.append(c.value)
        self.canvas_width = width
        self.canvas_height = height
        self.unit = unit
        self.title = title
        self.gray_colors = []
        self.red_colors = []
        self.set_gray_colors()
        self.set_red_colors()
        self.colors = self.gray_colors
        self.text_color = Colors.LIGHT_GREY
        self.state =  SensorState.NO_DATA
        self.value = None
        self.rounding = rounding

        
        self.setContentsMargins(0, 0, 0, 0)
 
    def sensor_state_changed(self, state):
        raise NotImplementedError('sensor_state_changed must be implemented!')

    def sensor_state_changed(self, value):
        raise NotImplementedError('sensor_state_changed must be implemented!')
    
    def draw_gauge(self):
        raise NotImplementedError('draw_gauge must be implemented!')

    def draw_pointer(self, value):
        raise NotImplementedError('draw_pointer must be implemented!')
       
    def set_gray_colors(self):
        num_of_tresholds = len(self.tresholds) - 1
        color = 200
        color_dif = round(180 / num_of_tresholds)
        for i in range (0, num_of_tresholds):
            self.gray_colors.append(QColor(color - i* color_dif, color - i* color_dif, color - i* color_dif))

    def set_red_colors(self):
        num_of_tresholds = len(self.tresholds) - 1
        color = 200
        color_dif = round(150 / num_of_tresholds)
        for i in range (0, num_of_tresholds):
            self.red_colors.append(QColor(255, color - i* color_dif, color - i* color_dif))

    
