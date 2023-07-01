from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QLabel
from PySide2.QtCore import QTimer, SIGNAL


class HeartbeatImage(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(None, *args, **kwargs)
        self.setFixedHeight(45)
        self.setFixedWidth(45)

        self.blank_picture = QPixmap("./gui/view/images/blank.png")
        self.warn_image = QPixmap(f"./gui/view/images/heartbeat.png")
        self.visible = False

        self.timer = QTimer(None)
        self.connect(self.timer,SIGNAL('timeout()'),self.timer_update)
        self.timer.singleShot = False
        self.timer.start(500)
        print("HELLLLOOOOO")

    def timer_update(self):
        print("HMMMM")
        self.visible = not self.visible
        self.setPixmap(self.warn_image if self.visible else self.blank_picture)
