from PySide6.QtWidgets import QRubberBand
from PiMapObj.PiLayer import PiLayer
from PySide6.QtWidgets import QRubberBand

from PiMapObj.PiLayer import PiLayer


# import pyqtgraph as pg

class PiGraphEdit():
    def __init__(self, view) -> None:
        self.view = view
        self.edit_on = PiLayer()
        self.select_rb = QRubberBand(QRubberBand.Rectangle, self.view)
        self.edit_rb = QRubberBand(QRubberBand.Line, self.view)
