#python3

def fibonacci(n):
	f_series = [0,1]
	for i in range(2,n+1):
		f_series.append(f_series[i-1]+f_series[i-2])
	return f_series[n]

if __name__=='__main__':
	n = int(input())
	print(fibonacci(n))