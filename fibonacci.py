fibo_cache={}
def fibo(n):
	if n in fibo_cache:
		return fibo_cache[n]
	if n==1:
		return 1
	elif n==2:
		return 1
	else:
		return fibo(n-1)+fibo(n-2)

	fibo_cache[n]=value
	return value

for i in range(1,100):  #memoization
	print(fibo(i))