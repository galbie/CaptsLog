#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
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

#Import the libraries needed for PyQt
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt, QtUrl
from PyQt4.QtGui import QApplication
from PyQt4.QtWebKit import QWebew

#Import the libraries needed for PyMarkdown

class Main(QtGui.QMainWindow):
	
	#Initialize the main window of the application 
	def __init__(self, parent = None):
		QtGui.QMainWindow.__init__(self, parent)
		
		self.initUI()
		
	def initUI(self):
	
		#Location of the editor window in width and height
		self.setGeometry(100, 100, 1030, 800)
		
		self.setWindowTitle("CaptsLog") 
		
		#Sets default tab width in the editor
		self.text.setTabStopWidth(33)
		
		#Placeholder windows icon
		self.setWindowIcon(QtGui.QIcon("board.png"))
		
		#Displays the cursor's current position in the toolbar
		self.text.cursorPositionChanged.connect(self.cursorPosition)

	
	def cursorPosition(self):

		cursor = self.text.textCursor()

		line = cursor.blockNumber() + 1
		col = cursor.columnNUmber()
		
	def main():
	
		app = QtGui.QApplication(sys.argv)
	
		main = Main()
		main.show()
	
		sys.exit(app.exec_())

	if __name__ == '__main__':
		main()
	
	def initToolbar(self):
	
		#Creates an Options Menu
		self.toolbar = self.addToolBar("Options")
	
		self.addToolBarBreak()

	def initFormatbar(self):
	
		#Creates a Format menu
		self.formatbar = self.addToolBar("Format")

	def initMenubar(self):
	
		menubar = self.menuBar()
	
		#Creates objects for the toolbar menus
		file = menubar.addMenu("File")
		edit = menubar.addMenu("Edit")
		view = menubar.addMenu("View")
		
		file.addAction(self.newAction)
		file.addAction(self.openAction)
		file.addAction(self.saveAction)
		file.addAction(self.printAction)
		file.addAction(self.previewAction)
		
		edit.addAction(self.undoAction)
		edit.addAction(self.redoAction)
		edit.addAction(self.cutAction)
		edit.addAction(self.copyAction)
		edit.addAction(self.pasteAction)
	

#Creates a QTextEdit object as the main PyQt object.
#Then initialize the three menu toolbars to appear at the top of the editor
#These will contain the markdown functions to be displayed in the editor
	def initUI(self):
	
		self.text = QtGui.QTextEdit(self)
		self.setCentralWidget(self.text)
	
		self.initToolbar()
		self.initFormatbar()
		self.initMenubar()
	
	#Creates a statusbar for the window
		self.statusbar = self.statusBar()
	
	#Coordinates for the main PyQt widget
		self.setGeometry(100, 100, 1030, 800)
	
		self.setWindowTitle("CaptsLog")
	
	def preview(self):
		
		#Open preview window
		preview = QtGui.QprintPreviewDialog()
		
		#If a print is requested, open a print dialog
		preview.paintRequested.connect(lambda p: self.text.print_(p))
		
		preview.exec_()
		
	def print(self):
	
		#Open printing window
		dialog = QtGui.QPrintDialog()
		
		if dialog.exec_() == QtGui.QDialog.Accepted:
			self.text.document().print_(dialog.printer())
			
	def bulletList(self):
		
		cursor = self.text.textCursor()
		
		cursor.insertText(" * ")
		cursor.setWordWrap(true)
	
	def numberList(self):
		
		cursor = self.text.textCursor()
		
		cursor.insertText("1"
		cursor.setWordWrap(true)

	def __init__(self, parent = None):
	
		QtGui.QMainWindow.__init__(self, parent)
	
		self.filename = " "
	
		self.initUI()
	
	def initToolbar(self):
	
	#Initializes the toolbar menu options for New, Open, and Save functions
	#Also sets their descriptions, shortcuts, and actions
	
		self.newAction = QtGui.QAction(QtGui.QIcon("/board.png"), "New", self)
		self.newAction.setStatusTip("Create a new Journal entry.")
		self.newAction.setShortcut("Ctrl + N")
		self.newAction.triggered.connect(self.new)
	
		self.openAction = QtGui.QAction(QtGui.QIcon("board.png"), "Open file", self)
		self.openAction.setStatusTip("Open existing journal entry")
		self.openAction.setShortcut("Ctrl + O")
		self.openAction.triggered.connect(self.open)
	
		self.saveAction = QtGui.QAction(QtGui.QIcon("board.png"), "Save", self)
		self.saveAction.setStatusTip("Save journal entry")
		self.saveAction.setShortcut("Ctrl + S")
		self.saveAction.triggered.connect(self.save)
	
		self.toolbar = self.addToolBar("Options")
		
		self.printAction = QtGui.QAction(QtGui.QIcon("board.png"), "Print journal", self)
		self.printAction.setStatusTip("Print journal entry")
		self.printAction.setShortcut("Ctrl + P")
		self.printAction.triggered.connect(self.print)
		
		self.previewAction = QtGui.QAction(QtGui.QIcon("board.png"), "Journal preview", self)
		self.previewAction.setStatusTip("Preview journal before printing"
		self.previewAction.setShortcut("Ctrl + Shift + P")
		self.previewAction.triggered.connect(self.preview)
		
		self.cutAction = QtGui.QAction(QtGui.QIcon("board.png"), "Cut to clipboard", self)
		self.cutAction.setStatusTip("Delete this text and copy the text to the clipboard")
		self.cutAction.setShortcut("Ctrl + x")
		self.cutAction.triggered.connect(self.text.cut)
		
		self.copyAction = QtGui.QAction(QtGui.QIcon("board.png"), "Copy to the clipboard", self)
		self.copyAction.setStatusTip("Copy text to the clipboard")
		self.copyAction.setShortcut("Ctrl + C")
		self.copyAction.triggered.connect(self.text.copy)
		
		self.pasteAction = QtGui.QAction(QtGui.QIcon("board.png"), "Paste from clipboard", self)
		self.pastAction.setStatusTip("Pastes text from the clipboard
		self.pasteAction.setShortcut("Ctrl + V")
		self.pasteAction.triggered.connect(self.text.paste)
		
		self.undoAction = QtGui.QAction(QtGui.QIcon("board.png"), "Undo last action", self)
		self.undoAction.setStatusTip("Undo last action")
		self.undoAction.setShortcut("Ctrl + Z")
		self.undoAction.triggered.connect(self.text.undo)
		
		self.redoAction = QtGui.QAction(QtGui.QIcon("board.png"), "Redo last action", self)
		self.redoAction.setStatusTip("Redo last action")
		self.redoAction.setShortcut("Ctrl + Y")
		self.redoAction.triggered.connect(self.text.undo)
		
		self.bulletAction = QtGui.QAction(QtGui.QIcon("board.png"), "Insert bulleted list", self)
		bulletAction.setStatusTip("Insert bullet list")
		bulletAction.setShortcut("Ctrl + Shift + B")
		bulletAction.triggered.connect(self.bulletList)
		
		numberedAction = QtGui.QAction(QtGui.QIcon("board.png"), "Insert numbered list", self)
		numberedAction.setStatusTip("Insert numbered list")
		numberedAction.setShortcut("Ctrl + Shift + L")
		numberedAction.triggered.connect(self.numberList)
		
	
		self.toolbar.addAction(self.newAction)
		self.toolbar.addAction(self.openAction)
		self.toolbar.addAction(self.saveAction)
	
	#Formats and separates the toolbar menus
		self.toolbar.addSeparator()
		
		self.toolbar.addAction(self.printAction)
		self.toolbar.addAction(self.previewAction)
		
		self.toolbar.addSeparator()
		
		self.toolbar.addAction(self.cutAction)
		self.toolbar.addAction(self.copyAction)
		self.toolbar.addAction(self.pasteAction)
		self.toolbar.addAction(self.undoAction)
		self.toolbar.addAction(self.redoAction)
		
		self.toolbar.addSeparator()
		
		self.toolbar.addAction(bulletAction)
		self.toolbar.addAction(numberedAction)
		
		
		self.addToolBarBreak()
	
	

	
	
	def new(self):
		
		spawn = Main(self)
		spawn.show()
	#Set to only open files with a .txt extension
	def open(self):
		
		#Get the journal entry name and filetype
		self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File',
		".", "(*.txt)")
		
		if self.filename:
			with open(self.filename, "rt") as file:
				self.text.setText(file.read())
				
	def save(self):
		
		#If the file has no name, open this window
		if not self.filename:
			self.filename = QtGui.QFileDialog.getSaveFileName(self, 'Save FIle')
			
		if not self.filename.endswith(".txt"):
			self.filename += ".txt."
		
		#Stores the contents of the text file in html
		
		with open(self.filename, "wt") as file:
			file.write(self.text.toHtml())
			

		
