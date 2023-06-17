from PySide2.QtCore import Qt
from PySide2.QtWidgets import QVBoxLayout, QLabel

from gui.view.panel_elements.home_panel.battery_current_widget import BatteryCurrentWidget
from gui.view.panel_elements.home_panel.battery_temperature_widget import BatteryTemperatureWidget
from gui.view.panel_elements.text_sensor_widget import TextSensorWidget
from gui.view.panels.abstract_panel import AbstractPanel
from gui.view.panel_elements.icon_value_widget import IconValueWidget

class IconValueGroupWidget(AbstractPanel):
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

        self.mppt_charger_voltage = IconValueWidget("charger voltage", 1112, 'V')
        self.mppt_charger_current = IconValueWidget("charger current", 1112, 'V')
        main_layout.addWidget(self.mppt_charger_voltage)
        main_layout.addWidget(self.mppt_charger_current)