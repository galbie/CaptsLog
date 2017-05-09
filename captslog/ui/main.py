from __future__ import absolute_import, unicode_literals

from random import randint

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
        self.current_selection = False
        self.db_handler = DBHandlerClass()
        super(Main, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.center_widget.entry.journalEntry.textChanged.connect(self.text_triggered)
        self.ui.center_widget.journalList.currentItemChanged.connect(self.item_changed)
        self.ui.actionNew_Entry.triggered.connect(self.new_entry_action)
        self.ui.action_Save_Entry.triggered.connect(self.save_button_action)
        self.ui.action_edit_entry.triggered.connect(self.edit_button_action)
        self.ui.action_Delete_Entry.triggered.connect(self.delete_button_action)
        self.ui.action_Cancel.triggered.connect(self.action_button_action)
        self.ui.center_widget.entry.journalEntry.setReadOnly(True)
        self.refresh_list_view()
        self.refresh_list_view()

    def action_button_action(self):
        self.current_selection = None
        self.ui.center_widget.journalList.setEnabled(True)
        self.ui.center_widget.entry.journalEntry.setReadOnly(True)
        self.ui.center_widget.journalList.setEnabled(True)

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

    def item_changed(self):
        """Not my portion."""
        item = self.ui.center_widget.journalList.currentItem()
        result = self.db_handler.search_entries_by_id(item.toolTip())[0]
        st = result["MarkdownFile"].encode('utf-8')

        self.ui.center_widget.entry.journalEntry.setPlainText(st)
        self.text_triggered()

    def remove_all_list(self):
        while self.ui.center_widget.journalList.count() != 0:
            self.ui.center_widget.journalList.clear()

    def refresh_list_view(self):
        self.remove_all_list()
        results = self.db_handler.get_all()

        for x in results:
            item = QtGui.QListWidgetItem('Title: ' + str(x['Title']))
            item.setToolTip(str(x["_id"]))
            self.ui.center_widget.journalList.addItem(item)

    def edit_button_action(self):
        item = self.ui.center_widget.journalList.currentItem()
        self.ui.center_widget.journalList.setEnabled(False)
        self.current_selection = item.toolTip()
        self.ui.center_widget.entry.journalEntry.setReadOnly(False)

    def delete_button_action(self):
        item = self.ui.center_widget.journalList.currentItem()
        result = self.db_handler.delete_entries(item.toolTip())
        self.refresh_list_view()

    def new_entry_action(self):
        self.ui.center_widget.journalList.setEnabled(False)
        self.current_selection = None
        self.ui.center_widget.entry.journalEntry.setReadOnly(False)
        self.ui.center_widget.entry.journalEntry.setPlainText("")

    def save_button_action(self):
        """
        Controls the menu Bar save button click event
        :return: None
        """
        if self.current_selection is not None:
            result = self.db_handler.search_entries_by_id(self.current_selection)[0]
            result["MarkdownFile"] = self.ui.center_widget.entry.journalEntry.toPlainText()
            self.db_handler.update_entries(self.current_selection, result)
        else:
            self.db_handler.insert_to_entries_table(self.get_title(), [],
                                                    self.ui.center_widget.entry.journalEntry.toPlainText())
            self.ui.center_widget.entry.journalEntry.setPlainText("")
            self.current_selection = None
        self.ui.center_widget.journalList.setEnabled(True)
        self.ui.center_widget.entry.journalEntry.setReadOnly(True)
        self.ui.center_widget.journalList.setEnabled(True)
        self.refresh_list_view()

    def get_title(self):
        return "Title "+ str(randint(1,100))
if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    Form = Main()
    Form.show()
    sys.exit(app.exec_())
