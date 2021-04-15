n = 5

mem = [-1 for i in range(n)]
mem[0] = mem[1] = 1

def fib_pd(n):
	if mem[n - 1] != -1:
		return mem[n - 1]
	mem[n - 1] = fib_pd(n - 1) + fib_pd(n - 2)
	return mem[n - 1]


print(fib_pd(n))

