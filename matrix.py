'''/*
** EPITECH PROJECT, 2017
** 103cypher
** File description:
** classe Matrix
*/'''

from math import sqrt
from copy import copy, deepcopy

class Matrix:
	def __init__(self, matrix):
		self.matrice = matrix
		self.lines = len(self.matrice)
		self.cols = len(self.matrice[0])
		if self.lines == self.cols:
			self.inverse()
	def define_matrice(self, lines, cols):
		i = 0
		matrice = [0] * lines
		while i != lines:
			matrice[i] = [0] * cols
			i = i + 1
		return (matrice)
	def define_matrice_identity(self, size):
		matrice = self.define_matrice(size, size)
		i = 0
		while i != size:
			matrice[i][i] = 1
			i = i + 1
		return (matrice)
	def calcul(self, other, lines, cols):
		size = self.cols
		i = 0
		somme = 0
		while i < size:
			somme = somme + (self.matrice[lines][i] * other.matrice[i][cols])
			i = i + 1
		return (somme)
	def multiplication(self, other):
		lines = 0
		cols = 0
		somme = 0
		matrice = self.define_matrice(self.lines, other.cols)
		matrice = Matrix(matrice)
		while lines < matrice.lines:
			cols = 0
			while cols < matrice.cols:
				matrice.matrice[lines][cols] = self.calcul(other, lines, cols)
				cols = cols + 1
			lines = lines + 1
		return (matrice)
	def search_max(self, j):
		i = j
		var = i
		while i != self.lines:
			if abs(self.tmp_matrice[i][j]) > abs(self.tmp_matrice[var][j]):
				var = i
			i = i + 1
		return (var)
	def normalisation(self, k, j):
		pivot = self.tmp_matrice[k][j]
		i = 0
		while i != self.cols:
			self.tmp_matrice[k][i] = self.tmp_matrice[k][i] / pivot
			self.inverse_matrice[k][i] = self.inverse_matrice[k][i] / pivot
			i = i + 1
	def swap(self, k, r):
		tmp = 0
		tmp2 = 0
		i = 0
		while i != self.cols:
			tmp = self.tmp_matrice[k][i]
			self.tmp_matrice[k][i] = self.tmp_matrice[r][i]
			self.tmp_matrice[r][i] = tmp
			tmp2 = self.inverse_matrice[k][i]
			self.inverse_matrice[k][i] = self.inverse_matrice[r][i]
			self.inverse_matrice[r][i] = tmp2
			i = i + 1
	def sub(self, r, i, j):
		cols = 0
		var = 0
		pivot = self.tmp_matrice[i][j]
		while cols != self.cols:
			var = self.tmp_matrice[r][cols] * pivot
			self.tmp_matrice[i][cols] = self.tmp_matrice[i][cols] - var
			var = self.inverse_matrice[r][cols] * pivot
			self.inverse_matrice[i][cols] = self.inverse_matrice[i][cols] - var
			cols = cols + 1
	def simplification(self, r, j):
		i = 0
		while i != self.lines:
			if i != r:
				self.sub(r, i, j)
			i = i + 1
	def inverse(self):
		r = -1
		j = 0
		self.tmp_matrice = deepcopy(self.matrice)
		self.inverse_matrice = self.define_matrice_identity(self.lines)
		while j != self.cols:
			k = self.search_max(j)
			if self.tmp_matrice[k][j] != 0:
				r = r + 1
				self.normalisation(k, j)
				self.swap(k, r)
				self.simplification(r, j)
			j = j + 1

class Key_matrix(Matrix):
	def __init__(self, key):
		self.matrice = self.create_matrice(key)
		Matrix.__init__(self, self.matrice)
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

class Message_matrix(Matrix):
	def __init__(self, message, key):
		self.cols = key.cols
		self.lines = self.determinate_lines(message)
		self.matrice = self.create_matrice(message)
		Matrix.__init__(self, self.matrice)
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
