from PySide2.QtWidgets import QLabel, QHBoxLayout, QWidget
from PySide2.QtCore import Signal
from data.sensor import SensorState

from data.sensor_manager import SensorManager


class TextSensorWidget(QWidget):
    value_changed_signal = Signal(float, str)
    state_changed_signal = Signal(SensorState, SensorState)

    def __init__(self, title: str, sensor_id: int):
        super().__init__()

        # Create main layout
        main_layout = QHBoxLayout(self)

        # Panel name
        name_label = QLabel(title + ': ')
        main_layout.addWidget(name_label)

        # Panel value
        self.value_label = QLabel('-')
        main_layout.addWidget(self.value_label)
        main_layout.addStretch()

        sensor = SensorManager.get_sensor(sensor_id)
        if sensor:
            sensor.add_qt_valuechange_handler(self)
            self.value_changed_signal.connect(
                lambda s: self.value_label.setText(f"{s} {sensor.data_type.unit}"))
            self.state_changed_signal.connect(self.sensor_state_changed)
        else:
            self.value_label.setText('<invalid sensor>')

    def sensor_state_changed(self, state, oldstate):
        if state == SensorState.MISSING_DATA:
            self.value_label.setStyleSheet("color: red")
            self.value_label.setText(self.value_label.text() + " - NO DATA")
        else:
            self.value_label.setStyleSheet("color: white")
