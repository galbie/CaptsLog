#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  filemanagement.py
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

import bisect
import codecs								#The codecs library is used for reading/writing text files in Python
import copy_reg								#Used for saving and loading files that contain arbitrary Python data structures
import cPickle					
import gzip									#Used to compress the text files and "Pickle" data
from PyQt4.QtCore import *
from PyQt4.QtXml import *

CODEC = "UTF-8"								#UTF-8 bit codec for text files
NEWPARA = UNICHR(0x2029)					#One byte for each ASCII Character, 2 or more bytes for any other characters
NEWLINE = UNICHR(0X2028)

class Journal(object):
	UNKNOWNDATA = 0000 
	UNKNOWNLENGTH = 0
	
	def __init__(self, title = None, data = UNKNOWNDATA,
	length = UNKNOWNLENGTH, lastupdated = None, notes = None):
		
		self.title = title
		self.data = data
		self.length = length
		self.lastupdated = lastupdated \
			if lastupdated is not None else QDate.currentDate()
		self.notes = notes

class JournalContainer(object):
	MAGIC_NUMBER = 0x3051E					#Magic Number and File Version are constants used for saving and loading files
	FILE_VERSION = 100						#Using PyQt's QDataStream class
	
	def __init__(self):			
		self.__fname = Qstring()			#Journal's file name is held as a Qstring() function
		self.journals = []					#
		self.__journalFromId = {}
		self.__dirty = False
	
	def __iter__(self):
		for pair in iter(self.__journals):	#Iterates over the ordered list of journals and returns the journal items for each entry
			yield pair[1]
	
	def __len__(self):
		return len(self.__journals)
		
	def clear(self, clearFilename = True):	#This function clears the information from the Journal entry
		self.__journals = []
		self.__journalFromId = {}
		if clearFilename:
			self.__fname = Qstring()
		self.__dirty = False
		
	def add(self, journal):					#This function adds a journal entry to the table
		if id(journal) in self.__journalFromId:
			return False
		key = self.key(journal.title, journal.year)
		bisect.insort_left(self.__journals, [key, journal])
		self.__journalFromId[id(journal)] = journal
		self.__dirty = True
		return True
	
	def key(self, title, data):				#Keys are used to ensure that journal entries with the same title aren't entered twice.
		text = unicode(title).lower()
		if text.startswith("a "):
			text = text[2:]
		elif text.startswith("an "):
			text = text[3:]
		elif text.startswith("the "):
			text = text[4:]
		parts = text.split(" ", 1)
		if parts[0].isdigit():
			text = "%08d " % int(parts[0])
			if len(parts) > 1:
				text += parts[1]
		return u"%s\t%d" % (text.replace(" ", ""), year)
		
		
	
	def delete(self, journal):
		if id(journal) not in self.__journalFromId:
			return False
		key = self.key(journal.title, movie.data)
		i = bisect.bisect_left(self.__journals, [key, journals])
		del self.__journals[i]
		del self.__journalFromId[id(journal)]
		self.__dirty = True
		return True
	
	def updateJournal(self, journal, title, data, length = None, notes = None): #After a journal has been deleted, the table needs to be updated
		
		if length is not None:
			journal.length = length
		if notes is not None:
			journal.notes = notes
		if title != journal.title or data != journal.date:
			key = self.key(journal.title, journal.data)
			i = bisect.bisect_left(self.__journals, [key, journal])
			self.__journals[i][0] = self.key(title, data)
			journal.title = title
			journal.date = date
			self.__journals.sort()
		self.__dirty = True
					
	@staticmethod
	def formats():							
		return "*.mqb *. mpb *.mqt *.mpt "		#Data formats
												#.mqb is Qt binary format
												#.mpb is also Pickle python format
												#.mqt is Qxt text format
												#.mpt is Python text format
	
	def save(self, fname = Qstring()):			#File save function
												#Depending on the file format, the proper PyQt save function will be called
		if not fname.isEmpty():
			self.__fname = fname
		if self.__fname.endsWith(".mqb"):
			return self.saveQDataStream()
		elif self.__fname.endsWith(".mpb"):
			return self.savePickle()
		elif self.__fname.endsWith(".mqt"):
			return self.saveQTextStream()
		elif self.__fname.endsWith(".mpt"):
			return self.saveText()
		return False
		
	#def saveQDataStream(self):
	#	error = None
	#	fh = None
	#	try:
	#		fh = QFile(self.__fname)
	#		if not fh.open(QIOD	
		
			
	def saveQTextStream(self):
		error = None 
		fh = None
		try:
			fh = QFile(self.__fname)
			if not fh.open(QIODevice.WriteOnly):
				raise IOerror, unicode(fh.errorString())
			stream = QTextStream(fh)
			stream.setCodec(CODEC)
			for key, journal in self.__journals:
				stream << "{{JOURNAL}} " << journal.title << "\n" \
					   << journal.date << " " << journal.length << " " \
					   << journal.lastupdated.toString(Qt.ISODate) \
					   << "\n{NOTES}"
				if not journal.notes.isEmpty():
					stream << "\" << journal.notes
				stream << "\n {{ENDJOURNAL}}\N"
	
	def intFromQstr(qstr):
		i, ok = qstr.toInt()
		if not ok:
			raise ValueError, unicode(qstr)
		return i		
# Refer back to page 251 
def main():
	
	return 0

if __name__ == '__main__':
	main()

