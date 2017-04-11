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
	
	# Horizontal Layout 7, Journal Table, Entry, and View Layout
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
		
		self.journalEntryLayout = QtGui.QHBoxLayout()
		self.journalEntryLayout.setMargin(11)
		self.journalEntryLayout.setSpacing(6)
		self.journalEntryLayout.setObjectName(_fromUtf8("journalEntryLayout"))
		self.__JournalEntry()
		self.journalEntryLayout.addWidget(self.journalEntry)
		self.horizontalLayout_7.addLayout(self.journalEntryLayout)
		
		self.journalViewLayout = QtGui.QHBoxLayout()
		self.journalViewLayout.setMargin(11)
		self.journalViewLayout.setSpacing(6)
		self.journalViewLayout.setObjectName(_fromUtf8("journalViewLayout"))
		self.__JournalView()
		self.journalViewLayout.addWidget(self.journalView)
		self.horizontalLayout_7.addLayout(self.journalViewLayout)
		
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
	
	# Journal Entry
	def __JournalEntry(self):
		self.journalEntry = QtGui.QPlainTextEdit(self.centralWidget)
		sizePolicy = QtGui.QSizePolicy(
			QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.journalEntry.sizePolicy().hasHeightForWidth())   
		self.journalEntry.setSizePolicy(sizePolicy)
		self.journalEntry.setMinimumSize(QtCore.QSize(200, 600))
		self.journalEntry.setObjectName(_fromUtf8("journalEntry"))
	
	def __JournalView(self):
		self.journalView = QtGui.QTextEdit(self.centralWidget)
		self.journalView.setMinimumSize(QtCore.QSize(200, 600))
		self.journalView.setObjectName(_fromUtf8("journalView"))
