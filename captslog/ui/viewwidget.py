from PyQt4 import QtCore, QtGui

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

#Journal View Class which contains the layout and widget		
class View_Widget(QtGui.QWidget):
	
	def __init__(self, parent):
		super(View_Widget, self).__init__(parent)
		self.view_layout(parent)
	
	#View Layout
	def view_layout(self, parent):
		self.journalViewLayout = QtGui.QHBoxLayout()
		self.journalViewLayout.setMargin(11)
		self.journalViewLayout.setSpacing(6)
		self.journalViewLayout.setObjectName(_fromUtf8("journalViewLayout"))
		self.__JournalView(parent)
		self.journalViewLayout.addWidget(self.journalView)
		parent.horizontalLayout_7.addLayout(self.journalViewLayout)
	
	#View Widget
	def __JournalView(self, parent):
		self.journalView = QtGui.QTextEdit(parent.centralWidget)
		self.journalView.setMinimumSize(QtCore.QSize(200, 600))
		self.journalView.setObjectName(_fromUtf8("journalView"))
		self.journalView.setReadOnly(True)

