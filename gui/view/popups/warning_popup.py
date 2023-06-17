from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel


class WarningPopup(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)

        label = QLabel('Warning')
        main_layout.addWidget(label)
