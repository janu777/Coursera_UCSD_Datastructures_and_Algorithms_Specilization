#Uses python3

import sys

# def largest_number(a):
# 	largest_salary = ''
# 	n = len(a)
# 	for i in range(n):
# 		for j in range(0, n-i-1):
# 			if len(a[j]) == len(a[j+1]):
# 				if int(a[j]) < int(a[j+1]):
# 					a[j], a[j+1] = a[j+1], a[j]
# 			else:
# 				digit = 0
# 				flag = 1
# 				while(flag):	
# 					digit_a = 0
# 					digit_b = 0
# 					if len(a[j])-1>=digit:
# 						digit_a = int(a[j][digit])
# 					else:
# 						digit_a = int(a[j][0])
# 						flag = 0

# 					if len(a[j+1])-1>=digit:
# 						digit_b = int(a[j+1][digit])
# 					else:
# 						digit_b = int(a[j+1][0])
# 						flag = 0

					
# 					if digit_a < digit_b:
# 						a[j], a[j+1] = a[j+1], a[j]
# 						flag = 0
# 					elif digit_a == digit_b:
# 						digit+=1
# 					else:
# 						flag = 0
# 	for i in a:
# 		largest_salary+=i

# 	return largest_salary

def largest_number(a):
	largest_salary = ''
	n = len(a)
	for i in range(n):
		for j in range(0, n-i-1):
			if a[j]+a[j+1]<= a[j+1]+a[j]:
				a[j], a[j+1] = a[j+1], a[j]
			
	for i in a:
		largest_salary+=i

	return largest_salary

if __name__ == '__main__':
	
	data = input()
	[*a] = input().split()
	print(largest_number(a))
	
''' sort all the first digits 
	if the first digits are similar then sort the second digits
	continue this until no similar digits are present '''
