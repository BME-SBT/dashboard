from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class ErrorPopup(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)

        label = QLabel('Error')
        main_layout.addWidget(label)
