from PySide2.QtWidgets import QLabel, QVBoxLayout, QWidget
from PySide2.QtCore import QSize, QRect

from data.sensor import SensorState
from gui.view.panel_elements.abstract_panel_elements.abstract_panel_element import AbstractPanelElement
from gui.view.panel_elements.circular_gauge_widget import CircularGaugeWidget
from gui.view.colors import Colors
from data.sensor_ids import SensorId


class PermanentBatteryCurrentWidget(AbstractPanelElement):
    # TODO implement custom design
    def __init__(self):
        super().__init__(title='CUR', sensor_id=SensorId.BATTERY_CURRENT.value)

        # Create main layout
        main_layout = QVBoxLayout(self)
        # self.setContentsMargins(0, 0, 0, 0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Panel name
        # name_label = QLabel(self.title)
        # main_layout.addWidget(name_label)

        # Panel value
        self.value_label = QLabel('0')
        # main_layout.addWidget(self.value_label)
        self.circular_gauge_widget = CircularGaugeWidget(100, 100, [-35, 0, 50, 150, 200], [Colors.BLUE, Colors.GREEN, Colors.ORANGE, Colors.RED], self.sensor.data_type.unit, self.title, 1)
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