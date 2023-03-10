from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton


class SideBarButton(QPushButton):
    """Fixed size push button class."""
    def __init__(self):
        super().__init__()
        self.setFixedSize(50, 50)


class SideBar(QWidget):
    """Base class for sidebar widgets."""
    def __init__(self):
        super().__init__()

        # Style
        self.setFixedWidth(50)

        # Layout
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.main_layout)

        # Image Widgets
        # info: Create separate variables to enable more accurate positioning if needed
        self.first_btn = SideBarButton()
        self.second_btn = SideBarButton()
        self.third_btn = SideBarButton()

        self.main_layout.addWidget(self.first_btn)
        self.main_layout.addWidget(self.second_btn)
        self.main_layout.addWidget(self.third_btn)
