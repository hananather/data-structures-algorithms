class myCircularQueue:

	def __init__(self, k):

		# we create an array size k
		self.queue = [None] * k
		self.front = -1
		self.rear = -1
		self.size = k 
		self.count = 0 

	def enQueue(self, value):
		"""
		:type value: int
		:rtype: bool
		"""
		if not self.isFull:
			next = (self.rear + 1) % self.size
			self.queue[next] = value


	def deQueue(self, value):\
		val = self.queue[self.front]
		next = (self.front + 1) % self.k
		self.front = next
		return val

	def Front(self):
		return self.front

	def Rear(self):
		return self.rear

	def isEmpty(self):
		if self.front == -1 and self.rear == -1
			return True
		else: 
			False

	def isFull(self):

		if (self.front + 1) % self.size == self.rear
			return True
		else:
			return False


