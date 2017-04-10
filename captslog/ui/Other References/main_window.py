import sys

from PySide import QtGui, QtCore
import markdown

from editor import UI_MainWindow


class MainWindow(object):

    def __init__(self, parent=None):
        self.editor = UI_MainWindow()
        self.ui = QtGui.QMainWindow()
        self.editor.setupUi(self.ui)
        self.editor.txtInput.textChanged.connect(self.textChange)

    def textChange(self):
        raw = self.ui.txtInput.toPlainText()
        md = markdown.convert(raw)
        self.ui.txtOutput.setHtml(md)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MW = MainWindow()
    MW.ui.show()
    sys.exit(app.exec_())
