from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


from gui.view.colors import Colors
from data.sensor import SensorState
from gui.view.panel_elements.abstract_panel_elements.abstract_panel_element import AbstractPanelElement
from gui.view.panel_elements.bar_widget import BarWidget


class BatteryCurrentWidget(AbstractPanelElement):
    # TODO implement custom design
    def __init__(self):
        super().__init__(title='Battery\nCurrent', sensor_id=0b01001010000)

        # Create main layout
        main_layout = QVBoxLayout(self)

        # Panel value
        self.bar_widget = BarWidget(250, 60, [-35, 0, 50, 150, 200], [Colors.BLUE, Colors.GREEN, Colors.ORANGE, Colors.RED], self.sensor.data_type.unit, 'Bat\nCurrent', True)
        main_layout.addWidget(self.bar_widget)
        self.value_label = QLabel('1')
        # main_layout.addWidget(self.value_label)

        # Panel name
        name_label = QLabel(self.title)
        # main_layout.addWidget(name_label)
        self.sensor_value_changed(100, 50)


    def sensor_state_changed(self, state, old_state):
        self.bar_widget.sensor_state_changed(state)
        if state == SensorState.MISSING_DATA:
            self.value_label.setStyleSheet("color: red")
            # TODO (dani) replace setStyleSheet to setProperty
            self.value_label.setText(self.value_label.text() + " - NO DATA")
        else:
            self.value_label.setStyleSheet("color: black")

    def sensor_value_changed(self, value, old_value):
        #self.value_label.setText(f"{value} {self.sensor.data_type.unit}")
        self.bar_widget.sensor_value_changed(value)
