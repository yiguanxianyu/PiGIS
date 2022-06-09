from PySide6.QtWidgets import QStatusBar, QLabel, QComboBox

from constants import *

scales_num = [
    100000000, 50000000, 25000000, 10000000, 5000000, 2500000, 1000000, 500000,
    250000, 100000, 50000, 25000, 10000, 5000, 2000, 1000, 500
]
scales_str = ['test'] + [f'1:{i}' for i in scales_num]


class PiComboBox(QComboBox):

    def __init__(self, parent):
        super(PiComboBox, self).__init__(parent)
        self.setEditable(True)
        self.addItems(scales_str)
        self.insertSeparator(1)

    def focusInEvent(self, e) -> None:
        self.grabKeyboard()

    def focusOutEvent(self, e) -> None:
        self.releaseKeyboard()


class PiStatusBar(QStatusBar):

    def __init__(self, main_window):
        super(PiStatusBar, self).__init__(main_window)
        self.setMinimumHeight(30)
        self.setMaximumHeight(30)

        self.addWidget(QLabel(f'v{PiGIS_MAJOR_VERSION}.{PiGIS_MINOR_VERSION}.{PiGIS_PATCH_VERSION}\t'))

        self.loc_label = QLabel('X: Y:\t')
        self.addWidget(self.loc_label)

        self.qcb = PiComboBox(self)
        self.addWidget(self.qcb)

    def update_mouse_loc(self, x, y):
        self.loc_label.setText(f'X:{x}  Y:{y}\t')
