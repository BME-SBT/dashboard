from PySide6.QtWidgets import QVBoxLayout, QLabel

from data.sensor import SensorState
from gui.view.panel_elements.abstract_panel_elements.abstract_panel_element import AbstractPanelElement
from gui.view.panel_elements.circular_gauge_widget import CircularGaugeWidget
from gui.view.colors import Colors


class GPSSpeedWidget(AbstractPanelElement):
    # TODO implement custom design
    def __init__(self):
        super().__init__(title='GPSSpeed', sensor_id=0b10110010100)

        # Create main layout
        main_layout = QVBoxLayout(self)
        main_layout.addStretch()

        # Panel value
        self.value_label = QLabel('0')
        # main_layout.addWidget(self.value_label)
        self.circular_gauge = CircularGaugeWidget(160, 160, [0, 10, 15, 20, 25, 30], [Colors.GREEN, Colors.LIGHT_GREEN, Colors.YELLOW, Colors.ORANGE, Colors.RED], self.sensor.data_type.unit)
        main_layout.addWidget(self.circular_gauge)

        # Panel name
        name_label = QLabel(self.title)
        main_layout.addWidget(name_label)

    def sensor_state_changed(self, state, old_state):
        if state == SensorState.MISSING_DATA:
            self.value_label.setStyleSheet("color: red")
            # TODO (dani) replace setStyleSheet to setProperty
            self.value_label.setText(self.value_label.text() + " - NO DATA")
        else:
            self.value_label.setStyleSheet("color: black")

    def sensor_value_changed(self, value, old_value):
        # self.value_label.setText(f"{value} {self.sensor.data_type.unit}")
        self.circular_gauge.sensor_value_changed(value)
