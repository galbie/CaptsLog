#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mainwindow.py
#  
#  Copyright 2017 Roark <roark@roark-Satellite-A665>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import os
import platform
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import helpform
import newimagedlg
import qrc_resources

_version_ = "1.0.0"

class MainWindow(QMainWindow):		#Initial declaration of the Main Program window
							
	def __init__(self, parent = None): 
		super(MainWindow, self).__init__(parent)
		
		self.journals = journaldata.JournalContainer()		#Create an empty container for the journals 	
		self.table = QTableWidget()							#Create an empty table widget to present journal metadata
		self.setCentralWidget(self.table)
	
	def updateTable(self, current = None):					#This function just updates the journal entry table.
															#It can be called without arguments, which just updates the table with the newest info															#
															#It can also be called with the ID of the current journal, in which case it selects that Journal entry in the table	
		self.table.clear()
		self.table.setRowCount(len(self.journal))
		self.table.setColumnCount(5)
		self.table.setHorizontalHeaderLabels(["Title", "Data", "Length", "Last Updated", "Notes"])
		self.table.setAlternatingRowColors(True)
		self.table.setEditTriggers(QTableWidget.NoEditTriggers)
		self.table.setSelectionBehavior(QTableWidget.SelectRows)
		self.table.setSelectionMode(QTableWidget.SingleSelection)
		selected = None
		
															#This for loop clears the table data/headings
															#Then sets the row and column counts and headers
															#Then it sets the rest of the journal settings
		for row, journal in enumerate(self.journals):
			item = QTableWidgetItem(journal.title)
			if current is not None and current == id(journal):
				selected = item
			item.setData(Qt.UserRole, QVariant(long(id(journal))))
			self.table.setItem(row, 0, item)
			year = journal.year
			
			if year != journal.UNKNOWNYEAR:
				item = QTableWidgetItem("%d" % year)
				item.setTextAlignment(Qt.AlignCenter)
				self.table.setItem(row, 1, item)
			length = journal.length	
			if length != journal.UNKNOWNLENGTH:
				item = QTableWidgetItem("%d" % length)
				item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
				self.table.setItem(row, 2, item)
			item = QTableWidgetItem(journal.acquired.toString(
			journaldata.DATEFORMAT))
			
			item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
			self.table.setItem(row, 3, item)
			notes = journal.notes
			if notes.length() > 40:
				notes = notes.left(39) + "..."
			self.table.setItem(row, 4, QTableWidgetItem(notes))
			
			self.table.resizeColumnsToContents()
			if selected is not None:
				selected.setSelected(True)
				self.table.setCurrentItem(selected)
				self.table.scrollToItem(selected)
	def fileNew(self):										#This function just creates a new journal table entry
															#Clears out the current journal data
		if not self.okToContinue():
			return
		self.journals.clear()
		self.statusBar().clearMessage()
		self.updateTable()
		
	def fileOpen(self):
		if not self.okToContinue():
			return
		path = QFileInfo(self.journals.filename()).path() \
		if not self.journals.filename().isEMpty() else "."
	frame = QFileDialog.getOpenFileName(self, 
		"My Journals -- Load Journal Data", path,
		"My Journal's data files (%s)" % \
		self.journals.formats())
	if not fname.isEmpty():
		of, msg = self.journals.load(fname)
		self.statusBar().showMessage(msg, 5000)
		self.updateTable()
	
	def fileSave(self):
		if self.journals.filename().isEmpty():
			self.fileSaveAs()
		else:
			ok, msg = self.journals.save()
			self.statusBar().showMessage(msg, 5000)
			
	def fileImportDOM(self):
		self.fileImport("dom")
		
	def fileImportSAX(self):
		self.fileImport("sax")
		
	def fileImport(self, format):
		if not self.okToContinue():
			return
		path = QFileInfo(self.journals.filename()).path() \
			if not self.journals.filename().isEmpty() else "."
		fname = QFileDialog.getOpenFileName(self, 
			"My Journals -- Import Journal Data", path,
			"My Journals XML files (*.xml)")
		if not fname.isEmpty():
				if format == "dom":
					ok, msg = self.journals.importDOM(fname)
				else:
					ok, msg = self.journals.importSAX(fname)
				self.statusBar().showMessage(msg, 5000)
				self.updateTable()
				
	def fileExportXml(self):
		
		fname = self.journals.filename()
		if fname.isEmpty():
			fname = "."
		else:
			i = fname.lastIndex0f(".")
			if i > 0:
				fname = fname.left(i)
			fname += ".xml"
		fname = QFileDialog.getSaveFileName(self,
			"My Journals -- Export Journal Data", fname,
			"My Journal's XML files (*.xml)")
		if not fname.isEmpty():
			if not fname.contains("."):
				fname += ".xml"
			ok, msg = self.journals.exportXml(fname)
			self.statusBar().showMessage(msg, 5000)
		
				
			 
			
			
		
		
		
def main():
	
	return 0

if __name__ == '__main__':
	main()

