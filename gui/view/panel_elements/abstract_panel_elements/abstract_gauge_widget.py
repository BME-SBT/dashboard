from PySide6.QtWidgets import QWidget

class AbstractGaugeWidget(QWidget):
    def __init__(self, height, width, tresholds, colors):
        super().__init__()
        self.tresholds = tresholds
        self.colors = colors
        self.canvas_width = width
        self.canvas_height = height
 
    def sensor_state_changed(self, state):
        raise NotImplementedError('sensor_state_changed must be implemented!')

    def sensor_state_changed(self, value):
        raise NotImplementedError('sensor_state_changed must be implemented!')
    
    def draw_gauge(self):
        raise NotImplementedError('draw_gauge must be implemented!')

    def draw_pointer(self, value):
        raise NotImplementedError('draw_pointer must be implemented!')
       
    
