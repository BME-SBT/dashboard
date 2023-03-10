from PySide6.QtWidgets import QVBoxLayout, QLabel

from Dashboard.view.panel_elements.battery_current_widget import BatteryCurrentWidget
from Dashboard.view.panel_elements.battery_temperature_widget import BatteryTemperatureWidget
from Dashboard.view.panels.abstract_panel import AbstractPanel


class AccuboxPanel(AbstractPanel):
    def __init__(self):
        super().__init__()

        # Main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Test counter
        counter_label = QLabel('3')
        main_layout.addWidget(counter_label)

        self.battery_temperature_widget = BatteryTemperatureWidget(1)
        main_layout.addWidget(self.battery_temperature_widget)

        self.battery_current_widget = BatteryCurrentWidget()
        main_layout.addWidget(self.battery_current_widget)
