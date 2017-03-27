from .editor import Ui_MainWindow
import markdown


class MainWindow(gui.QMainWindow):

    def __init(self, parent=None):
        self.markdown = Markdown()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.txtInput.textChanged.conenct(self.textChange)

    def textChange(self):
        raw = self.ui.txtInput.toPlainText()
        md = self.markdown.convert(raw)
        self.ui.txtOutput.setHtml(md)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myMain = MainWindow()
    myMain.show()
    sys.exit(app.exec_())
