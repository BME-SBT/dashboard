from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QLabel
from PySide2.QtCore import Signal
from data.sensor import SensorState
from data.sensor_manager import SensorManager


class WarnImage(QLabel):
    value_changed_signal = Signal(float, str)
    state_changed_signal = Signal(SensorState, SensorState)
    def __init__(self, id: int, name: str, value_validator, state_validator=None, init_false = False, *args, **kwargs):
        super().__init__(None, *args, **kwargs)
        self.setFixedHeight(45)
        self.setFixedWidth(45)

        self.blank_picture = QPixmap("./gui/view/images/blank.png")
        self.warn_image = QPixmap(f"./gui/view/images/{name}.png")

        if init_false:
            self.setPixmap(self.blank_picture)
        else:
            self.setPixmap(self.warn_image)

        self.state_validator = state_validator
        self.value_validator = value_validator

        SensorManager.get_sensor(id).add_qt_statechange_handler(self)
        SensorManager.get_sensor(id).add_qt_valuechange_handler(self)

        self.state_changed_signal.connect(self.state_changed)
        self.value_changed_signal.connect(self.value_changed)

    def state_changed(self, v, ov):
        if self.state_validator is not None:
            if self.state_validator(v, ov):
                self.setPixmap(self.warn_image)
            else:
                self.setPixmap(self.blank_picture)
        else:
            if ov == SensorState.NO_DATA and v == SensorState.NORMAL:
                self.setPixmap(self.blank_picture)

    def value_changed(self, v, name):
        if self.value_validator(v, name):
            self.setPixmap(self.warn_image)
        else:
            self.setPixmap(self.blank_picture)
