import sys
from string import String
from matrix import *
from math import *

def display_key(key):
	lines = 0
	cols = 0
	while lines != key.lines:
		cols = 0
		while cols != key.cols:
			print (key.matrice[lines][cols], end = '')
			if cols + 1 != key.cols:
				print ("	", end = '')
			cols = cols + 1
		print ()
		lines = lines + 1

def display_message_encrypted(matrice):
	lines = 0
	cols = 0
	print ("Encrypted message :")
	while lines != matrice.lines:
		cols = 0
		while cols != matrice.cols:
			print (matrice.matrice[lines][cols], end = '')
			print (" ", end = '')
			cols = cols + 1
		lines = lines + 1
	print ()

def display_encrypted(key, matrice):
	print ("Key matrix :")
	display_key(key)
	print ()
	display_message_encrypted(matrice);

def encrypted():
	key = String(sys.argv[2])
	key = Key_matrix(key)
	message = String(sys.argv[1])
	message = Message_matrix(message, key)
	matrice = message.multiplication(key)
	display_encrypted(key, matrice)
