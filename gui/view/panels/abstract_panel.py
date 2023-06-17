from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget


class AbstractPanel(QWidget):
    def __init__(self):
        super().__init__()

        # Style
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        self.setFixedSize(850, 400)
