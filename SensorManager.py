from Sensor import Sensor
from can import Message

class SensorManager:
    sensors = dict()
    def __init__(self) -> None:
        pass
    def add_sensor(self, sensor):
        self.sensors.update({sensor.id: sensor})
    def receive_message(self, message : Message):
        # data = self.sensors[sensor_id].add_data(message)
        message_id, data  = message.arbitration_id, message.data
        sensor : Sensor = self.sensors.get(message_id)
        sensor.add_data(data)