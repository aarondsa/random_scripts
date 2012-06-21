# first python program

class foo():
	def blabber(self, x):
		while x < 10:
			self.x = x
			print x
			x = x + 1

class bar():
	def wabble(self):
		y = 7
		return y
i = foo()
h = bar()

i.blabber(h.wabble())

