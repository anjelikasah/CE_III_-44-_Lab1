def linearSearch(alist, item):
	found = -1
	
	for i in range(len(alist)):
		if alist[i] == item:
			found = i
			break
	return found

if __name__ == '__main__':
	print("Enter the array items separated by spaces \n")
	inparray = list(map(int, input().split()))
	
	print("Enter the item to search for \n")
	tosearch = int(input())

	print("Sorted array is:", inparray)
	print("Number to search is:", tosearch)

	if(linearSearch(inparray, tosearch) == -1):
		print("Number not found in array")
	else:
		print("Number found at", linearSearch(inparray, tosearch), "position in sorted array by linear search.")
