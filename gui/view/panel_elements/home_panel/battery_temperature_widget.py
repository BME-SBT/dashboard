from PySide2.QtWidgets import QLabel, QVBoxLayout

from data.sensor import SensorState
from gui.view.panel_elements.abstract_panel_elements.abstract_panel_element import AbstractPanelElement
from gui.view.panel_elements.bar_widget import BarWidget
from gui.view.colors import Colors

class BatteryTemperatureWidget(AbstractPanelElement):
    # TODO implement custom design
    def __init__(self):
        super().__init__(title='Battery Temperature', sensor_id=0b00010010000)

        # Create main layout
        main_layout = QVBoxLayout(self)

        # Panel name
        name_label = QLabel(self.title)
        # main_layout.addWidget(name_label)

        # Panel value
        self.value_label = QLabel('0')
        # main_layout.addWidget(self.value_label)
        self.bar_widget = BarWidget(80, 300, [-10, 0, 40, 65, 85], [Colors.BLUE, Colors.GREEN, Colors.ORANGE, Colors.RED], self.sensor.data_type.unit, 'Bat.Temp', False)
        main_layout.addWidget(self.bar_widget)
        self.sensor_value_changed(50, 50)

    def sensor_state_changed(self, state, old_state):
        self.bar_widget.sensor_state_changed(state)
        if state == SensorState.MISSING_DATA:
            self.value_label.setStyleSheet("color: red")
            # TODO (dani) replace setStyleSheet to setProperty
            self.value_label.setText(self.value_label.text() + " - NO DATA")
        else:
            self.value_label.setStyleSheet("color: black")

    def sensor_value_changed(self, value, old_value):
        #todo
       # self.value_label.setText(f"{value} {self.sensor.data_type.unit}")
       self.bar_widget.sensor_value_changed(value)
