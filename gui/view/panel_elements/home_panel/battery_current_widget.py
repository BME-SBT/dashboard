from PySide2.QtWidgets import QLabel, QVBoxLayout, QWidget


from gui.view.colors import Colors
from data.sensor import SensorState
from gui.view.panel_elements.abstract_panel_elements.abstract_panel_element import AbstractPanelElement
from gui.view.panel_elements.bar_widget import BarWidget
from data.sensor_ids import SensorId


class BatteryCurrentWidget(AbstractPanelElement):
    # TODO implement custom design
    def __init__(self):
        super().__init__(title='CUR', sensor_id=SensorId.BATTERY_CURRENT.value)

        # Create main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Panel value
        self.bar_widget = BarWidget(250, 70, [-35, 0, 50, 150, 200], [Colors.BLUE, Colors.GREEN, Colors.ORANGE, Colors.RED], self.sensor.data_type.unit, self.title, True)
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
