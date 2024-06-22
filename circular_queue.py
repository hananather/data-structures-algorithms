class CircularQueue:
	def __init__(self, queue, front, rear, size):
		self.queue = [None] * size
		self.max_size. = size
		self.front = -1
		self.rear = -1

	def is_full(self) -> bool:
		# check if the first position of rear is circularly is equal to front
		return ((self.rear +1) % self.max_size == self.front) 
	def is_empty()