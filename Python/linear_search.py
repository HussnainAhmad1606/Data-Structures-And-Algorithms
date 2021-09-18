def linear_search(list1, target):
	for i in range(len(list1)):
		if list1[i] == target:
			return i


arr = [54, 34, 65, 98, 100]
print(linear_search(arr, 34))