#Uses python3

import sys

def max_dot_product(a, b):
    a = sorted(a)
    b = sorted(b)    
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    n = int(input())
    [*a] = map(int,input().split())
    [*b] = map(int,input().split())
    print(max_dot_product(a, b))
    
