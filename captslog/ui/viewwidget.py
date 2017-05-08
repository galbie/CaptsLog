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


class View_Widget(QtGui.QWidget):
    """Set up Journal View.

    This widget acts as the output for the markdown converted html text.

    """
    def __init__(self, parent):
        """Initialize Journal View.

        Set up the caller function as reference when
        this class is initiated. Then calls
        the view_layout function.

        """
        super(View_Widget, self).__init__(parent)
        self.view_layout(parent)

    def view_layout(self, parent):
        """Add box layout for Journal View.

        This function adds a box layout in the right side of the central widget
        and calls __JournalView funtion.

        """
        self.journalViewLayout = QtGui.QHBoxLayout()
        #self.journalViewLayout.setMargin(11)
        self.journalViewLayout.setSpacing(6)
        self.journalViewLayout.setObjectName(_fromUtf8("journalViewLayout"))
        self.__JournalView(parent)
        self.journalViewLayout.addWidget(self.journalView)
        parent.horizontalLayout_7.addLayout(self.journalViewLayout)

    def __JournalView(self, parent):
        """Set up QPlainTextEdit.

        This function creates a Text Editor that cathces the output text from
        the mardown function and displays the html text.

        The size of this widget scales along with the window size.

        Note : The user should not be able to input any text in this widget.

        """
        self.journalView = QtGui.QTextEdit(parent.centralWidget)
        self.journalView.setMinimumSize(QtCore.QSize(200, 600))
        self.journalView.setObjectName(_fromUtf8("journalView"))
        self.journalView.setReadOnly(True)
