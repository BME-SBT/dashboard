from PySide6.QtWidgets import QVBoxLayout, QLabel

from Dashboard.view.panel_elements.battery_current_widget import BatteryCurrentWidget
from Dashboard.view.panel_elements.battery_temperature_widget import BatteryTemperatureWidget
from Dashboard.view.panels.abstract_panel import AbstractPanel


class AccuboxPanel(AbstractPanel):
    def __init__(self):
        super().__init__(title='AccuboxPanel')

        # Test counter
        self.battery_temperature_widget = BatteryTemperatureWidget(1)
        self.panel_container.addWidget(self.battery_temperature_widget)

        self.battery_current_widget = BatteryCurrentWidget()
        self.panel_container.addWidget(self.battery_current_widget)
