#!/bin/python

def bbsort(list, predicate):
	i = 0
	while i < len(list)-1:
		if predicate(list[i], list[i+1]) >= 1:	# i > j
			big = list[i]
			list[i] = list[i+1]
			list[i+1] = big
			i = 0
			continue
		i += 1
	return list


def srt(v1, v2):
	major1 = v1[0]
	minor1 = v1[1] if len(v1) > 1 else None
	revis1 = v1[2] if len(v1) > 2 else None

	major2 = v2[0]
	minor2 = v2[1] if len(v2) > 1 else None
	revis2 = v2[2] if len(v2) > 2 else None

	if major1 != major2:
		return major1 - major2
	else:
		if minor1 == None:
			return -1
		elif minor2 == None:
			return 1
		else: 
			if minor1 != minor2:
				return minor1 - minor2
			else:
				if revis1 == None:
					return -1
				elif revis2 == None:
					return 1
				else:
					return revis1 - revis2
		

def solution(l):
	list = []
	for v in l:
		c = v.split(".")
		for i in range(0, len(c)):
			c[i] = int(c[i])
		list += [c]
	bbsort(list, srt)
	strings = []
	for v in list:
		for i in range(0, len(v)):
			v[i] = str(v[i])
		strings += [".".join(v)]
	return strings


print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2", "1", "1.0.0"]))
print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))