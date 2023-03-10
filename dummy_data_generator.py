import random
import sys
import time
from typing import Tuple

from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication

from process_can_messages_test import SensorManager


class DummyData:
    def __init__(self, init_value: object, full_range: Tuple, diff_range: Tuple, value_type: object, signal: Signal):
        self.current_value = init_value
        self.value_type = value_type
        self.signal = signal

        self.min_value = full_range[0]
        self.max_value = full_range[1]

        self.diff_min = diff_range[0]
        self.diff_max = diff_range[1]

    def emit_new_value(self):
        diff = random.randint(self.diff_min, self.diff_max)
        positive_sign = random.random() > 0.5

        if self.current_value < self.min_value:
            self.current_value += diff
        elif self.current_value > self.max_value:
            self.current_value -= diff
        elif positive_sign:
            self.current_value += diff
        else:
            self.current_value -= diff

        self.signal.emit(self.current_value)


class DummyDataGenerator(QThread):
    def __init__(self):
        super().__init__()
        self.manager = SensorManager()

        self.stop = False

        # Accubox
        # self.battery_temperatue = DummyData(40, (10, 100), (0, 3), int, SIG_MANAGER.sig_battery_temperature_changed)
        # self.battery_current = DummyData(70, (60, 100), (2, 4), int, SIG_MANAGER.sig_battery_current_changed)

        # battery_temperature = Sensor()
        # self.manager.add_sensor(bms)
        # manager.add_sensor()

    def run(self) -> None:
        while not self.stop:
            # self.battery_temperatue.emit_new_value()
            # self.battery_current.emit_new_value()
            time.sleep(0.2)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    generator = DummyDataGenerator()
    generator.start()

    sys.exit(app.exec())
