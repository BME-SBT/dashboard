from enum import Enum
import struct


class NumberType(Enum):
    FLOAT = '>f'
    DOUBLE = '>d'
    INT = '>i'
    UNSIGNED_INT = '>I'
    SHORT = '>h'
    UNSIGNED_SHORT = '>H'
    CHAR = '>'
    UNSIGNED_CHAR = '>'


class DataType:
    def __init__(self, number_type: NumberType, resolution, unit):
        self.number_type = number_type
        self.resolution = resolution
        self.unit = unit

    def get_value(self, data):
        return struct.unpack(self.number_type.value, data)[0] * self.resolution

    def get_text_value(self, data):
        val = self.get_value(data)
        return f"{val} {self.unit}"

    def to_raw(self, value):
        return struct.pack(self.number_type.value, int((value / self.resolution)))


RPM = DataType(NumberType.SHORT, 1, '1/min')
TEMPERATURE = DataType(NumberType.SHORT, 0.1, '°C')
CURRENT = DataType(NumberType.SHORT, 0.1, 'A')
MCURRENT = DataType(NumberType.SHORT, 1, 'mA')
VOLTAGE = DataType(NumberType.SHORT, 0.1, 'V')
VOLTAGE_MV = DataType(NumberType.SHORT, 1, 'mV')
SOC = DataType(NumberType.UNSIGNED_SHORT, 0.1, '%')
THROTTLE_POSITION = DataType(NumberType.SHORT, 1, '%')
SWITCH_POSITION = DataType(NumberType.UNSIGNED_SHORT, 1, '')
GPS_POSITION = DataType(NumberType.FLOAT, 1, '°')
SPEED = DataType(NumberType.SHORT, 0.1, 'km/h')
ROLL_PITCH_DEGREE = DataType(NumberType.SHORT, 1, '°')
HEADING = DataType(NumberType.UNSIGNED_SHORT, 1, 'sec')
ABSOLUTTIME = DataType(NumberType.UNSIGNED_INT, 1, 'sec')
POWER = DataType(NumberType.INT, 1, 'mW')
ACCELERATION = DataType(NumberType.SHORT, 1, 'm/s^2')
FLOW = DataType(NumberType.UNSIGNED_SHORT, 1, 'L\sec')
DISTANCE = DataType(NumberType.SHORT, 1, 'mm')
LEVEL = DataType(NumberType.UNSIGNED_SHORT, 1, '%')
PERCENT = DataType(NumberType.SHORT, 0.1, '%')
DEGREE = DataType(NumberType.SHORT, 0.1, '°')
