from Deque_Generator import get_deque

class Stack:

	def __init__(self):
		self._dq = get_deque()
		
	def __str__(self):
		# TODO replace pass with your implementation.
		return(str(self._dq))
		
	def __len__(self):
		# TODO replace pass with your implementation.
		return(len(self._dq))
		
	def push(self, val):
		# TODO replace pass with your implementation.
		self._dq.push_front(val)
		
	def pop(self):
		# TODO replace pass with your implementation.
		return self._dq.pop_front()
		
	def peek(self):
		# TODO replace pass with your implementation.
		return (self._dq.peek_front())
		
# Unit tests make the main section unneccessary.
if __name__ == '__main__':
	pass
