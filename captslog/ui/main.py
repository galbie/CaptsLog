from __future__ import absolute_import, unicode_literals
from PyQt4 import QtCore, QtGui
from captslog.db.DBHandler import DBHandlerClass
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


# Main class
class Main(QtGui.QMainWindow):
    """Main Control class.

    This is the main class that controls GUI and DataBase.

    """

    def __init__(self, parent=None):
        """Initiate GUI and Database.

        Args:
            db_handler (DBHandlerClass) : calls and initialize database.
            ui (QMainWindow) : calls and initialize main window.

        """
        self.db_handler = DBHandlerClass()
        super(Main, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.center_widget.entry.journalEntry.textChanged.connect(
            self.text_triggered)
        self.ui.center_widget.journalList.currentItemChanged.connect(
            self.itemChanged)
        results = self.db_handler.get_all()
        for x in results:
            item = QtGui.QListWidgetItem('Title: ' + str(x['Title']))
            item.setToolTip(str(x["_id"]))
            self.ui.center_widget.journalList.addItem(item)

    def text_triggered(self):
        """Update text to markdown text simultaneously.

        Args:
            raw (String) : Recieves the string from entry every time an input
            is made
            ntxt (html string) : Converted html string

        """
        raw = self.ui.center_widget.entry.journalEntry.toPlainText()
        md = markdown.Markdown()
        # raw = raw.encode('utf-8')
        ntxt = md.convert(raw)
        self.ui.center_widget.view.journalView.setHtml(ntxt)

    def itemChanged(self):
        """Not my portion."""
        item = self.ui.center_widget.journalList.currentItem()
        result = self.db_handler.search_entries_by_id(item.toolTip())[0]

        st = result["MarkdownFile"].encode('utf-8')

        print(st)
        self.ui.center_widget.entry.journalEntry.setPlainText(st)
        self.text_triggered()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = Main()
    Form.show()
    sys.exit(app.exec_())
