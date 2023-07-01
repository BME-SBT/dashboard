from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QHBoxLayout

from data.sensor import SensorState
from gui.view.panel_elements.heartbeat_image import HeartbeatImage
from gui.view.panel_elements.warn_image import WarnImage


class TopBar(QWidget):
    """The top bar that contains the warning icons."""
    def __init__(self):
        super().__init__()

        # Style
        self.setFixedHeight(50)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(10)

        self.motor_data_warn = WarnImage(0b00001010010, "motor_data_warn", lambda v,name: False, lambda s, os: s == SensorState.MISSING_DATA)
        self.motor_temp_warn = WarnImage(0b00010110010, "motor_temp_warn", lambda v,name: v >= 65.0)
        self.motor_temp_err = WarnImage(0b00010110010, "motor_temp_err", lambda v,name: v >= 85.0)
        self.controller_temp_warn = WarnImage(0b00011010010, "controller_temp_warn", lambda v,name: v >= 70.0)
        self.battery_soc_warn = WarnImage(0b00001110000, "battery_soc_warn", lambda v,name: v <= 40.0)
        self.battery_soc_err = WarnImage(0b00001110000, "battery_soc_err", lambda v,name: v <= 37.2)
        self.battery_temp_warn = WarnImage(0b00010010000, "battery_temp_warn", lambda v,name: v >= 50.0)

        self.motor_on_ok = WarnImage(0b00001010010, "motor_on", lambda v,name: True, lambda s, os: s == SensorState.NORMAL, True)
        self.heartbeat = HeartbeatImage()

        main_layout.addSpacing(10)

        main_layout.addWidget(self.motor_data_warn)
        main_layout.addWidget(self.motor_temp_warn)
        main_layout.addWidget(self.motor_temp_err)
        main_layout.addWidget(self.controller_temp_warn)
        main_layout.addWidget(self.battery_soc_warn)
        main_layout.addWidget(self.battery_soc_err)
        main_layout.addWidget(self.battery_temp_warn)

        main_layout.addStretch()
        main_layout.addWidget(self.motor_on_ok)
        main_layout.addWidget(self.heartbeat)
        main_layout.addSpacing(10)
