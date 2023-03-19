from PySide6.QtCore import Signal

from Dashboard.view.sidebars.side_bar import SideBar


class RightBar(SideBar):
    """The right sidebar with button markers."""
    sig_next_panel = Signal()

    def __init__(self):
        super().__init__()

        self.first_btn.setText('CUS')
        self.second_btn.setText('>')
        self.third_btn.setText('ENT')

        # Button style
        self.first_btn.setProperty('side', 'right')
        self.second_btn.setProperty('side', 'right')
        self.third_btn.setProperty('side', 'right')

        # Connect signals
        self.second_btn.clicked.connect(self.sig_next_panel)
