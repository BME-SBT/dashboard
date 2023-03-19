from PySide6.QtWidgets import QLabel

from Dashboard.view.panels.abstract_panel import AbstractPanel


class SolarboxPanel(AbstractPanel):
    def __init__(self):
        super().__init__(title='SolarboxPanel')

        # Example:
        # self.panel_container.addWidget(example)
