import sys
from encrypted import *
from number import *

def display_encrypted(key, message):
	lines = 0
	cols = 0
	key = round_matrice(key)
	print ("Key matrix :")
	display_key(key)
	print ()
	print ("Decrypted message : ")
	while lines != message.lines:
		cols = 0
		while cols != message.cols:
			print (chr(int(round(message.matrice[lines][cols]))), end = '')
			cols = cols + 1
		lines = lines + 1
	print ()

def round_matrice(matrice):
	lines = 0
	cols = 0
	while lines != matrice.lines:
		cols = 0
		while cols != matrice.cols:
			matrice.matrice[lines][cols] = round(matrice.matrice[lines][cols], 3)
			cols = cols + 1
		lines = lines + 1
	return (matrice)

def decrypted():
	key = String(sys.argv[2])
	key = Key_matrix(key)
	message = Number(sys.argv[1])
	message = Message_matrix(message, key)
	key = key.inverse_matrice
	key = Matrix(key)
	message = message.multiplication(key)
	display_encrypted(key, message)
