from PySide6.QtWidgets import QVBoxLayout, QLabel

from Dashboard.view.panels.abstract_panel import AbstractPanel


class SolarboxPanel(AbstractPanel):
    def __init__(self):
        super().__init__()

        # Main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Test counter
        counter_label = QLabel('2')
        main_layout.addWidget(counter_label)