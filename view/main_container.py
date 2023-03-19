from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout

from Dashboard.view.center_panel import CenterPanel, PanelSwitchDirection
from Dashboard.view.sidebars.left_bar import LeftBar
from Dashboard.view.sidebars.right_bar import RightBar
from Dashboard.view.sidebars.top_bar import TopBar


class MainContainer(QWidget):
    """The main container that contains the switchable pages."""
    def __init__(self):
        super().__init__()

        # Main Layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Top sidebar
        self.top_sidebar = TopBar()

        # Middle part
        self.right_sidebar = RightBar()
        self.left_sidebar = LeftBar()
        self.center_panel = CenterPanel()

        middle_part_layout = QHBoxLayout()
        middle_part_layout.addWidget(self.left_sidebar)
        middle_part_layout.addWidget(self.center_panel)
        middle_part_layout.addWidget(self.right_sidebar)

        # Add layouts to main layout
        main_layout.addWidget(self.top_sidebar)
        main_layout.addLayout(middle_part_layout)

        # Connect signals
        self.right_sidebar.sig_next_panel.connect(
            lambda: self.center_panel.switch_panel(PanelSwitchDirection.NEXT))
        self.left_sidebar.sig_previous_panel.connect(
            lambda: self.center_panel.switch_panel(PanelSwitchDirection.PREVIOUS))
