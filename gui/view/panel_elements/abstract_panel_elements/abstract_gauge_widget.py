from PySide2.QtWidgets import QWidget

class AbstractGaugeWidget(QWidget):
    def __init__(self, height, width, tresholds, colors, unit, name):
        super().__init__()
        self.tresholds = tresholds
        self.normal_colors = colors
        self.canvas_width = width
        self.canvas_height = height
        self.unit = unit
        self.name = name
        self.grey_colors = []
        self.red_colors = []
 
    def sensor_state_changed(self, state):
        raise NotImplementedError('sensor_state_changed must be implemented!')

    def sensor_state_changed(self, value):
        raise NotImplementedError('sensor_state_changed must be implemented!')
    
    def draw_gauge(self):
        raise NotImplementedError('draw_gauge must be implemented!')

    def draw_pointer(self, value):
        raise NotImplementedError('draw_pointer must be implemented!')
       
    
