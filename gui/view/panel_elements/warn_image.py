from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QLabel

from data.sensor import SensorState
from data.sensor_manager import SensorManager


class WarnImage(QLabel):
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

        SensorManager.get_sensor(id).add_statechange_handler(lambda v, ov: self.state_chaned(v, ov))
        SensorManager.get_sensor(id).add_valuechange_handler(lambda v, name: self.value_changed(v, name))

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
