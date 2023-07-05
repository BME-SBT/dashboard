from PySide2.QtWidgets import QLabel, QVBoxLayout

from data.sensor import SensorState
from gui.view.panel_elements.abstract_panel_elements.abstract_panel_element import AbstractPanelElement
from gui.view.panel_elements.bar_widget import BarWidget
from gui.view.colors import Colors
from data.sensor_ids import SensorId
from gui.view.panel_elements.text_sensor_widget import TextSensorWidget


class LowestCellVoltageTextWidget(TextSensorWidget):
    def __init__(self):
        super().__init__(title='L.Cell', sensor_id=SensorId.LOWEST_CELL_VOLTAGE.value)

