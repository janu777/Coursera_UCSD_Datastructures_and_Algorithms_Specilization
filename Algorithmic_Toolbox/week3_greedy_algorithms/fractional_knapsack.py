# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
	value = 0.
	k = 0
	fractions = [values[i]/weights[i] for i in range(len(weights))]
	sorted_fractions = ([i[0] for i in sorted(enumerate(fractions), key=lambda x:x[1], reverse=True)])
	while(capacity and k<len(weights)):
		if capacity-weights[sorted_fractions[k]] >= 0:
			capacity-=weights[sorted_fractions[k]]
			value+=values[sorted_fractions[k]]
		else:
			value+=(values[sorted_fractions[k]]/weights[sorted_fractions[k]])*capacity
			capacity=0 
		k+=1


	return value


if __name__ == "__main__":
	n, capacity = map(int, input().split())
	values = []
	weights = []
	for i in range(n):
		val,wgt = map(int, input().split())
		values.append(val)
		weights.append(wgt)
	opt_value = get_optimal_value(capacity, weights, values)
	print("{:.10f}".format(opt_value))
