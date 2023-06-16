from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout

from gui.view.panel_elements.permanent_panel.permanent_battery_current_widget import PermanentBatteryCurrentWidget
from gui.view.panel_elements.permanent_panel.permanent_battery_temperature_widget import PermanentBatteryTemperatureWidget
from gui.view.panel_elements.permanent_panel.permanent_battery_voltage_widget import PermanentBatteryVoltageWidget
from gui.view.panel_elements.permanent_panel.permanent_motor_rpm_widget import PermanentMotorRPMWidget
from gui.view.panel_elements.permanent_panel.permanent_motor_temperature_widget import PermanentMotorTemperatureWidget


class PermanentPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(850, 120)

        # Style
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        self.setContentsMargins(0, 0, 0, 0)

        # Layout
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Panel elements
        self.permanent_battery_temperature_widget = PermanentBatteryTemperatureWidget()
        self.permanent_battery_current_widget = PermanentBatteryCurrentWidget()
        self.permanent_battery_voltage_widget = PermanentBatteryVoltageWidget()
        self.permanent_motor_rpm_widget = PermanentMotorRPMWidget()
        self.permanent_motor_temperature_widget = PermanentMotorTemperatureWidget()

        main_layout.addWidget(self.permanent_motor_rpm_widget)
        main_layout.addWidget(self.permanent_battery_voltage_widget)
        main_layout.addWidget(self.permanent_battery_current_widget)
        main_layout.addWidget(self.permanent_motor_temperature_widget)
        main_layout.addWidget(self.permanent_battery_temperature_widget)
