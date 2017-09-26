# Question 5: Show f(x) = f(x-1)**f(x-1), x0 = .5 -> 1 slowly

import matplotlib.pyplot as plt

# Highly unoptimized
# f = lambda x: f(x-1)**f(x-1) if x > 1 else 0.5
# x = map(f, range(0,20))

# Tail recursion
f = lambda x: x + [x[-1]**x[-1]]
def repeat(f, n):
	def rfun(p):
		return reduce(lambda x, _: f(x), range(n), p)
	return rfun

x = repeat(f, 1000)([0.5])
print map(lambda x: abs(x - 1) < 0.001, x).index(True)

# plt.title("Graph of f(x) = f(x-1)**f(x-1)")
# plt.xlabel("x value")
# plt.ylabel("y value")
# plt.plot(x)
# plt.show()