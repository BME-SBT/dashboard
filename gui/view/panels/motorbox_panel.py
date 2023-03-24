from PySide6.QtWidgets import QVBoxLayout, QLabel

from gui.view.panels.abstract_panel import AbstractPanel


class MotorboxPanel(AbstractPanel):
    def __init__(self):
        super().__init__(title='MotorboxPanel')

        # Example:
        # self.panel_container.addWidget(example)
