from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class BatteryTemperatureWidget(QWidget):
    # SIG_CHANGED = Signal(int)

    def __init__(self, sensor_id):
        super().__init__()
        # self.sensor = SensorManager.get_sensor(sensor_id)
        #
        # self.sensor.register_callback(
        #     lambda val: self.sig_valami.emit(val)
        # )

        # Create main layout
        main_layout = QVBoxLayout(self)

        # Panel name
        name_label = QLabel('BatteryTemperature')
        main_layout.addWidget(name_label)

        # Panel value
        self.value_label = QLabel('0')
        main_layout.addWidget(self.value_label)

        # Create connections
        # SIG_MANAGER.sig_battery_temperature_changed.connect(
        #     lambda value: self.value_label.setText(str(value))
        # )
