from enum import Enum
from typing import List

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

from Dashboard.view.panels.abstract_panel import AbstractPanel
from Dashboard.view.panels.accubox_panel import AccuboxPanel
from Dashboard.view.panels.motorbox_panel import MotorboxPanel
from Dashboard.view.panels.solarbox_panel import SolarboxPanel


class PanelSwitchDirection(Enum):
    PREVIOUS = -1
    NEXT = 1


class CenterPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.panels: List[AbstractPanel] = [
            SolarboxPanel(),
            AccuboxPanel(),
            MotorboxPanel(),
        ]
        self.current_panel_idx = 1

        # Layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        for panel in self.panels:
            main_layout.addWidget(panel, alignment=Qt.AlignmentFlag.AlignCenter)
            panel.hide()

        self.panels[self.current_panel_idx].show()

    def switch_panel(self, direction: PanelSwitchDirection):
        old_panel_idx = self.current_panel_idx
        self.current_panel_idx = (self.current_panel_idx + direction.value) % len(self.panels)
        old_panel = self.panels[old_panel_idx]
        new_panel = self.panels[self.current_panel_idx]

        old_panel.hide()
        new_panel.show()
