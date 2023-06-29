import logging
import math
from data.sensor import Sensor
from can.message import Message


class SensorManager:
    sensors = dict()

    @classmethod
    def add_sensor(cls, sensor: Sensor):
        cls.sensors[sensor.id] = sensor

    @classmethod
    def receive_message(cls, message: Message):
        # data = self.sensors[sensor_id].add_data(message)
        message_id, data = message.arbitration_id, message.data
        #print(f"raw: {hex(message_id)}: {data}")
        if message_id in cls.sensors.keys():
            sensor: Sensor = cls.sensors[message_id]
            sensor.add_data(data)
        else:
            logging.warn(f"unknown CAN ID: {message_id}")

    @classmethod
    def get_sensor(cls, id: int) -> Sensor:
        if id in cls.sensors.keys():
            return cls.sensors[id]
        return None

    @classmethod
    def lcm_frequency(cls):
        lcm = 1
        for sensor in cls.sensors.values():
            lcm = math.lcm(lcm, sensor.update_frequency)

        return lcm

    @classmethod
    def lcm_tick(cls):
        for sensor in cls.sensors.values():
            sensor.timer_tick()

    @classmethod
    def get_sensors(cls):
        return cls.sensors.values()
