# python3
import sys
def compute_min_refills(distance, tank, stops):
	
	refills = 0
	i = 0
	distance_covered = 0
	T=tank
	flag = 0
	if distance_covered+tank<stops[0]:
		return -1
	elif distance_covered+tank>=distance:
		return 0
	stops.append(distance)
	while(distance_covered<distance and i<len(stops)):
		if distance_covered+tank>=stops[i]:
			tank=(distance_covered+tank)-stops[i]
			distance_covered=stops[i]
			i+=1
			flag = 0				
		elif flag==0:
			tank = T
			refills+=1
			flag = 1
		elif flag == 1:
			return -1

	if distance_covered<distance:
		refills = -1
			
	return refills



if __name__ == '__main__':
	d = int(input())
	m = int(input())
	n = int(input())
	[*stops] = map(int, input().split())
	print(compute_min_refills(d, m, stops))
