from struct import pack
from can import Message
from DataType import DataType
from Sensor import Sensor
from SensorManager import SensorManager
from NumberType import NumberType

rpm = DataType(NumberType.SIGNED_INT, 1, '1/min')
temperature = DataType(NumberType.SIGNED_INT, 0.1, '°C')
current = DataType(NumberType.SIGNED_INT, 0.1, 'A')
mcurrent = DataType(NumberType.SIGNED_INT, 1, 'mA')
voltage = DataType(NumberType.SIGNED_INT, 0.01, 'V')
soc = DataType(NumberType.UNSIGNED_INT, 0.1, '%')
throttle_position = DataType(NumberType.SIGNED_INT, 1, '%')
switch_position = DataType(NumberType.UNSIGNED_INT, 1, '')
gps_position = DataType(NumberType.FLOAT, 0.01, '°')
speed = DataType(NumberType.SIGNED_INT, 0.1, 'km/h')
roll_pitch_degree = DataType(NumberType.SIGNED_INT, 1, '°')
heading = DataType(NumberType.UNSIGNED_INT, 1, 'sec')
absoluttime = DataType(NumberType.UNSIGNED_INT, 1, 'sec')
power = DataType(NumberType.SIGNED_INT, 1, 'mW')
acceleration = DataType(NumberType.SIGNED_INT, 1, 'm/s^2')
flow = DataType(NumberType.UNSIGNED_INT, 1, 'L\sec')
distance = DataType(NumberType.SIGNED_INT, 1, 'mm')
level = DataType(NumberType.UNSIGNED_INT, 1, '%')
percent = DataType(NumberType.SIGNED_INT, 0.1, '%')
degree = DataType(NumberType.SIGNED_INT, 0.1, '°')

def printMessage(sensor_id, sensor_name, message, unit):
    print(type(message))
    print('sensor id: ' + str(sensor_id) +' sensor name: '+ sensor_name + ' message: ' + str(message) + ' ' + unit)

sensors = SensorManager()
sensorA = Sensor(1, 'SensorA', rpm, printMessage)
sensorB = Sensor(2, 'SensorB', temperature, printMessage)
sensorC = Sensor(3, 'SensorC', gps_position, printMessage)
sensorD = Sensor(4, 'SensorD', soc, printMessage)

sensors.add_sensor(sensorA)
sensors.add_sensor(sensorB)
sensors.add_sensor(sensorC)
sensors.add_sensor(sensorD)

# can_original_message = "01000000100000000001100000001000000000000001111111111"

data0 = pack(NumberType.SIGNED_INT.value, 15)
data1 = pack(NumberType.SIGNED_INT.value, -20)
data2 = pack(NumberType.SIGNED_INT.value, 123)
data3 = pack(NumberType.FLOAT.value, 118.12356)
data4 = pack(NumberType.FLOAT.value, -585.235)
data5 = pack(NumberType.UNSIGNED_INT.value, 836)

message0 = Message(data=data0, arbitration_id=1)
message1 = Message(data=data1, arbitration_id=1)
message2 = Message(data=data2, arbitration_id=2)
message3 = Message(data=data3, arbitration_id=3)
message4 = Message(data=data4, arbitration_id=3)
message5 = Message(data=data5, arbitration_id=4)

sensors.receive_message(message0)
sensors.receive_message(message1)
sensors.receive_message(message2)
sensors.receive_message(message3)
sensors.receive_message(message4)
sensors.receive_message(message5)