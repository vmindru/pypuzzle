#!/usr/bin/python

import pygtk
pygtk.require('2.0')
import gtk
class Base:
		def __init__(puzz):
			puzz.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
			puzz.window.show() 
			puzz.window.set_border_width(200)	
#			puzz.window.set_border_height(300)
		def main(puzz):
			gtk.main()

if __name__ == "__main__" :
	base = Base()
	base.main()
	time.sleep(5)


