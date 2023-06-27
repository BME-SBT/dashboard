from PySide2.QtWidgets import QWidget

from data.sensor_manager import SensorManager


class AbstractPanelElement(QWidget):
    def __init__(self, title: str, sensor_id: int):
        super().__init__()

        self.title = title
        self.sensor_id = sensor_id

        self.setContentsMargins(0, 0, 0, 0)

        # Connect sensor
        self.sensor = SensorManager.get_sensor(sensor_id)
        if self.sensor:
            self.sensor.add_valuechange_handler(self.sensor_value_changed)
            self.sensor.add_statechange_handler(self.sensor_state_changed)
        else:
            pass  # TODO (dani, mate) invalid sensor? abstract function?

    def sensor_state_changed(self, state, old_state):
        raise NotImplementedError('sensor_state_changed must be implemented!')

    def sensor_value_changed(self, value, old_value):
        raise NotImplementedError('sensor_value_changed must be implemented!')
