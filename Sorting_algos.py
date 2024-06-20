class Solution:	
	def sort_by_length(self,lst: List[str] ->) None:
		"""
		Sorts a list of stings by the length of each string
		"""
		lst.sort(key = lambda x: len(x))

	def selection_sort(self, lst: List[int]) -> None:
		# i is the current index
		for i in range(len(lst)):
			min_index = i
			for j in range(i +1, len(lst)):
				# find the smallest value in the sub-list
				if lst[j] < lst[min_index]:
					min_index = j
			lst[i], lst[min_index] = lst[min_index], lst[i]