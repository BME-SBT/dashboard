import time
from app import CAN_BITRATE

import can, time
import sys
from data import data_types
from can.message import Message
from threading import Thread
from data.sensor_ids import SensorId

def send_message(arbitration_id, is_extended_id, value, data_type):
        message = Message( arbitration_id = arbitration_id,
                              is_extended_id = is_extended_id, data=data_type.to_raw(float(value)))
        bus.send(msg=message)

if __name__ == "__main__":
    bus = None
    try:
        bus = can.Bus(
            'ws://localhost:54701/',
                      bustype='remote',
                      bitrate=CAN_BITRATE)

        # do CAN things
       
        motor_temp = open("test_data/motor_temp.txt", 'r').readlines()
        motor_rpm = open("test_data/motor_rpm.txt", 'r').readlines()
        motor_controller_temp = open("test_data/motor_controller_temp.txt", 'r').readlines()
        motor_power = open("test_data/motor_power.txt", 'r').readlines()
        motor_controller_current = open("test_data/motor_controller_current.txt", 'r').readlines()
        voltage = open("test_data/voltage.txt", 'r').readlines()
        battery_current = open("test_data/battery_current.txt", 'r').readlines()
        battery_temp = open("test_data/battery_temp.txt", 'r').readlines()

        i = 0
        for j in motor_temp:
            # idk??
            send_message(SensorId.MOTOR_TEMPERATURE.value, False, motor_temp[i], data_types.TEMPERATURE)
            send_message(SensorId.MOTOR_RPM.value, False, motor_rpm[i], data_types.RPM)
            send_message(SensorId.MOTOR_CONTROLLER_TEMPERATURE.value, False, motor_controller_temp[i], data_types.TEMPERATURE)
            if(i < 20):
                send_message(SensorId.MOTOR_POWER.value, False, motor_power[i], data_types.POWER)
            send_message(SensorId.MOTOR_CONTROLLER_CURRENT.value, False, motor_controller_current[i], data_types.CURRENT)
            send_message(SensorId.BATTERY_VOLTAGE.value, False, voltage[i], data_types.VOLTAGE)            
            send_message(SensorId.BATTERY_CURRENT.value, False, battery_current[i], data_types.CURRENT)
            send_message(SensorId.BATTERY_TEMPERATURE_1_2_3.value, False, battery_current[i], data_types.CURRENT)
            # ?
            # send_message(552, False, battery_temp[i],data_types.TEMPERATURE)

            i+=1
            time.sleep(0.1)

    except Exception as e:
        print(e)
        print(
            f"make sure that the server is running: python3 -m can_remote --interface=virtual --channel=0 --bitrate={int(CAN_BITRATE)}")
        raise e
    



