def binarySearch(alist, item):
	first = 0
	last = len(alist) - 1
	found = -1
	alist.sort()
	while first <= last and found == -1:
		midpoint = (first + last) // 2		
		if alist[midpoint] == item:
			found = midpoint
		else:
			if item < alist[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1
	return found

if __name__ == '__main__':
	print("Enter the array items separated by spaces \n")
	inparray = list(map(int, input().split()))
	inparray.sort()
	print("Enter the item to search for \n")
	tosearch = int(input())

	print("Sorted array is:", inparray)
	print("Number to search is:", tosearch)

	if(binarySearch(inparray, tosearch) == -1):
		print("Number not found in array")
	else:
		print("Number found at",binarySearch(inparray, tosearch), "position in sorted array by binary search.")
		
	
