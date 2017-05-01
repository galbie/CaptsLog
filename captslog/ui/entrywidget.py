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

# Journal Entry Class which contains the layout and widget


class Entry_Widget(QtGui.QWidget):

    def __init__(self, parent):
        super(Entry_Widget, self).__init__(parent)
        self.entry_layout(parent)

    # Entry Layout
    def entry_layout(self, parent):
        self.journalEntryLayout = QtGui.QHBoxLayout()
        self.journalEntryLayout.setMargin(11)
        self.journalEntryLayout.setSpacing(6)
        self.journalEntryLayout.setObjectName(_fromUtf8("journalEntryLayout"))
        self.__JournalEntry(parent)
        self.journalEntryLayout.addWidget(self.journalEntry)
        parent.horizontalLayout_7.addLayout(self.journalEntryLayout)

    # Entry Widget
    def __JournalEntry(self, parent):
        self.journalEntry = QtGui.QPlainTextEdit(parent.centralWidget)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.journalEntry.sizePolicy().hasHeightForWidth())
        self.journalEntry.setSizePolicy(sizePolicy)
        self.journalEntry.setMinimumSize(QtCore.QSize(200, 600))
        self.journalEntry.setObjectName(_fromUtf8("journalEntry"))
