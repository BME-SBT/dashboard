from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget


class PermanentPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(850, 100)

        # Style
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
