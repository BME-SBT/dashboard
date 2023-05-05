from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout

from gui.view.panel_elements.battery_current_widget import BatteryCurrentWidget
from gui.view.panel_elements.battery_temperature_widget import BatteryTemperatureWidget


class PermanentPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(850, 100)

        # Style
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)

        # Layout
        main_layout = QHBoxLayout(self)

        # Panel elements
        self.battery_temperature_widget = BatteryTemperatureWidget()
        self.battery_current_widget = BatteryCurrentWidget()

        main_layout.addWidget(self.battery_temperature_widget)
        main_layout.addWidget(self.battery_current_widget)
