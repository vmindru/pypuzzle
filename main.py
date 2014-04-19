#!/usr/bin/python

import pygtk
pygtk.require('2.0')
import gtk
class Base:
		def __init__(puzz):
			puzz.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
			puzz.window.set_border_width(200)	
			puzz.button=gtk.Button("testme")	
			puzz.button.connect("clicked",puzz.hello,None)	
			puzz.window.add(puzz.button)
			puzz.window.show() 
			puzz.button.show()			

	
		def main(puzz):
			gtk.main()
		
		def hello(puzz, widget, data=None):
			print "testme data"

if __name__ == "__main__" :
	base = Base()
	base.main()


