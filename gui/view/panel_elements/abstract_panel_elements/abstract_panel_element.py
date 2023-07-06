from PySide2.QtWidgets import QWidget

from data.sensor import Sensor, SensorState
from data.sensor_manager import SensorManager
from PySide2.QtCore import Signal, SIGNAL


class AbstractPanelElement(QWidget):
    value_changed_signal = Signal(float, str)
    state_changed_signal = Signal(SensorState, SensorState)

    def __init__(self, title: str, sensor_id: int):
        super().__init__()

        self.title = title

        self.sensor_id = sensor_id

        self.setContentsMargins(0, 0, 0, 0)

        # Connect sensor
        self.sensor = SensorManager.get_sensor(sensor_id)
        if self.sensor:
            self.sensor.add_qt_valuechange_handler(self)
            self.value_changed_signal.connect(lambda v, name: self.sensor_value_changed(v, name))
            self.sensor.add_qt_statechange_handler(self)
            self.state_changed_signal.connect(self.sensor_state_changed)
        else:
            pass  # TODO (dani, mate) invalid sensor? abstract function?


    def sensor_state_changed(self, state, old_state):
        raise NotImplementedError('sensor_state_changed must be implemented!')

    def sensor_value_changed(self, value, old_value):
        raise NotImplementedError('sensor_value_changed must be implemented!')
