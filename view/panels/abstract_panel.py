from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class AbstractPanel(QWidget):
    def __init__(self, title=''):
        super().__init__()

        # Style
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        self.setFixedSize(850, 400)

        # Layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Title
        title_label = QLabel()
        title_label.setProperty('class', 'TitleLabel')
        title_label.setText(title)

        # Panel container
        self.panel_container = QVBoxLayout()

        # Add widgets
        main_layout.addWidget(title_label, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addStretch()
        main_layout.addLayout(self.panel_container)
