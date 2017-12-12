'''/*
** EPITECH PROJECT, 2017
** 103cypher
** File description:
** classe Matrix
*/'''

from math import sqrt

class Key_matrix:
	def __init__(self, key):
		self.matrice = self.create_matrice(key)
		self.lines = len(self.matrice)
		self.cols = self.lines
	def create_matrice(self, key):
		i = 0
		tmp = len(key.tab)
		size = sqrt(tmp)
		if size != int(size):
			size = size + 1
		size = int(size)
		matrice = [0] * size
		while i != size:
			matrice[i] = [0] * size
			i = i + 1
		matrice = self.stock_in_matrice(key, matrice)
		return (matrice)
	def stock_in_matrice(self, key, matrice):
		cols = 0
		lines = 0
		i = 0
		while i != len(key.tab):
			matrice[lines][cols] = key.tab[i]
			i = i + 1
			cols = cols + 1
			if cols == len(matrice):
				cols = 0
				lines = lines + 1
		return (matrice)

class Message_matrix:
	def __init__(self, message, key):
		self.cols = key.cols
		self.lines = self.determinate_lines(message)
		self.matrice = self.create_matrice(message)
	def determinate_lines(self, message):
		size_message = len(message.tab)
		size = size_message / self.cols
		if size != int(size):
			size = size + 1
		size = int(size)
		return (size)
	def create_matrice(self, message):
		i = 0
		matrice = [0] * self.lines
		while i != self.lines:
			matrice[i] = [0] * self.cols
			i = i + 1
		matrice = self.stock_in_matrice(matrice, message)
		return (matrice)
	def stock_in_matrice(self, matrice, message):
		cols = 0
		lines = 0
		i = 0
		while i != len(message.tab):
			matrice[lines][cols] = message.tab[i]
			i = i + 1
			cols = cols + 1
			if cols == self.cols:
				cols = 0
				lines = lines + 1
		return (matrice)

class Matrix:
	def __init__(self, matrix):
		self.matrice = matrix
		self.lines = len(self.matrice)
		self.cols = len(self.matrice[0])

def define_matrice(lines, cols):
	i = 0
	matrice = [0] * lines
	while i != lines:
		matrice[i] = [0] * cols
		i = i + 1
	return (matrice)

def calcul(message, key, lines, cols):
	size = message.cols
	i = 0
	somme = 0
	while i < size:
		somme = somme + (message.matrice[lines][i] * key.matrice[i][cols])
		i = i + 1
	return (somme)

def multiplication(message, key):
	lines = 0
	cols = 0
	somme = 0
	matrice = define_matrice(message.lines, key.cols)
	matrice = Matrix(matrice)
	while lines < matrice.lines:
		cols = 0
		while cols < matrice.cols:
			matrice.matrice[lines][cols] = calcul(message, key, lines, cols)
			cols = cols + 1
		lines = lines + 1
	return (matrice)
