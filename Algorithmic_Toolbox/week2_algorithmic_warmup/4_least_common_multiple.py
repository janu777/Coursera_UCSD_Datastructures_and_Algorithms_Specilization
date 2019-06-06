#python3

def least_common_multiple(a,b):
	A = a
	B = b
	while b:
		a,b = b, a%b
	lcm = (A*B)//a 	
	return int(lcm)

if __name__ == '__main__':
	a,b = map(int,input().split())
	print(least_common_multiple(a,b))