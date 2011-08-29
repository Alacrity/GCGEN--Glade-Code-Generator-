#!/usr/bin/env python

#    Copyright@2010 Ganesh.Katrapati
#    This file is part of Glade Code Generator.
#    Glade Code Generator is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    Glade Code Generator is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with Glade Code Generator.  If not, see <http://www.gnu.org/licenses/>.
from xml.dom import minidom
class Search:
	def __init__(self,filename):
		self.xmldoc = minidom.parse(filename)
	def getElementList(self,element,attr):
		reflist = self.xmldoc.getElementsByTagName(element)
		array = []
		for el in reflist:
			array.append(el.attributes[attr].value)
		return array

def getSignals(filename):
	s = Search(filename)
	return s.getElementList("signal","handler")

def getWids(filename):
	s = Search(filename)
	return s.getElementList("widget","id")

