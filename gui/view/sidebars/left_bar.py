from PySide6.QtCore import Signal

from gui.view.sidebars.side_bar import SideBar


class LeftBar(SideBar):
    """The left sidebar with button markers."""
    sig_previous_panel = Signal()

    def __init__(self):
        super().__init__()

        self.first_btn.setText('M')
        self.second_btn.setText('<')
        self.third_btn.setText('ESC')

        # Button style
        self.first_btn.setProperty('side', 'left')
        self.second_btn.setProperty('side', 'left')
        self.third_btn.setProperty('side', 'left')

        # Connect signals
        self.second_btn.clicked.connect(self.sig_previous_panel)
