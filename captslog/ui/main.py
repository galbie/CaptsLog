from __future__ import absolute_import, unicode_literals
from PyQt4 import QtCore, QtGui
from mainwindow import Ui_MainWindow
import markdown

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


# Main Control Class		
class Main(QtGui.QMainWindow):
	
	def __init__(self, parent=None):
		super(Main, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.center_widget.journalEntry.textChanged.connect(self.text_changed)
	
	def text_changed(self):
		raw = self.ui.center_widget.journalEntry.toPlainText()
		md = markdown.Markdown()
		raw = str(raw)
		ntxt = md.convert(raw)
		self.ui.center_widget.journalView.setHtml(ntxt)
		

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	Form = Main()
	Form.show()
	sys.exit(app.exec_())