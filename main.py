#!/usr/bin/python

import pygtk
pygtk.require('2.0')
import gtk
class Base:
		def __init__(puzz):
			puzz.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

			puzz.window.set_border_width(200)	
			puzz.window.set_title("Magic Puzzle")
			puzz.window.connect("delete_event", puzz.delete_event)
			
			puzz.box_main = gtk.HBox(False, 0)
				
			puzz.button=gtk.Button("testme")	
			puzz.button.connect("clicked",puzz.hello,None)	
			

			puzz.window.add(puzz.button)
			puzz.window.add(puzz.box_main)				


			puzz.button.show()			
			puzz.window.show() 
	
		
		def hello(puzz, widget, data=None):
			print "testme data"
	
		def delete_event(self, widget, event, data=None):
			gtk.main_quit()
			return False	
		
		def main(puzz):
			gtk.main()

if __name__ == "__main__" :
	base = Base()
	base.main()


