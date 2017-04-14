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
		
class Main(QtGui.QMainWindow):
	
	def __init__(self, parent=None):
		super(Main, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.center_widget.journalEntry.textChanged.connect(self.text_changed)
		self.wire_keys()
	
	def text_changed(self):
		raw = self.ui.center_widget.journalEntry.toPlainText()
		md = markdown.Markdown()
		raw = str(raw)
		ntxt = md.convert(raw)
		self.ui.center_widget.journalView.setHtml(ntxt)
	
	def keyPressEvent(self, ev):
		if ev.modifiers() & QtCore.Qt.ControlModifier\
			and ev.key() in self.ctrl_keys:
			return self.ctrl_keys[ev.key()](ev)
		if ev.modifiers() & QtCore.Qt.AltModifier and ev.key() in self.mod_keys:
			return self.mod_keys[ev.key()](ev)
		if ev.key() in self.keys:
			return self.keys[ev.key()](ev)

	def _help(self, ev):
		print "showing help"

	def _save(self, ev):
		print "saving file"

	def _open(self, ev):
		print "opening file"

	def wire_keys(self):
		self.ctrl_keys = {
			QtCore.Qt.Key_S: self._save,
			QtCore.Qt.Key_O: self._open,
		}
		self.mod_keys = {

		}
		self.keys = {
			QtCore.Qt.Key_F1: self._help,
        }
		

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	Form = Main()
	Form.show()
	sys.exit(app.exec_())