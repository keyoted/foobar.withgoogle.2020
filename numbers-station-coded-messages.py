#!/bin/python

def solution(l, t):
	for index in range(0, len(l)-1):
		sum = 0
		for i in range(index, len(l)):
			sum += l[i]
			if sum > t:
				break
			elif sum == t:
				return [index, i]
	return [-1,-1]

print(solution([4, 3, 5, 7, 8], 12))
print(solution([1, 2, 3, 4], 15))
print(solution([4, 3, 10, 2, 8], 12))