from PySide6.QtCore import Signal

from Dashboard.view.sidebars.side_bar import SideBar


class LeftBar(SideBar):
    """The left sidebar with button markers."""
    sig_previous_panel = Signal()

    def __init__(self):
        super().__init__()

        self.first_btn.setText('M')
        self.second_btn.setText('<')
        self.third_btn.setText('ESC')

        # Connect signals
        self.second_btn.clicked.connect(self.sig_previous_panel)
