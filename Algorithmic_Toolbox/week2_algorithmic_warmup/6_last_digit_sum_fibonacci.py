#python3

def last_digit_sum_fibonacci(n):
	f_series = [0,1]
	if n <= 1:
		return n
	else:
		last_digit_sum_fibonacci = 1
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
	if flag == 1:
		M = (N-n)//periodic_length
		last_digit_sum_fibonacci = ((sum(f_series)-1)*M+sum(f_series[:n+1]))%10 
	return last_digit_sum_fibonacci

if __name__=='__main__':
	n = int(input())
	print(last_digit_sum_fibonacci(n))