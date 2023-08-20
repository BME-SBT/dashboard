from struct import unpack
from data.data_types import DataType
from enum import Enum
import time


class SensorState(Enum):
    NO_DATA = (0,)
    NORMAL = (1,)
    MISSING_DATA = (2,)


class Sensor:
    def __init__(
        self,
        id: int,
        data_type: DataType,
        name: str,
        update_frequency: float,
        missing_data_multiplier: int = 10,
    ):
        self.id = id
        self.name = name
        self.data_type = data_type
        self.state = SensorState.NO_DATA
        self.update_frequency = update_frequency
        self.missing_data_multiplier = missing_data_multiplier
        self.last_updated = 0
        self.value = None

        self.qt_valuechange_handlers = []
        self.qt_statechange_handlers = []
        self.statechange_handlers = []
        self.valuechange_handlers = []

    def add_qt_valuechange_handler(self, sensor_handler_object):
        self.qt_valuechange_handlers.append(sensor_handler_object)

    def add_qt_statechange_handler(self, sensor_handler_object):
        self.qt_statechange_handlers.append(sensor_handler_object)

    def add_valuechange_handler(self, callback):
        self.valuechange_handlers.append(callback)

    def add_statechange_handler(self, callback):
        self.statechange_handlers.append(callback)

    def add_data(self, data):
        value = self.data_type.get_value(data)
        self.last_updated = time.time()
        self._set_state(SensorState.NORMAL)
        # print("state changed")

        self._set_value(value)

    def _set_value(self, value):
        self.value = value

        for valuechange_handler in self.valuechange_handlers:
            valuechange_handler(self.value, self.name)

        for valuechange_handler in self.qt_valuechange_handlers:
            valuechange_handler.value_changed_signal.emit(self.value, self.name)

    def _set_state(self, state: SensorState):
        if self.state != state:
            oldstate = self.state
            self.state = state
            for statechange_handler in self.statechange_handlers:
                statechange_handler(self.state, oldstate)

            for statechange_handler in self.qt_statechange_handlers:
                statechange_handler.state_changed_signal.emit(self.state, oldstate)

    def timer_tick(self):
        update_interval = 1 / self.update_frequency
        if time.time() > (
            self.last_updated + (update_interval * self.missing_data_multiplier)
        ):
            if self.state == SensorState.NORMAL:
                self._set_state(SensorState.MISSING_DATA)
