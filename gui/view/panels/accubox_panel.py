from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel

from gui.view.panel_elements.battery_current_widget import BatteryCurrentWidget
from gui.view.panel_elements.battery_temperature_widget import BatteryTemperatureWidget
from gui.view.panel_elements.text_sensor_widget import TextSensorWidget
from gui.view.panels.abstract_panel import AbstractPanel


class AccuboxPanel(AbstractPanel):
    def __init__(self):
        super().__init__()

        # Layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Test counter
        # self.battery_temperature_widget = BatteryTemperatureWidget(1)
        # main_layout.addWidget(self.battery_temperature_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        #
        # self.battery_current_widget = BatteryCurrentWidget()
        # main_layout.addWidget(self.battery_current_widget)

        self.rpm_widget = TextSensorWidget("Motor RPM", 1112)
        main_layout.addWidget(self.rpm_widget)
