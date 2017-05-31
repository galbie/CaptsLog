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


class List_Widget(QtGui.QWidget):
    """Set up Journal Entry.

    This widget allows users to manage their journals.
	Users are able to create, delete, select and edit their journals.

    """

    def __init__(self, parent):
        """Initialize Journal Entry.

        Set up the caller function as reference when
        this class is initiated. Then calls
        the list_layout function.

        """
        super(List_Widget, self).__init__(parent)
        self.list_layout(parent)

    def list_layout(self, parent):
        """Add box layout for Journal List.

        This function adds a box layout in the middle of the central widget
        and calls __JournalList funtion.

        """
        self.journalTableLayout = QtGui.QHBoxLayout()
        self.journalTableLayout.setMargin(11)
        self.journalTableLayout.setSpacing(6)
        self.journalTableLayout.setObjectName(_fromUtf8("journalTableLayout"))
        self.__JournalList()
        self.journalTableLayout.addWidget(self.journalList)
        self.horizontalLayout_7.addLayout(self.journalTableLayout)

    def __JournalList(self, parent):
        """Journal List widget."""
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