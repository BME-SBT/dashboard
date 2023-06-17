from PySide2.QtWidgets import QVBoxLayout, QLabel

from data.sensor import SensorState
from gui.view.panel_elements.abstract_panel_elements.abstract_panel_element import AbstractPanelElement
from gui.view.colors import Colors
from gui.view.panel_elements.circular_gauge_widget import CircularGaugeWidget


class PermanentMotorTemperatureWidget(AbstractPanelElement):
    # TODO implement custom design
    def __init__(self):
        super().__init__(title='Motor\nTemperature', sensor_id=0b00010110010)

        # Create main layout
        main_layout = QVBoxLayout(self)

        # Panel name
        # name_label = QLabel(self.title)
        # main_layout.addWidget(name_label)

        # Panel value
        self.value_label = QLabel('0')
        # main_layout.addWidget(self.value_label)
        self.circular_gauge_widget = CircularGaugeWidget(100, 100, [20, 65, 85, 110], [Colors.GREEN, Colors.ORANGE, Colors.RED], self.sensor.data_type.unit, 'Mot. Temp.')
        main_layout.addWidget(self.circular_gauge_widget)

    def sensor_state_changed(self, state, old_state):
        self.circular_gauge_widget.sensor_state_changed(state)
        if state == SensorState.MISSING_DATA:
            self.value_label.setStyleSheet("color: red")
            # TODO (dani) replace setStyleSheet to setProperty
            self.value_label.setText(self.value_label.text() + " - NO DATA")
        else:
            self.value_label.setStyleSheet("color: black")

    def sensor_value_changed(self, value, old_value):
        self.circular_gauge_widget.sensor_value_changed(value)
