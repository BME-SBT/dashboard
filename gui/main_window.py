from PySide2.QtGui import QKeySequence
from PySide2.QtWidgets import QShortcut, QMainWindow, QApplication
from PySide2.QtCore import Qt

from gui.view.main_container import MainContainer


class DashboardWindow(QMainWindow):
    def __init__(self, can_thread, lcm_thread):
        super().__init__()
        self.can_thread = can_thread  # We own it
        self.lcm_thread = lcm_thread  # We own it
        # Style settings
        self.setFixedSize(1024, 600)
        self.setContentsMargins(0, 0, 0, 0)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        # Create main container
        self.main_container = MainContainer()
        self.setCentralWidget(self.main_container)

        # Style refresh shortcut
        refresh_shortcut = QShortcut(QKeySequence('Ctrl+R'), self)
        refresh_shortcut.activated.connect(self.init_stylesheet)

    def init_stylesheet(self):
        # FIXME: Ez tuti hogy nem fog menni rendesen
        qss_path = './gui/view/style.qss'
        with open(qss_path, 'r') as qss_file:
            self.setStyleSheet(qss_file.read())
