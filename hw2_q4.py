import matplotlib.pyplot as plt

# Jumping straight to TOC
f = lambda r: lambda x: x + [r * x[-1] * (1 - x[-1])]

def repeat(f, n):
	def rfun(p):
		return reduce(lambda x, _: f(x), range(n), p)
	return rfun

# Part A
# print repeat(f(1.5), 10)([0.5])

# Part B
rs = [2, 2.5, 3, 3.2, 3.5, 3.52]
sets = [repeat(f(r), 10)([0.5]) for r in rs]

for i in range(len(rs)-1):
	print i
	plt.title(str(rs[i]))
	plt.plot(sets[i])
	plt.show()