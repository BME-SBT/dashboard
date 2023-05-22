from PySide6.QtWidgets import QVBoxLayout, QLabel
from PySide6.QtGui import QPainter, QColor


from data.sensor import SensorState
from gui.view.panel_elements.abstract_panel_elements.abstract_panel_element import AbstractPanelElement
from gui.view.panel_elements.bar_widget import BarWidget


class MotorTemperatureWidget(AbstractPanelElement):
    # TODO implement custom design
    def __init__(self):
        super().__init__(title='Motor Temperature', sensor_id=0b00010110010)

        # Create main layout
        main_layout = QVBoxLayout(self)

        # Panel name
        name_label = QLabel(self.title)
        main_layout.addWidget(name_label)

        # Panel value
        # self.value_label = QLabel('0')
        # main_layout.addWidget(self.value_label)
        self.bar_widget = BarWidget(100, 200, [0, 20, 45, 70, 100], [QColor(200, 0, 0), QColor(255, 80, 0, 160), QColor(25, 0, 90, 200), QColor(200, 0, 0)], False)
        main_layout.addWidget(self.bar_widget)

    def sensor_state_changed(self, state, old_state):
        if state == SensorState.MISSING_DATA:
            self.value_label.setStyleSheet("color: red")
            # TODO (dani) replace setStyleSheet to setProperty
            self.value_label.setText(self.value_label.text() + " - NO DATA")
        else:
            self.value_label.setStyleSheet("color: black")

    def sensor_value_changed(self, value, old_value):
        self.value_label.setText(f"{value} {self.sensor.data_type.unit}")
