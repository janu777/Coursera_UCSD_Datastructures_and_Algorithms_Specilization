#python3

def maximum_pairwise_product(variables):
	# max_number1 = 0
	# max_number2 = 0
	# for i in variables:	
	# 	if i > max_number1:
	# 		max_number2 = max_number1
	# 		max_number1 = i
			
	# print(max_number1,max_number2)
	#max_product = max_number1*max_number2
	#return max_product
	variables = sorted(variables, reverse = True)
	max_product = variables[0]*variables[1]
	return max_product

if __name__=='__main__':
	number_of_variables = input()
	variables = list(map(int, input().split()))
	print(maximum_pairwise_product(variables))