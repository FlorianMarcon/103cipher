import re

class Number:
	def __init__(self, tmp):
		self.nb = tmp
		self.size = len(self.nb)
		self.tab = self.transcript_nb_in_tab()
	def transcript_nb_in_tab(self):
		tab = self.nb.split(' ')
		i = 0
		size = len(tab)
		while i != size:
			tab[i] = int(tab[i])
			i = i + 1
		return (tab)
