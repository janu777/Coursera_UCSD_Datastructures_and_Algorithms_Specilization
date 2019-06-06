#python3
import numpy as np

def last_digit_sum_fibonacci_inrange(m,n):
	f_series = [0,1]
	if n <= 1:
		return n
	elif m<=1:
		last_digit_sum_inrange = 1
	else:
		last_digit_sum_inrange = 0
	flag = 0
	N = n
	M = m
	for i in range(2,n+1):
		f_series.append((f_series[i-1]+f_series[i-2])%10)
		if i>=m:
			last_digit_sum_inrange=(last_digit_sum_inrange+f_series[i])%10
		if f_series[i-1] == 0 and f_series[i] == 1 and flag == 0:
			periodic_length = len(f_series)-2
			n = n%periodic_length
			m = m%periodic_length
			flag = 1
			if n<=N:
				break
	if flag == 1:
		Q = (M-m)//periodic_length
		K = (N-n)//periodic_length
		last_digit_sum_inrange = ((sum(f_series)-1)*K+sum(f_series[:n+1])-(sum(f_series)-1)*Q-sum(f_series[:m]))%10 
	
	return last_digit_sum_inrange

if __name__=='__main__':
	m,n = map(int,input().split())
	print(last_digit_sum_fibonacci_inrange(m,n))