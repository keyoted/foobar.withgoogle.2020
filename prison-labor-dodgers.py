#!/bin/python

def solution(x,y):
	if len(x) > len(y):
		longA = x
		shortA = y
	else:
		longA = y
		shortA = x

	for l in longA:
		gotIt = False
		for s in shortA:
			if l == s:
				gotIt = True
				break
		if not gotIt:
			return l

x=[14, 27, 1, 4, 2, 50, 3, 1]
y=[2, 4, -4, 3, 1, 1, 14, 27, 50]

print(solution(y,x))