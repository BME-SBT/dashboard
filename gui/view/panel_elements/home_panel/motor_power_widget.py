from PySide2.QtWidgets import QVBoxLayout, QLabel
from PySide2.QtGui import QPainter, QColor

from data.sensor import SensorState
from data.sensor_manager import SensorManager
from gui.view.panel_elements.abstract_panel_elements.abstract_panel_element import AbstractPanelElement
from gui.view.panel_elements.circular_gauge_widget import CircularGaugeWidget
from gui.view.colors import Colors
from data.sensor_ids import SensorId
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal


class MotorPowerWidget(QWidget):
    value_changed_signal = Signal(float, str)
    state_changed_signal = Signal(SensorState, SensorState)

    def __init__(self):
        super().__init__()

        self.setContentsMargins(0, 0, 0, 0)
        self.title = 'PWR2'
        # Create main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Panel value
        self.circular_gauge_widget = CircularGaugeWidget(120, 120, [0, 1, 4, 6],
                                                         [Colors.GREEN, Colors.ORANGE, Colors.RED], 'W', self.title, 1)
        main_layout.addWidget(self.circular_gauge_widget)

        self.current = 0
        self.voltage = 0

        self.current_sensor = SensorManager.get_sensor(SensorId.MOTOR_CONTROLLER_CURRENT.value)
        if self.current_sensor:
            self.current_sensor.add_qt_valuechange_handler(self)
            self.current_sensor.add_qt_statechange_handler(self)

        self.voltage_sensor = SensorManager.get_sensor(SensorId.BATTERY_VOLTAGE.value)
        if self.voltage_sensor:
            self.voltage_sensor.add_qt_valuechange_handler(self)
            self.voltage_sensor.add_qt_statechange_handler(self)

        self.value_changed_signal.connect(self.value_changed)
        self.state_changed_signal.connect(self.state_changed)

    def value_changed(self, value, name):
        if name == 'motor_controller_current':
            self.current = value
        elif name == 'battery_voltage':
            self.voltage = value
        watt = self.current * self.voltage

        if watt < 1000:
            self.circular_gauge_widget.sensor_value_changed(watt, watt / 1000)  # mW != W :D
            print(watt, watt / 1000)
        else:
            print(watt)
            self.circular_gauge_widget.sensor_value_changed(watt / 1000)

    def state_changed(self, state, oldstate):
        self.circular_gauge_widget.sensor_state_changed(state)
