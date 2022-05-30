import sys

from PySide6 import QtWidgets

from PiMapObj.PiLayer import PiLayer
from PiMapObj.PiProjection import PiProjection
from PiMapObj.PiShow import PiWindow

if __name__ == "__main__":
    layer = PiLayer()
    layer2 = PiLayer()
    layer3 = PiLayer()
    proj = PiProjection()
    # layer.load("图层文件/省会城市.lay")
    # layer.load("图层文件/国界线.lay")
    # print(layer.fields)
    layer.load("PiMapObj/图层文件/省级行政区.lay")
    layer2.load("PiMapObj/图层文件/国界线.lay")
    layer3.load("PiMapObj/图层文件/省会城市.lay")
    proj.load("PiMapObj/图层文件/图层文件坐标系统说明.txt")

    app = QtWidgets.QApplication(sys.argv)
    main = PiWindow()
    main.figure.add_layer(layer, proj)
    main.figure.add_layer(layer2, proj)
    main.figure.add_layer(layer3, proj)
    main.show()
    sys.exit(app.exec())

    # print(layer.get_geometry_type())
    # print(layer.get_fields())
