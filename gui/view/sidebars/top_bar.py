from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget


class TopBar(QWidget):
    """The top bar that contains the warning icons."""
    def __init__(self):
        super().__init__()

        # Style
        self.setFixedHeight(50)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
