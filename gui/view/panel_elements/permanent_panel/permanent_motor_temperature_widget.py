from PySide2.QtWidgets import QVBoxLayout, QLabel

from data.sensor import SensorState
from gui.view.panel_elements.abstract_panel_elements.abstract_panel_element import AbstractPanelElement
from gui.view.colors import Colors
from gui.view.panel_elements.circular_gauge_widget import CircularGaugeWidget
from data.sensor_ids import SensorId

class PermanentMotorTemperatureWidget(AbstractPanelElement):
    def __init__(self):
        super().__init__(title='M.TMP', sensor_id=SensorId.MOTOR_TEMPERATURE.value)

        # Create main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Panel value
        self.circular_gauge_widget = CircularGaugeWidget(100, 100, [20, 65, 85, 110], [Colors.GREEN, Colors.ORANGE, Colors.RED], self.sensor.data_type.unit, self.title, 1)
        main_layout.addWidget(self.circular_gauge_widget)

    def sensor_state_changed(self, state, old_state):
        self.circular_gauge_widget.sensor_state_changed(state)
        # if state == SensorState.MISSING_DATA:
        #     self.value_label.setStyleSheet("color: red")
        #     # TODO (dani) replace setStyleSheet to setProperty
        #     self.value_label.setText(self.value_label.text() + " - NO DATA")
        # else:
        #     self.value_label.setStyleSheet("color: black")

    def sensor_value_changed(self, value, old_value):
        self.circular_gauge_widget.sensor_value_changed(value)
