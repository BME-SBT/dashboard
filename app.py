import logging
import sys
import time

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QThread
import can
from can.interfaces import udp_multicast
import data.data_types
from data.sensor import Sensor
from data.sensor_manager import SensorManager
from gui.main_window import DashboardWindow

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
LOGGER = logging.getLogger("app")

CAN_BITRATE = 500E3


def build_sensor_array():
    LOGGER.info("registering sensors")
    
    SensorManager.add_sensor(
        Sensor(0b00000010101, data.data_types.THROTTLE_POSITION, "throttle_position", 100))
    SensorManager.add_sensor(
        Sensor(0b00000110101, data.data_types.SWITCH_POSITION, "switch_positions", 10))
    SensorManager.add_sensor(
        Sensor(0b00001010010, data.data_types.RPM, "motor_rpm", 10))
    SensorManager.add_sensor(
        Sensor(0b00001110000, data.data_types.VOLTAGE, "battery_voltage", 10))
    SensorManager.add_sensor(
        Sensor(0b00010010000, data.data_types.TEMPERATURE, "battery_temperature_1_2_3", 1))
    SensorManager.add_sensor(
        Sensor(0b00010110010, data.data_types.TEMPERATURE, "motor_temperature", 10))
    SensorManager.add_sensor(
        Sensor(0b00011010010, data.data_types.TEMPERATURE, "motor_controller_temperature", 10))
    SensorManager.add_sensor(
        Sensor(0b00011110000, data.data_types.SOC, "battery_soc", 1))
    SensorManager.add_sensor(
        Sensor(0b00100010001, data.data_types.TEMPERATURE, "mppt_temperature_1", 1))
    SensorManager.add_sensor(
        Sensor(0b00100110001, data.data_types.TEMPERATURE, "mppt_temperature_2", 1))
    SensorManager.add_sensor(
        Sensor(0b00101010001, data.data_types.TEMPERATURE, "mppt_temperature_3", 1))
    SensorManager.add_sensor(
        Sensor(0b00101110001, data.data_types.TEMPERATURE, "mppt_temperature_4", 1))
    SensorManager.add_sensor(
        Sensor(0b00110010001, data.data_types.TEMPERATURE, "mppt_temperature_5", 1))
    SensorManager.add_sensor(
        Sensor(0b00110110001, data.data_types.TEMPERATURE, "mppt_temperature_6", 1))
    SensorManager.add_sensor(
        Sensor(0b00111010100, data.data_types.TEMPERATURE, "coolant_temp", 1))
    SensorManager.add_sensor(
        Sensor(0b00111111011, data.data_types.ROLL_PITCH_DEGREE, "foil_1_position", 100))
    SensorManager.add_sensor(
        Sensor(0b01000011100, data.data_types.ROLL_PITCH_DEGREE, "foil_2_position", 100))
    SensorManager.add_sensor(
        Sensor(0b01000111011, data.data_types.DISTANCE, "height", 100))
    SensorManager.add_sensor(
        Sensor(0b01001010000, data.data_types.CURRENT, "battery_current", 10))
    SensorManager.add_sensor(
        Sensor(0b01001110001, data.data_types.VOLTAGE, "mppt_charger_voltage_1", 1))
    SensorManager.add_sensor(
        Sensor(0b01010010001, data.data_types.VOLTAGE, "mppt_charger_voltage_2", 1))
    SensorManager.add_sensor(
        Sensor(0b01010110001, data.data_types.VOLTAGE, "mppt_charger_voltage_3", 1))
    SensorManager.add_sensor(
        Sensor(0b01011010001, data.data_types.VOLTAGE, "mppt_charger_voltage_4", 1))
    SensorManager.add_sensor(
        Sensor(0b01011110001, data.data_types.VOLTAGE, "mppt_charger_voltage_5", 1))
    SensorManager.add_sensor(
        Sensor(0b01100010001, data.data_types.VOLTAGE, "mppt_charger_voltage_6", 1))
    SensorManager.add_sensor(
        Sensor(0b01100110001, data.data_types.CURRENT, "mppt_charger_current_1", 1))
    SensorManager.add_sensor(
        Sensor(0b01101010001, data.data_types.CURRENT, "mppt_charger_current_2", 1))
    SensorManager.add_sensor(
        Sensor(0b01101110001, data.data_types.CURRENT, "mppt_charger_current_3", 1))
    SensorManager.add_sensor(
        Sensor(0b01110010001, data.data_types.CURRENT, "mppt_charger_current_4", 1))
    SensorManager.add_sensor(
        Sensor(0b01110110001, data.data_types.CURRENT, "mppt_charger_current_5", 1))
    SensorManager.add_sensor(
        Sensor(0b01111010001, data.data_types.CURRENT, "mppt_charger_current_6", 1))
    SensorManager.add_sensor(
        Sensor(0b01111110010, data.data_types.CURRENT, "motor_controller_current", 10))
    SensorManager.add_sensor(
        Sensor(0b10000010010, data.data_types.RPM, "gearbox_rpm", 10))
    SensorManager.add_sensor(
        Sensor(0b10000110010, data.data_types.POWER, "motor_power", 10))
    SensorManager.add_sensor(
        Sensor(0b10001010100, data.data_types.LEVEL, "coolant_level", 1))
    SensorManager.add_sensor(
        Sensor(0b10001110011, data.data_types.TEMPERATURE, "accubox_air_temperature", 1))
    SensorManager.add_sensor(
        Sensor(0b10010010110, data.data_types.TEMPERATURE, "solarbox_air_temperature", 1))
    SensorManager.add_sensor(
        Sensor(0b10010110010, data.data_types.TEMPERATURE, "motorbox_air_temperature", 1))
    SensorManager.add_sensor(
        Sensor(0b10011010111, data.data_types.TEMPERATURE, "telemetrybox_air_temperature", 1))
    SensorManager.add_sensor(
        Sensor(0b10011110100, data.data_types.TEMPERATURE, "ambient_temperature", 1))
    SensorManager.add_sensor(
        Sensor(0b10100010100, data.data_types.ABSOLUTTIME, "gps_time", 1))
    SensorManager.add_sensor(
        Sensor(0b10100111001, data.data_types.ABSOLUTTIME, "rtc_time", 1))
    SensorManager.add_sensor(
        Sensor(0b10101010100, data.data_types.FLOW, "coolant_flow", 1))
    SensorManager.add_sensor(
        Sensor(0b10101110010, data.data_types.ACCELERATION, "motor_vibration", 1))
    SensorManager.add_sensor(
        Sensor(0b10110010100, data.data_types.SPEED, "gps_speed", 10))
    SensorManager.add_sensor(
        Sensor(0b10110110100, data.data_types.GPS_POSITION, "gps_position", 1))
    SensorManager.add_sensor(
        Sensor(0b10111010100, data.data_types.ROLL_PITCH_DEGREE, "roll", 10))
    SensorManager.add_sensor(
        Sensor(0b10111110100, data.data_types.ROLL_PITCH_DEGREE, "pitch", 10))
    SensorManager.add_sensor(
        Sensor(0b11000010100, data.data_types.HEADING, "gps_heding", 1))
    SensorManager.add_sensor(
        Sensor(0b11000110100, data.data_types.HEADING, "magnetic_heding", 1))
    SensorManager.add_sensor(
        Sensor(0b11001010100, data.data_types.HEADING, "wind_direction", 1))
    SensorManager.add_sensor(
        Sensor(0b11001110100, data.data_types.SPEED, "wind_speed", 1))
    SensorManager.add_sensor(
        Sensor(0b11010010011, data.data_types.RPM, "accubox_fan_rpm", 1))
    SensorManager.add_sensor(
        Sensor(0b11010110010, data.data_types.RPM, "motorbox_fan_rpm", 1))
    SensorManager.add_sensor(
        Sensor(0b11011010110, data.data_types.RPM, "solarbox_fan_rpm", 1))
    SensorManager.add_sensor(
        Sensor(0b11011110111, data.data_types.RPM, "telemetrybox_fan_rpm", 1))
    SensorManager.add_sensor(
        Sensor(0b00000000010, data.data_types.THROTTLE_POSITION, "error_throttle_position", 100))
    SensorManager.add_sensor(
        Sensor(0b00000100010, data.data_types.SWITCH_POSITION, "error_dead_mans_switch_position", 10))
    SensorManager.add_sensor(
        Sensor(0b00001000010, data.data_types.SWITCH_POSITION, "error:motor_switch_position", 10))

    LOGGER.info(f"lcm frequency: {SensorManager.lcm_frequency()}")


def start_gui(can_thread, lcm_thread):
    LOGGER.info("starting gui")
    app = QApplication(sys.argv)

    dashboard = DashboardWindow(can_thread, lcm_thread)
    dashboard.init_stylesheet()
    dashboard.show()

    sys.exit(app.exec())


class CANThread(QThread):

    def __init__(self, use_virtual: bool = False):
        super().__init__()
        self.use_virtual = use_virtual

    def run(self):
        LOGGER.info("CAN thread started")
        while True:
            try:
                with self.create_bus() as bus:
                    while True:
                        message: can.message.Message = bus.recv()
                        SensorManager.receive_message(message)
            except Exception as e:
                print(e)
                LOGGER.warn('restarting bus after timeout')
                QThread.msleep(500)

    def create_bus(self):
        if self.use_virtual:
            return can.Bus('ws://localhost:54701/',
                           bustype='remote',
                           bitrate=CAN_BITRATE)
        else:
            return can.Bus(interface='socketcan', channel='vcan0', bitrate=CAN_BITRATE)


def start_can_thread():
    LOGGER.info("starting CAN thread")
    can_thread = CANThread(True)  # TODO: Replace with false for socketcan
    can_thread.finished.connect(can_thread.deleteLater)
    can_thread.start()
    return can_thread


class LCMThread(QThread):
    def __init__(self, lcm_freq) -> None:
        super().__init__()
        self.wait_time_s = 1 / lcm_freq

    def run(self):
        LOGGER.info("LCM thread started")
        while True:
            try:
                QThread.msleep(int(self.wait_time_s * 1000))
                SensorManager.lcm_tick()
            except Exception as e:
                print(e)


def start_lcm_thread():
    LOGGER.info("starting LCM thread")
    lcm_thread = LCMThread(SensorManager.lcm_frequency())
    lcm_thread.finished.connect(lcm_thread.deleteLater)
    lcm_thread.start()
    return lcm_thread


if __name__ == '__main__':
    build_sensor_array()

    can_thread = start_can_thread()
    lcm_thread = start_lcm_thread()
    start_gui(can_thread, lcm_thread)
