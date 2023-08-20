from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QLabel
from PySide2.QtCore import Signal
from data.sensor import SensorState
from data.sensor_ids import SensorId
from data.sensor_manager import SensorManager


class NetworkstatusImage(QLabel):
    value_changed_signal = Signal(float, str)
    state_changed_signal = Signal(SensorState, SensorState)

    def __init__(self, *args, **kwargs):
        super().__init__(None, *args, **kwargs)
        self.setFixedHeight(45)
        self.setFixedWidth(45)

        SensorManager.get_sensor(
            SensorId.TELEMETRY_NETWORK_STATUS.value
        ).add_qt_statechange_handler(self)
        SensorManager.get_sensor(
            SensorId.TELEMETRY_NETWORK_STATUS.value
        ).add_qt_valuechange_handler(self)

        self.ok_image = QPixmap("./gui/view/images/network_status_ok.png")
        self.err_image = QPixmap(f"./gui/view/images/network_status_error.png")

        self.setPixmap(self.err_image)

        self.state_changed_signal.connect(self.state_changed)
        self.value_changed_signal.connect(self.value_changed)

    def state_changed(self, v, ov):
        if (ov == SensorState.NO_DATA and v == SensorState.NORMAL) or (
            ov == SensorState.MISSING_DATA and v == SensorState.NORMAL
        ):
            self.setPixmap(self.ok_image)
        elif ov == SensorState.NORMAL and v != SensorState.NORMAL:
            self.setPixmap(self.err_image)

    def value_changed(self, v, name):
        if v:
            self.setPixmap(self.ok_image)
        else:
            self.setPixmap(self.err_image)
