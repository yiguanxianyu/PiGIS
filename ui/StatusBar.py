from PySide6.QtWidgets import QStatusBar, QLabel, QComboBox
from constants import *

scales_num = [100000000, 50000000, 25000000, 10000000, 5000000, 2500000, 1000000, 500000, 250000, 100000, 50000,
              25000, 10000, 5000, 2000, 1000, 500]
scales_str = ['test'] + [f'1:{i}' for i in scales_num]


class PiStatusBar(QStatusBar):
    def __init__(self, mainwindow):
        super(PiStatusBar, self).__init__(mainwindow)
        self.setMinimumHeight(30)
        self.setMaximumHeight(30)

        self.addWidget(
            QLabel(f'v{PiGIS_MAJOR_VERSION}.{PiGIS_MINOR_VERSION}.{PiGIS_PATCH_VERSION}\t')
        )

        self.loc_label = QLabel('X: Y:')
        self.addWidget(self.loc_label)

        qcb = QComboBox(self)
        qcb.setEditable(True)
        qcb.addItems(scales_str)
        qcb.insertSeparator(1)
        self.addWidget(qcb)

    def update_mouse_loc(self, x, y):
        self.loc_label.setText(f'X:{x}  Y:{y}')
