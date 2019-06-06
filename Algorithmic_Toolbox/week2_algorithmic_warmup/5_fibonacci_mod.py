#python3

def fibonacci_mod(n,mod):
	f_series = [0,1]
	flag = 0
	N = n
	for i in range(2,n+1):
		f_series.append((f_series[i-1]+f_series[i-2])%10)
		last_digit_sum_fibonacci=(last_digit_sum_fibonacci+f_series[i])%10
		if f_series[i-1] == 0 and f_series[i] == 1 and flag == 0:
			periodic_length = len(f_series)-2
			n = n%periodic_length
			flag = 1
			if n<=N:
				break
	mod_number = f_series[n]%mod
	return mod_number

if __name__=='__main__':
	n,mod = map(int,input().split())
	print(fibonacci_mod(n,mod))