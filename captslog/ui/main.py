from __future__ import absolute_import, unicode_literals


from PySide import QtCore, QtGui
from captslog.db.DBHandler import DBHandlerClass

from captslog.ui.mainwindow import Ui_MainWindow
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


# Main Control Class		
class Main(QtGui.QMainWindow):
    def __init__(self, parent=None):
        self.db_handler = DBHandlerClass()
        super(Main, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.center_widget.entry.journalEntry.textChanged.connect(self.text_triggered)
        self.ui.center_widget.journalList.currentItemChanged.connect(self.itemChanged)
        results = self.db_handler.get_all()
        for x in results:
            item = QtGui.QListWidgetItem('Title: ' + str(x['Title']))
            item.setToolTip(str(x["_id"]))
            self.ui.center_widget.journalList.addItem(item)

    def text_triggered(self):
        raw = self.ui.center_widget.entry.journalEntry.toPlainText()
        md = markdown.Markdown()
        #raw = raw.encode('utf-8')
        ntxt = md.convert(raw)
        self.ui.center_widget.view.journalView.setHtml(ntxt)

    def itemChanged(self):
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
