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

