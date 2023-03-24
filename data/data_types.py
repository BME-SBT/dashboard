from enum import Enum
import struct


class NumberType(Enum):
    FLOAT = '>f'
    DOUBLE = '>d'
    SIGNED_INT = '>i'
    UNSIGNED_INT = '>I'
    SHORT = '>h'
    UNSIGNED_SHORT = '>H'


class DataType:
    def __init__(self, number_type: NumberType, resolution, unit):
        self.number_type = number_type
        self.resolution = resolution
        self.unit = unit

    def get_value(self, data):
        return struct.unpack(self.number_type.value, data)[0] / self.resolution

    def get_text_value(self, data):
        val = self.get_value(data)
        return f"{val} {self.unit}"

    def to_raw(self, value):
        return struct.pack(self.number_type.value, int((value / self.resolution)))


# TODO: Port Bakonyi's types
RPM = DataType(NumberType.SHORT, 1, '1/min')
