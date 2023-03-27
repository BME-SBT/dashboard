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
        Sensor(1112, data.data_types.RPM, "motor_rpm", 10))

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
