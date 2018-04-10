from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from qgis.gui import QgsMapToolEmitPoint

class CreateRectangleTool(QgsMapToolEmitPoint):
    def __init__(self, canvas):
        self.canvas = canvas
        QgsMapToolEmitPoint.__init__(self, self.canvas)

    def canvasPressEvent(self, e):
        point = self.toMapCoordinates(self.canvas.mouseLastXY())
        print('({0}, {1})'.format(point[0], point[1]))

    def canvasReleaseEvent(self, e):
        QApplication.instance().setOverrideCursor(Qt.ArrowCursor)
