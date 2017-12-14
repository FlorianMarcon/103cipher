class String:
	def __init__(self, tmp):
		self.str = tmp
		self.size = len(self.str)
		self.tab = self.transcript_str_in_tab()
	def transcript_str_in_tab(self):
		tab = [0] *self.size
		i = 0
		while i != self.size:
			tab[i] = ord(self.str[i])
			i = i + 1
		return (tab)
