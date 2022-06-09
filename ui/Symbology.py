from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPen, QBrush
from PySide6.QtWidgets import QDialog, QPushButton, QColorDialog
from numpy import linspace

from ui.raw import Ui_Symbology

pen_style = [Qt.NoPen, Qt.SolidLine, Qt.DashLine, Qt.DotLine, Qt.DashDotLine, Qt.DashDotDotLine]

pen_join = [Qt.BevelJoin, Qt.MiterJoin, Qt.RoundJoin]


class SymbologyPage(QDialog):
    def __init__(self, parent, levels, fields):
        super().__init__(parent)
        self.unique_level = levels
        # self.fields = fields
        self.ui = Ui_Symbology()
        self.ui.setupUi(self)
        self.current_index = 0
        self.border_width = '1'
        self.border_join = 0
        self.border_type = 0
        self.level_size = 2
        self.border_color = QColor()
        self.single_color = QColor()
        self.begin_color = QColor()
        self.end_color = QColor()

        self.border_width_linedit = [self.ui.borderWidth_0, self.ui.borderWidth_1, self.ui.borderWidth_2]
        self.border_color_buttons = [self.ui.borderColor_0, self.ui.borderColor_1, self.ui.borderColor_2]
        self.border_join_combobox = [self.ui.borderJoinCombo_0, self.ui.borderJoinCombo_1, self.ui.borderJoinCombo_2]
        self.border_type_combobox = [self.ui.borderTypeCombo_0, self.ui.borderTypeCombo_1, self.ui.borderTypeCombo_2]
        self.begin_color_buttons = [self.ui.beginColor_1, self.ui.beginColor_2]
        self.end_color_buttons = [self.ui.endColor_1, self.ui.endColor_2]
        self.single_color_buttons = [self.ui.singleColor]

        self.ui.fieldsComboBox.addItems(fields)

    @staticmethod
    def set_button_color(button: QPushButton, color: QColor):
        br, bg, bb, _ = color.getRgb()
        style_sheet = f'background:rgb({br},{bg},{bb});color:rgb({255 - br},{255 - bg},{255 - bb})'
        button.setStyleSheet(style_sheet)

    def index_changed(self, index):
        self.current_index = index

    def field_id_changed(self, index):
        self.ui.levelNumberLabel.setText(f'levels: {self.unique_level[index]}')

    def get_gradient_colors(self, num: int) -> list[QColor]:
        br, bg, bb, _ = self.begin_color.getRgbF()
        er, eg, eb, _ = self.end_color.getRgbF()
        red = linspace(br, er, num)
        green = linspace(bg, eg, num)
        blue = linspace(bb, eb, num)
        return [QColor.fromRgbF(red[i], green[i], blue[i]) for i in range(num)]

    def set_begin_color(self):
        color = QColorDialog.getColor()
        self.begin_color = color
        for button in self.begin_color_buttons:
            self.set_button_color(button, color)

    def set_end_color(self):
        color = QColorDialog.getColor()
        self.end_color = color
        for button in self.end_color_buttons:
            self.set_button_color(button, color)

    def set_single_color(self):
        color = QColorDialog.getColor()
        self.single_color = color
        for button in self.single_color_buttons:
            self.set_button_color(button, color)

    def set_border_width(self, text):
        self.border_width = text
        for line_edit in self.border_width_linedit:
            line_edit.setText(text)

    def set_border_type(self, index):
        self.border_type = index
        for item in self.border_type_combobox:
            item.setCurrentIndex(index)

    def set_border_join(self, index):
        self.border_join = index
        for item in self.border_join_combobox:
            item.setCurrentIndex(index)

    def set_border_color(self):
        color = QColorDialog.getColor()
        self.border_color = color
        for button in self.border_color_buttons:
            self.set_button_color(button, color)

    def set_bl_level_size(self, index):
        self.level_size = index + 2

    def dialog_accept(self, *args):
        print('acc')

    def dialog_reject(self, *args):
        print('rej')

    def result(self):
        width = float(self.border_width)
        pen = QPen(self.border_color, width, pen_style[self.border_type])
        pen.setJoinStyle(pen_join[self.border_join])

        match self.current_index:
            case 0:  # 唯一值
                return pen, self.get_gradient_colors(self.unique_level)
            case 1:  # 分级
                return pen, self.get_gradient_colors(self.level_size)
            case 2:  # 单值
                return pen, QBrush(self.single_color)
            case _:
                raise ValueError('Page does not exist.')
