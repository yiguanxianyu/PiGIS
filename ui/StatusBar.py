from PySide6.QtWidgets import QStatusBar, QLabel, QComboBox

from constants import *

scales_num = [
    100000000, 50000000, 25000000, 10000000, 5000000, 2500000, 1000000, 500000,
    250000, 100000, 50000, 25000, 10000, 5000, 2000, 1000, 500
]
scales_str = [f'1:{i}' for i in scales_num]


class PiComboBox(QComboBox):

    def __init__(self, parent, set_scale):
        super(PiComboBox, self).__init__(parent)
        self.setEditable(True)
        self.setInsertPolicy(QComboBox.NoInsert)
        self.addItems(scales_str)
        self.set_scale = set_scale
        self.currentIndexChanged.connect(self.index_changed)

    def focusInEvent(self, e) -> None:
        self.grabKeyboard()

    def focusOutEvent(self, e) -> None:
        self.releaseKeyboard()

    def keyReleaseEvent(self, e) -> None:
        txt = e.text()
        if len(txt) == 1:
            if ord(txt) == 13:
                try:
                    scale = int(self.lineEdit().text()[2:])
                    self.set_scale(scale)
                except Exception as e:
                    print(e)

    def index_changed(self, index):
        self.set_scale(scales_num[index])

    def update_scale(self, scale) -> None:
        self.lineEdit().setText(f'1:{int(scale)}')


class PiStatusBar(QStatusBar):

    def __init__(self, main_window):
        super(PiStatusBar, self).__init__(main_window)
        self.setMinimumHeight(30)
        self.setMaximumHeight(30)

        self.addWidget(QLabel(f'v{PiGIS_MAJOR_VERSION}.{PiGIS_MINOR_VERSION}.{PiGIS_PATCH_VERSION}\t'))

        self.loc_label = QLabel('X: Y:\t')
        self.addWidget(self.loc_label)

        self.qcb = PiComboBox(self, main_window.graphWidget.set_scale)
        self.addWidget(self.qcb)

    def update_coord(self, x, y):
        self.loc_label.setText(f'X:{int(x)}  Y:{int(y)}\t')

    def update_scale(self, scale):
        self.qcb.update_scale(scale)
