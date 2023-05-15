nums = [100,200,34,1,23,0,768,102]

def selectionSort(nums):
	for i in range(len(nums)):
		min_index = i
		for j in range(i+1, len(nums)):
			if nums[min_index]>nums[j]:
				min_index = j
		nums[i], nums[min_index] = nums[min_index], nums[i]
	print("Sorted array is:")
	for i in range(len(nums)):
		print(nums[i],end="  ")
	print()
		
selectionSort(nums)
