import Node

class Steque:

	def __init__()
		self.head = None
		self.tail = None

	def insert_head(self,node):
		self.head = node
		self.tail = node

	def push(self,value):
		new_node = Node(value)
		if self.head is None:
		    self.insert_head(new_node)
		else:
			curr_head = self.head
			self.head = new_node
			self.head.next = curr_head

	def enqueue(self, value):
		new_node = Node(value)

		if self.tail is None:
			self.insert_head(new_node)
		else:
			curr_tail = self.tail
			curr_tail.next = new_node
			self.tail = new_node

	def pop(self):
		if self.head is None:
			return None
		else:
			val = self.head.get_value()
			curr = self.head
			self.head = curr.next
			curr.next = None
			return val

