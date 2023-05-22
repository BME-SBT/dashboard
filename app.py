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
from data.sensor_ids import SensorId

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
LOGGER = logging.getLogger("app")

CAN_BITRATE = 500E3


def build_sensor_array():
    LOGGER.info("registering sensors")
    
    SensorManager.add_sensor(
        Sensor(SensorId.THROTTLE_POSITION,  data.data_types.THROTTLE_POSITION, "throttle_position", 100))
    SensorManager.add_sensor(
        Sensor(SensorId.SWITCH_POSITIONS,  data.data_types.SWITCH_POSITION, "switch_positions", 10))
    SensorManager.add_sensor(
        Sensor(SensorId.MOTOR_RPM,  data.data_types.RPM, "motor_rpm", 10))
    SensorManager.add_sensor(
        Sensor(SensorId.BATTERY_VOLTAGE,  data.data_types.VOLTAGE, "battery_voltage", 10))
    SensorManager.add_sensor(
        Sensor(SensorId.BATTERY_TEMPERATURE_1_2_3,  data.data_types.TEMPERATURE, "battery_temperature_1_2_3", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.MOTOR_TEMPERATURE,  data.data_types.TEMPERATURE, "motor_temperature", 10))
    SensorManager.add_sensor(
        Sensor(SensorId.MOTOR_CONTROLLER_TEMPERATURE,  data.data_types.TEMPERATURE, "motor_controller_temperature", 10))
    SensorManager.add_sensor(
        Sensor(SensorId.BATTERY_SOC,  data.data_types.SOC, "battery_soc", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.MPPT_TEMPERATURE_1,  data.data_types.TEMPERATURE, "mppt_temperature_1", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.MPPT_TEMPERATURE_2,  data.data_types.TEMPERATURE, "mppt_temperature_2", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.MPPT_TEMPERATURE_3,  data.data_types.TEMPERATURE, "mppt_temperature_3", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.MPPT_TEMPERATURE_4,  data.data_types.TEMPERATURE, "mppt_temperature_4", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.MPPT_TEMPERATURE_5,  data.data_types.TEMPERATURE, "mppt_temperature_5", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.MPPT_TEMPERATURE_6,  data.data_types.TEMPERATURE, "mppt_temperature_6", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.COOLANT_TEMP,  data.data_types.TEMPERATURE, "coolant_temp", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.FOIL_1_POSITION,  data.data_types.ROLL_PITCH_DEGREE, "foil_1_position", 100))
    SensorManager.add_sensor(
        Sensor(SensorId.FOIL_2_POSITION,  data.data_types.ROLL_PITCH_DEGREE, "foil_2_position", 100))
    SensorManager.add_sensor(
        Sensor(SensorId.HEIGHT,  data.data_types.DISTANCE, "height", 100))
    SensorManager.add_sensor(
        Sensor(SensorId.BATTERY_CURRENT,  data.data_types.CURRENT, "battery_current", 10))
    SensorManager.add_sensor(
        Sensor(SensorId.MPPT_CHARGER_VOLTAGE_1,  data.data_types.VOLTAGE, "mppt_charger_voltage_1", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.MPPT_CHARGER_VOLTAGE_2,  data.data_types.VOLTAGE, "mppt_charger_voltage_2", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.MPPT_CHARGER_VOLTAGE_3,  data.data_types.VOLTAGE, "mppt_charger_voltage_3", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.MPPT_CHARGER_VOLTAGE_4,  data.data_types.VOLTAGE, "mppt_charger_voltage_4", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.MPPT_CHARGER_VOLTAGE_5,  data.data_types.VOLTAGE, "mppt_charger_voltage_5", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.MPPT_CHARGER_VOLTAGE_6,  data.data_types.VOLTAGE, "mppt_charger_voltage_6", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.MPPT_CHARGER_CURRENT_1,  data.data_types.CURRENT, "mppt_charger_current_1", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.MPPT_CHARGER_CURRENT_2,  data.data_types.CURRENT, "mppt_charger_current_2", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.MPPT_CHARGER_CURRENT_3,  data.data_types.CURRENT, "mppt_charger_current_3", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.MPPT_CHARGER_CURRENT_4,  data.data_types.CURRENT, "mppt_charger_current_4", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.MPPT_CHARGER_CURRENT_5,  data.data_types.CURRENT, "mppt_charger_current_5", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.MPPT_CHARGER_CURRENT_6,  data.data_types.CURRENT, "mppt_charger_current_6", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.MOTOR_CONTROLLER_CURRENT,  data.data_types.CURRENT, "motor_controller_current", 10))
    SensorManager.add_sensor(
        Sensor(SensorId.GEARBOX_RPM,  data.data_types.RPM, "gearbox_rpm", 10))
    SensorManager.add_sensor(
        Sensor(SensorId.MOTOR_POWER,  data.data_types.POWER, "motor_power", 10))
    SensorManager.add_sensor(
        Sensor(SensorId.COOLANT_LEVEL,  data.data_types.LEVEL, "coolant_level", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.ACCUBOX_AIR_TEMPERATURE,  data.data_types.TEMPERATURE, "accubox_air_temperature", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.SOLARBOX_AIR_TEMPERATURE,  data.data_types.TEMPERATURE, "solarbox_air_temperature", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.MOTORBOX_AIR_TEMPERATURE,  data.data_types.TEMPERATURE, "motorbox_air_temperature", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.TELEMETRYBOX_AIR_TEMPERATURE,  data.data_types.TEMPERATURE, "telemetrybox_air_temperature", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.AMBIENT_TEMPERATURE,  data.data_types.TEMPERATURE, "ambient_temperature", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.GPS_TIME,  data.data_types.ABSOLUTTIME, "gps_time", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.RTC_TIME,  data.data_types.ABSOLUTTIME, "rtc_time", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.COOLANT_FLOW,  data.data_types.FLOW, "coolant_flow", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.MOTOR_VIBRATION,  data.data_types.ACCELERATION, "motor_vibration", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.GPS_SPEED,  data.data_types.SPEED, "gps_speed", 10))
    SensorManager.add_sensor(
        Sensor(SensorId.GPS_POSITION,  data.data_types.GPS_POSITION, "gps_position", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.ROLL,  data.data_types.ROLL_PITCH_DEGREE, "roll", 10))
    SensorManager.add_sensor(
        Sensor(SensorId.PITCH,  data.data_types.ROLL_PITCH_DEGREE, "pitch", 10))
    SensorManager.add_sensor(
        Sensor(SensorId.GPS_HEDING,  data.data_types.HEADING, "gps_heding", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.MAGNETIC_HEDING,  data.data_types.HEADING, "magnetic_heding", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.WIND_DIRECTION,  data.data_types.HEADING, "wind_direction", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.WIND_SPEED,  data.data_types.SPEED, "wind_speed", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.ACCUBOX_FAN_RPM,  data.data_types.RPM, "accubox_fan_rpm", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.MOTORBOX_FAN_RPM,  data.data_types.RPM, "motorbox_fan_rpm", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.MOTORBOX_FAN_RPM,  data.data_types.RPM, "solarbox_fan_rpm", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.TELEMETRYBOX_FAN_RPM,  data.data_types.RPM, "telemetrybox_fan_rpm", 1))
    SensorManager.add_sensor(
        Sensor(SensorId.ERROR_THROTTLE_POSITION,  data.data_types.THROTTLE_POSITION, "error_throttle_position", 100))
    SensorManager.add_sensor(
        Sensor(SensorId.ERROR_DEAD_MANS_SWITCH_POSITION,  data.data_types.SWITCH_POSITION, "error_dead_mans_switch_position", 10))
    SensorManager.add_sensor(
        Sensor(SensorId.ERROR_MOTOR_SWITCH_POSITION,  data.data_types.SWITCH_POSITION, "error_motor_switch_position", 10))


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
                LOGGER.warning('restarting bus after timeout')
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
