from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout

from gui.view.panels.abstract_panel import AbstractPanel
from gui.view.panel_elements.battery_current_widget import BatteryCurrentWidget
from gui.view.panel_elements.motor_rpm_widget import MotorRPMWidget
from gui.view.panel_elements.gps_speed_widget import GPSSpeedWidget
from gui.view.panel_elements.battery_voltage_widget import BatteryVoltageWidget
from gui.view.panel_elements.motor_power_widget import MotorPowerWidget
from gui.view.panel_elements.battery_temperature_widget import BatteryTemperatureWidget
from gui.view.panel_elements.motor_temperature_widget import MotorTemperatureWidget


class HomePanel(AbstractPanel):
    def __init__(self):
        super().__init__()

        #  Panel elements:
        #   - RPM - MotorRPMWidget
        #   - Sebesseg - GPSSpeedWidget
        #   - Akkufesz - BatteryVoltageWidget
        #   - Motor telj - MotorPowerWidget
        #   - Motor ho - MotorTemperatureWidget
        #   - Akku ho - BatteryTemperatureWidget
        #   - Akku aram - BatteryCurrentWidget

        # Main Layout
        main_layout = QHBoxLayout(self)

        # Middle Part Layout, temperatures and indicators
        middle_part_layout = QVBoxLayout()

        # Top Layout, temperatures
        top_layout = QHBoxLayout()
        top_layout.addWidget(MotorTemperatureWidget())
        top_layout.addStretch()
        top_layout.addWidget(BatteryTemperatureWidget())

        # Bottom Layout, indicators
        bottom_layout = QHBoxLayout()
        bottom_layout.addStretch()
        bottom_layout.addWidget(MotorPowerWidget())
        bottom_layout.addWidget(MotorRPMWidget())
        bottom_layout.addWidget(GPSSpeedWidget())
        bottom_layout.addWidget(BatteryVoltageWidget())
        bottom_layout.addStretch()

        # Add layouts to Middle Part layout
        middle_part_layout.addLayout(top_layout)
        middle_part_layout.addLayout(bottom_layout)

        # Add layouts to Main layout
        main_layout.addWidget(BatteryCurrentWidget())
        main_layout.addLayout(middle_part_layout)





