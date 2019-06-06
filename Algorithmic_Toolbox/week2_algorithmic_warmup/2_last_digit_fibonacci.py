#python3

def last_digit_fibonacci(n):
	f_series = [0,1]
	for i in range(2,n+1):
		f_series.append((f_series[i-1]+f_series[i-2])%10)
	return f_series[n]

if __name__=='__main__':
	n = int(input())
	print(last_digit_fibonacci(n))