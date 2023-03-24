from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget


class TopBar(QWidget):
    """The top bar that contains the warning icons."""
    def __init__(self):
        super().__init__()

        # Style
        self.setFixedHeight(50)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
