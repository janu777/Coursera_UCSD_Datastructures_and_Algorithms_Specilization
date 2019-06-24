# Uses python3
import sys

def get_change(m):
	change = 0
	i = 0
	denominations = [10,5,1]
	while(m):
		if m-denominations[i] >= 0:
			m-=denominations[i]
			change+=1
		else:
			i+=1
	return change

if __name__ == '__main__':
	m = int(input())
	print(get_change(m))
