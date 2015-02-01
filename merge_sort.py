def merge(list1, list2):
	result = []

	while len(list1) > 0 and len(list2) > 0:
		if list1[0] <= list2[0]:
			result.append(list1[0])
			list1 = list1[1::]
		else:
			result.append(list2[0])
			list2 = list2[1::]

	for i in (list1, list2):
		result.extend(i) if len(i) > 0 else ''

	return result

def merge_sort(num_list):
	list_len =  len(num_list)
	if list_len == 1:
		return num_list
	
	mid = int((list_len)/ 2)
	
	# Split the array into two parts
	list1 = merge_sort(num_list[:mid])
	list2 = merge_sort(num_list[mid:])
	return merge(list1, list2)


def main():
	num_list = range(10)[::-1]
	print "Initial list " + str(num_list)
	print "After sorting " + str(merge_sort(num_list))

if __name__ == '__main__':
	main()
