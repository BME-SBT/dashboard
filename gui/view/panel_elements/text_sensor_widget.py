from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Signal
from data.sensor import SensorState

from data.sensor_manager import SensorManager


class TextSensorWidget(QWidget):

    sensor_value_changed = Signal(str)

    def __init__(self, title: str, sensor_id: int):
        super().__init__()

        # Create main layout
        main_layout = QVBoxLayout(self)

        # Panel name
        name_label = QLabel(title)
        main_layout.addWidget(name_label)

        # Panel value
        self.value_label = QLabel('N/A')
        main_layout.addWidget(self.value_label)

        sensor = SensorManager.get_sensor(sensor_id)
        if sensor:
            sensor.set_valuechange_handler(
                lambda v, oldval: self.sensor_value_changed.emit(str(v)))
            self.sensor_value_changed.connect(
                lambda s: self.value_label.setText(f"{s} {sensor.data_type.unit}"))
            sensor.set_statechange_handler(self.sensor_state_changed)
        else:
            self.value_label.setText('<invalid sensor>')

    def sensor_state_changed(self, state, oldstate):
        if state == SensorState.MISSING_DATA:
            self.value_label.setStyleSheet("color: red")
            self.value_label.setText(self.value_label.text() + " - NO DATA")
        else:
            self.value_label.setStyleSheet("color: black")
