from struct import * 

# Tudom, hogy külön fájlba kell, meg csúnya meg minden, csak első próba, hogy egyáltalán ilyenre kell-e gondolni

FLOAT = '<f'
DOUBLE = '<d'
INT = 'i'


class Sensor:
    def __init__(self, id, data_type):
        self.id = id
        self.data_type = data_type
    def add_data(self, data):
        print(data)
        if(self.data_type == INT):
            decoded_data =int(data, 2)
            print(decoded_data)


class SensorManager:
    sensors = dict()
    def __init__(self) -> None:
        pass
    def add_sensor(self, sensor):
        self.sensors.update({sensor.id: sensor})
    def receive_message(self, message):
        # data = self.sensors[sensor_id].add_data(message)
        message_id, data  = self.split_message(message) 
        sensor : Sensor = self.sensors.get(message_id)
        sensor.add_data(data)

    def split_message(self, can_message):
        # sof = can_message[:1]
        # priority = can_message[1:2]
        message_id = can_message[2:9]
        # node_id = can_message[9:121]
        # rtr = can_message[12:13]
        # ide = can_message[13:14]
        # r1 = can_message[14:15]
        # r0 = can_message[15:16]
        dlc = can_message[16:20]
        # data_length_bytes = bytes.
        data_length = int(dlc)
        data = can_message[20:20+data_length*8]
        # print('can_message: ' + can_message)
        # print('sof: ' + sof + ' priority: ' + priority + ' message_id: ' + message_id + ' data_length: ' + str(data_length) + ' data: ' + data)
        return (message_id, data)

can_original_message = "01000000100000000001100000001000000000000001111111111"
sensors = SensorManager()
sensorA = Sensor("0000001", INT)
sensorB = Sensor("0000010", INT)
sensors.add_sensor(sensorA)
sensors.add_sensor(sensorB)
sensors.receive_message(can_original_message)