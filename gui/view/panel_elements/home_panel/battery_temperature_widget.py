from PySide2.QtWidgets import QLabel, QVBoxLayout

from data.sensor import SensorState
from gui.view.panel_elements.abstract_panel_elements.abstract_panel_element import AbstractPanelElement
from gui.view.panel_elements.bar_widget import BarWidget
from gui.view.colors import Colors
from data.sensor_ids import SensorId


class BatteryTemperatureWidget(AbstractPanelElement):
    def __init__(self):
        super().__init__(title='B.TMP', sensor_id=SensorId.BATTERY_TEMPERATURE_1_2_3.value)

        # Create main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Panel
        self.bar_widget = BarWidget(70, 300, [-10, 0, 40, 65, 85], [Colors.BLUE, Colors.GREEN, Colors.ORANGE, Colors.RED], self.sensor.data_type.unit, self.title, False, 1)
        main_layout.addWidget(self.bar_widget)

    def sensor_state_changed(self, state, old_state):
        self.bar_widget.sensor_state_changed(state)
        # if state == SensorState.MISSING_DATA:
        #     self.value_label.setStyleSheet("color: red")
        #     # TODO (dani) replace setStyleSheet to setProperty
        #     self.value_label.setText(self.value_label.text() + " - NO DATA")
        # else:
        #     self.value_label.setStyleSheet("color: black")

    def sensor_value_changed(self, value, old_value):
       self.bar_widget.sensor_value_changed(value)
