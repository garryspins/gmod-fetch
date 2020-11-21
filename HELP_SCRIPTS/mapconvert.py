#
# 	GFetch Map Conversion Script
# 	Read License File
#
#	Script Usage:
#		mapconvert.py input.txt output.txt
#		Converts HTML map image data into command-line images
#
# 	Options:
# 		Positional:
#			1 	  Input File
# 			2 	  Output File
#
#		Optional:
#			-s : --silent   Silent
# 			-o : --output 	Output to StdOut (print it)
#			-n : --nlines 	Dont separate lines with newlines
#
#
#	I Recommend https://www.text-image.com/convert/ for converting images into color ascii art
#
# 	Use the following characters:
# ▓█
# 	With a width of 50 or whatever looks good

import os 
import re
from sys import argv as args
from html.parser import HTMLParser

if len(args) < 2:
	print("Invalid Number of Arguments Given\nRead the file script usage on line 4")
	exit()

def hex_to_rgb(hex):
	hex = hex.replace("#","")
	hlen = len(hex)
	return tuple(int(hex[i:i + hlen // 3], 16) for i in range(0, hlen, hlen // 3))

class html_par(HTMLParser):
	def __init__(self,args):
		super().__init__()
		self.toret = "{"
		self.silent = "-s" in args or "--silent" in args
		self.stdout = "-o" in args or "--output" in args
		self.swnlin = "-n" in args or "--nlines" in args 
		self.separa = "\n"

		if self.swnlin:
			self.separa = ""

		self.args = args

	def handle_starttag(self,tag,attrs):
		aa = dict(attrs)
		if "style" in aa:
			mat = re.match(r"color:#([\dabcdef]+)",aa["style"])
			if mat:
				try:
					hexr,hexg,hexb = hex_to_rgb(mat.group(1))
					col = "Color("+str(hexr)+","+str(hexg)+","+str(hexb)+")"
					self.toret += (col+",")
					if not self.silent: print("Added "+col,str(self.getpos()))
				except:
					if not self.silent: print("Issue adding Color, Skipping")
		elif tag == "font":
			if "color" in aa:
				try:
					hexr,hexg,hexb = hex_to_rgb(aa["color"])
					col = "Color("+str(hexr)+","+str(hexg)+","+str(hexb)+")"
					self.toret += (col+",")
					if not self.silent: print("Added "+col,str(self.getpos()))
				except:
					if not self.silent: print("Issue adding Color, Skipping")




		elif tag == "br":
			try:
				self.toret = self.toret.rstrip(',') + "},"+self.separa+"{"
				if not self.silent: print("Added Newline br")
			except:
				if not self.silent: print("Issue adding Newline, Skipping")

	def handle_data(self, data):
		try:
			if len(data) > 0 and data != "\n":
				data="[["+data+"]]"
				self.toret += (data+",")
				if not self.silent: print("Added "+data,str(self.getpos()))
		except:
			if not self.silent: print("Issue adding Data, Skipping")

	def finishex(self):
		f = open(self.args[2], "w")
		f.write("['mapname_here'] = {"+parser.toret.rstrip(',')+"}}")
		f.close()

	def finish(self):
		if not self.silent: print("Finished")
		if not self.stdout:
			self.finishex()
		else:
			inn = input("The output is most likely not going to fit in your console\nAre you sure you want to print it? [Y/n]: ").lower()
			if inn == "y" or inn == "":
				print("----- BEGIN -----\n\n")
				print("['mapname_here']={"+parser.toret.rstrip(',')+"}}")
				print("\n\n-----  END  -----")
			else:
				self.finishex()

f = open(args[1], "r")
file = f.read()
f.close()

parser = html_par(args)
parser.feed(file)
parser.finish()


