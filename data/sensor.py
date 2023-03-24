from struct import unpack
from data.data_types import DataType
from enum import Enum
import time


class SensorState(Enum):
    NO_DATA = 0,
    NORMAL = 1,
    MISSING_DATA = 2,


class Sensor:
    def __init__(self, id: int, data_type: DataType, name: str, update_frequency: int, missing_data_multiplier: int = 5):
        self.id = id
        self.name = name
        self.data_type = data_type
        self.state = SensorState.NO_DATA
        self.update_frequency = update_frequency
        self.missing_data_multiplier = missing_data_multiplier
        self.last_updated = 0
        self.value = None

        self.valuechange_handler = None
        self.statechange_handler = None

    def set_valuechange_handler(self, callback):
        self.valuechange_handler = callback

    def set_statechange_handler(self, callback):
        self.statechange_handler = callback

    def add_data(self, data):
        value = self.data_type.get_value(data)
        self.last_updated = time.time()
        self._set_state(SensorState.NORMAL)

        self._set_value(value)

    def _set_value(self, value):
        oldval = self.value
        self.value = value
        if self.valuechange_handler:
            self.valuechange_handler(self.value, oldval)

    def _set_state(self, state: SensorState):
        if self.state != state:
            oldstate = self.state
            self.state = state
            if self.statechange_handler:
                self.statechange_handler(self.state, oldstate)

    def timer_tick(self):
        update_interval = 1 / self.update_frequency
        if time.time() > (self.last_updated + (update_interval * self.missing_data_multiplier)):
            if self.state == SensorState.NORMAL:
                self._set_state(SensorState.MISSING_DATA)
