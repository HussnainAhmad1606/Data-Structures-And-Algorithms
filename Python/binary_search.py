def binary_search(list1, target):
	first = 0
	last = len(list1) - 1

	while first <= last:
		midpoint = first+last // 2
		if list1[midpoint] == target:
			return midpoint
		elif list1[midpoint] < target:
			first = midpoint + 1	
		else:
			last = midpoint - 1

	return None

numbers = [54, 56, 87, 23, 95]
numbers.sort()
print(binary_search(numbers, 87))
