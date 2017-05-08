<<<<<<< HEAD
=======
from PyQt4 import QtCore, QtGui
# from PySide import QtCore, QtGui
>>>>>>> refs/remotes/jaehoonhwang/master
from centralwidget import CentralWidget

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


class Ui_MainWindow(QtGui.QMainWindow):
    """MainWindow class

    This is the main class for GUI, it calls initiation from the CentralWidget
    class, which generates the main content of GUI.

    """
    def setupUi(self, MainWindow):
        """Set up the Main Window.

        This function does three main things: set an initial size
        for the window, set up the central widget, and the menu bar.

        Attributes:
            sizePolicy (QSizePolicy) : Window size setting.
            _layout (QHBoxLayout) : layout for central widget to
                                    scale along with window.

        """
        self.setObjectName(_fromUtf8("MainWindow"))
        self.resize(550, 600)

        # Size Policy
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sizePolicy().hasHeightForWidth())

        # Main Window
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setDocumentMode(False)
        self.center_widget = CentralWidget(MainWindow)
        _widget = QtGui.QWidget()
        _layout = QtGui.QVBoxLayout(_widget)
        _layout.addWidget(self.center_widget)
        MainWindow.setCentralWidget(_widget)

        # Menu Bar
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 550, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.actionNew_Entry = QtGui.QAction(MainWindow)
        self.actionNew_Entry.setObjectName(_fromUtf8("actionNew_Entry"))
        self.menuFile.addAction(self.actionNew_Entry)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.action_edit_entry = QtGui.QAction(MainWindow)
        self.action_edit_entry.setObjectName(_fromUtf8("action_Edit_Entry"))
        self.menuFile.addAction(self.action_edit_entry)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.action_Save_Entry = QtGui.QAction(MainWindow)
        self.action_Save_Entry.setObjectName(_fromUtf8("action_Save_Entry"))
        self.menuFile.addAction(self.action_Save_Entry)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.action_Delete_Entry = QtGui.QAction(MainWindow)
        self.action_Delete_Entry.setObjectName(_fromUtf8("action_Delete_Entry"))
        self.menuFile.addAction(self.action_Delete_Entry)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.action_Cancel = QtGui.QAction(MainWindow)
        self.action_Cancel.setObjectName(_fromUtf8("action_Cancel"))
        self.menuFile.addAction(self.action_Cancel)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """Language translation.

        This function exist in case of multi languages are introduce
        to the program.

        """
        MainWindow.setWindowTitle(_translate("Captslog", "Captslog", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionNew_Entry.setText(
            _translate("MainWindow", "New Entry", None))
        self.action_edit_entry.setText(
            _translate("MainWindow", "Edit Entry", None))
        self.action_Save_Entry.setText(
            _translate("MainWindow", "Save Entry", None))
        self.action_Delete_Entry.setText(
            _translate("MainWindow", "Delete Entry", None))
        self.action_Cancel.setText(
            _translate("MainWindow", "Cancel", None))
