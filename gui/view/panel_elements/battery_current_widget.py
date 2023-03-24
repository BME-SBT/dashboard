from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class BatteryCurrentWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create main layout
        main_layout = QVBoxLayout(self)

        # Panel name
        name_label = QLabel('BatCurr')
        main_layout.addWidget(name_label)

        # Panel value
        self.value_label = QLabel('0')
        main_layout.addWidget(self.value_label)

        # Create connections
        # SIG_MANAGER.sig_battery_current_changed.connect(
        #     lambda value: self.value_label.setText(str(value))
        # )
