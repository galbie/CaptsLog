from PySide import QtCore, QtGui

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


class Entry_Widget(QtGui.QWidget):
    """Set up Journal Entry.

    This widget allows users to type in their journal
    to be converted to markdown format.

    """

    def __init__(self, parent):
        """Initialize Journal Entry.

        Set up the caller function as reference when
        this class is initiated. Then calls
        the entry_layout function.

        """
        super(Entry_Widget, self).__init__(parent)
        self.entry_layout(parent)

    def entry_layout(self, parent):
        """Add box layout for Journal Entry.

        This function adds a box layout in the middle of the central widget
        and calls __JournalEntry funtion.

        """
        self.journalEntryLayout = QtGui.QHBoxLayout()
        # self.journalEntryLayout.setMargin(11)
        self.journalEntryLayout.setSpacing(6)
        self.journalEntryLayout.setObjectName(_fromUtf8("journalEntryLayout"))
        self.__JournalEntry(parent)
        self.journalEntryLayout.addWidget(self.journalEntry)
        parent.horizontalLayout_7.addLayout(self.journalEntryLayout)

    def __JournalEntry(self, parent):
        """Set up QPlainTextEdit.

        This function create a Plain Text Editor as the input for the user.

        The size of this widget scales along with the window size.

        """
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
