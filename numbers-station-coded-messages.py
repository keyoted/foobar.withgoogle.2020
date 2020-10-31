#!/bin/python

def solution(list, target):
	for index in range(0, len(list)-1):
		sum = 0
		for i in range(index, len(list)):
			sum += list[i]
			if sum > target:
				break
			elif sum == target:
				return [index, i]
	return [-1,-1]

print(solution([4, 3, 5, 7, 8], 12))
print(solution([1, 2, 3, 4], 15))
print(solution([4, 3, 10, 2, 8], 12))