from PyQt4 import QtCore, QtGui
from entrywidget import Entry_Widget
from viewwidget import View_Widget

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

#Collection of all widgets
class CentralWidget(QtGui.QWidget):
	def __init__(self, parent):
		super(CentralWidget, self).__init__(parent)
		self.__CentralWidget()
		self.__HorizLayout()
		
	
	#Central Widget
	def __CentralWidget(self):
		self.centralWidget = QtGui.QWidget(self)
		sizePolicy = QtGui.QSizePolicy(
			QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.centralWidget.sizePolicy().hasHeightForWidth())
		self.centralWidget.setSizePolicy(sizePolicy)
		self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
	
	# Horizontal Layout 7, Journal Table, Entry, and View
	def __HorizLayout(self):
		self.horizontalLayout_7 = QtGui.QHBoxLayout(self.centralWidget)
		self.horizontalLayout_7.setMargin(11)
		self.horizontalLayout_7.setSpacing(6)
		self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
		
		self.journalTableLayout = QtGui.QHBoxLayout()
		self.journalTableLayout.setMargin(11)
		self.journalTableLayout.setSpacing(6)
		self.journalTableLayout.setObjectName(_fromUtf8("journalTableLayout"))
		self.__JournalList()
		self.journalTableLayout.addWidget(self.journalList)
		self.horizontalLayout_7.addLayout(self.journalTableLayout)
		
		self.entry = Entry_Widget(self)
		
		self.view = View_Widget(self)
			
		self.setLayout(self.horizontalLayout_7)
		
	
	# Journal List
	def __JournalList(self):
		self.journalList = QtGui.QListWidget(self.centralWidget)
		sizePolicy = QtGui.QSizePolicy(
			QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.journalList.sizePolicy().hasHeightForWidth())
		self.journalList.setSizePolicy(sizePolicy)
		self.journalList.setMinimumSize(QtCore.QSize(100, 600))
		self.journalList.setMaximumSize(QtCore.QSize(250, 16777215))
		self.journalList.setObjectName(_fromUtf8("journalList"))
