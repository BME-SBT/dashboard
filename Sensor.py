from struct import unpack
from DataType import DataType

class Sensor:
    def __init__(self, id, name, data_type : DataType, callback_function):
        self.id = id
        self.name = name
        self.data_type = data_type
        self.callback_function = callback_function

    def add_data(self, data):
        # print(data)
        self.callback_function(self.id, self.name, self.convert_message(data), self.data_type.unit)
        
    def convert_message(self, message):
        unpacked_value = unpack(self.data_type.number_type.value, message)[0]
        return unpacked_value * self.data_type.resolution
