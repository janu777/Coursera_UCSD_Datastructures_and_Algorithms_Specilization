#python3

def greatest_common_divisor(a,b):
	while b:
		a,b = b, a%b 
	return a

if __name__ == '__main__':
	a,b = map(int,input().split())
	print(greatest_common_divisor(a,b))