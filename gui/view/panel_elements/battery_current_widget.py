from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import QSize, QRect
from PySide6.QtGui import QPainter, QColor

from data.sensor import SensorState
from gui.view.panel_elements.abstract_panel_elements.abstract_panel_element import AbstractPanelElement
from gui.view.panel_elements.bar_widget import BarWidget


class BatteryCurrentWidget(AbstractPanelElement):
    # TODO implement custom design
    def __init__(self):
        super().__init__(title='Battery\nCurrent', sensor_id=0b01001010000)

        # Create main layout
        main_layout = QVBoxLayout(self)

        # Panel name
        name_label = QLabel(self.title)
        main_layout.addWidget(name_label)

        self.bar_widget = BarWidget(200, 100, [0, 20, 45, 70, 100], [QColor(200, 0, 0), QColor(255, 80, 0, 160), QColor(25, 0, 90, 200), QColor(200, 0, 0)], True)
 
        main_layout.addWidget(self.bar_widget)

        
        # Panel value
        self.value_label = QLabel('1')
        # main_layout.addWidget(self.value_label)
        self.sensor_value_changed(50, 40)
        self.sensor_value_changed(60, 50)
        self.sensor_value_changed(70, 60)


    def sensor_state_changed(self, state, old_state):
        if state == SensorState.MISSING_DATA:
            self.value_label.setStyleSheet("color: red")
            # TODO (dani) replace setStyleSheet to setProperty
            self.value_label.setText(self.value_label.text() + " - NO DATA")
        else:
            self.value_label.setStyleSheet("color: black")

    def sensor_value_changed(self, value, old_value):
        #todo sir
        #self.value_label.setText(f"{value} {self.sensor.data_type.unit}")
        self.bar_widget.sensor_value_changed(value)
