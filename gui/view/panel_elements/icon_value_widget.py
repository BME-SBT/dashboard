from PySide2.QtWidgets import QLabel, QHBoxLayout, QWidget

from data.sensor import SensorState
from gui.view.panel_elements.abstract_panel_elements.abstract_panel_element import AbstractPanelElement

class IconValueWidget(AbstractPanelElement):
    # TODO implement custom design
    def __init__(self, title, sensor_id, unit):
        super().__init__(title, sensor_id)
        self.unit = unit

        # Create main layout
        main_layout = QHBoxLayout(self)

        # Panel name
        name_label = QLabel(self.title + ": ")
        main_layout.addWidget(name_label)
        
        # Panel value
        self.value_label = QLabel('1')
        main_layout.addWidget(self.value_label)

        # Panel Unit
        self.value_unit = QLabel(self.unit)
        main_layout.addWidget(self.value_label)

    def sensor_state_changed(self, state, old_state):
        if state == SensorState.MISSING_DATA:
            self.value_label.setStyleSheet("color: red")
            # TODO (dani) replace setStyleSheet to setProperty
            self.value_label.setText(self.value_label.text() + " - NO DATA")
        else:
            self.value_label.setStyleSheet("color: black")

    def sensor_value_changed(self, value, old_value):
        self.value_label.setText(f"{value} {self.sensor.data_type.unit}")
