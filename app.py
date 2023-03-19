import sys

from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtWidgets import QMainWindow, QApplication

from Dashboard.dummy_data_generator import DummyDataGenerator
from Dashboard.view.main_container import MainContainer


class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Style settings
        self.setFixedSize(1024, 600)
        self.setContentsMargins(0, 0, 0, 0)

        # Create main container
        self.main_container = MainContainer()
        self.setCentralWidget(self.main_container)

        # Style refresh shortcut
        refresh_shortcut = QShortcut(QKeySequence('Ctrl+R'), self)
        refresh_shortcut.activated.connect(self.init_stylesheet)

    def init_stylesheet(self):
        qss_path = './view/style.qss'
        with open(qss_path, 'r') as qss_file:
            self.setStyleSheet(qss_file.read())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    dummy_generator = DummyDataGenerator()
    dummy_generator.start()

    dashboard = DashboardWindow()
    dashboard.init_stylesheet()
    dashboard.show()

    sys.exit(app.exec())
