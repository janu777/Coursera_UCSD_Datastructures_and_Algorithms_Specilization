# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    sorted_segments = ([i[0] for i in sorted(enumerate([a[0] for a in segments]), key=lambda x:x[1])])
    k = 0
    current_list = []
    while(k<len(segments)-1):
        if current_list:
            current_start,current_end = current_list
        else:
            current_start,current_end = segments[sorted_segments[k]]
        if segments[sorted_segments[k+1]][0]<=current_end:
            if segments[sorted_segments[k+1]][1]<=current_end:
                current_list = [segments[sorted_segments[k+1]][0],segments[sorted_segments[k+1]][1]]
            else:
                current_list = [segments[sorted_segments[k+1]][0],current_end]
        else:
            points.append(current_end)
            current_list = []
        k+=1
    if current_list:
        points.append(current_list[1])
    else:
        points.append(segments[sorted_segments[k]][1])
    return points

if __name__ == '__main__':
    n = int(input())
    segments = []
    for i in range(n):
        segments.append(list(map(int,input().split())))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
