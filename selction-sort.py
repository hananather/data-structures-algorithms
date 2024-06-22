class Solution
	def selection_sort(self, lst: List[int]) -> None:

		# iterate over every element of the list
		for i in range(len(lst)):
			# find the index of the smallest element in the remaining unsorted portion
			min_index = i
			for j in range(i+ 1, len(lst)):
				if lst[j] < lst[min_index]:
					min_index = j
			lst[i], lst[min_index] = lst[min_index], lst[i]
