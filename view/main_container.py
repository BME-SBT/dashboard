from PySide6.QtWidgets import QWidget, QHBoxLayout

from Dashboard.view.center_panel import CenterPanel, PanelSwitchDirection
from Dashboard.view.sidebars.left_bar import LeftBar
from Dashboard.view.sidebars.right_bar import RightBar


class MainContainer(QWidget):
    """The main container that contains the switchable pages."""
    def __init__(self):
        super().__init__()

        # Main Layout
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(main_layout)

        # Right sidebar
        self.right_sidebar = RightBar()

        # Left sidebar
        self.left_sidebar = LeftBar()

        # Top sidebar
        # TODO implement

        # CenterPanel
        self.center_panel = CenterPanel()

        # Add layouts to main layout
        main_layout.addWidget(self.left_sidebar)
        main_layout.addWidget(self.center_panel)
        main_layout.addWidget(self.right_sidebar)

        # Connect signals
        self.right_sidebar.sig_next_panel.connect(
            lambda: self.center_panel.switch_panel(PanelSwitchDirection.NEXT))
        self.left_sidebar.sig_previous_panel.connect(
            lambda: self.center_panel.switch_panel(PanelSwitchDirection.PREVIOUS))
