class Node:
	"""
	Node is a self referencial data that encapsulate a value.
	It usually holds reference to other nodes in the storage address.
	"""
	next_node = None

	def __init__(self, data):
		self.data = data

	def __repr__(self):
		return "<Node: %s>" % self.data


class LinkedList:
	"""
	Singly Linked List is a kind of data structure the holds reference to the data after it with the help of a node.
	Since it's singly linked list, we'll only hold reference to the head node in memory.
	"""

	def __init__(self):
		self.head = None


	def prepend(self, data):
		""" It adds data and make the new data the head of the list with losing reference to the previous head of the list. """
		current = self.head
		new_node = Node(data)

		self.head = new_node
		new_node.next_node = current


	def append(self, data):
		""" It adds data to the end of the list. """
		current = self.head
		new_node = Node(data)

		if self.head == None:
			self.head = new_node
		else:
			while current.next_node is not None:
				current = current.next_node

			current.next_node = new_node


	def is_empty(self):
		# Convenience method
		return self.head == None


	def len(self):
		""" It returns the length of list. - 1 based count """
		count = 0
		current = self.head
		while current:
			count += 1
			current = current.next_node

		return count


	def index(self, index):
		""" It returns the key at a given in the list. - 0 based count. """
		current = self.head
		position = 0
		while current:
			if position == index:
				return current
			else:
				current = current.next_node
				position += 1

		return None

		
	def insert(self, data, index):
		"""
		It adds data to any given position of the list.
		0 based count
		"""
		if index == 0:
			self.prepend(data)

		if index > 0:
			current = self.head
			position = index
			new_node = Node(data)
			while position > 1:
				position -= 1
				current = current.next_node

			prev_node = current
			next_node = current.next_node

			prev_node.next_node = new_node
			new_node.next_node = next_node


	def extend(self, data):
		""" It runs loop on group of values and add them singularly to in linked list. """
		for x in data:
			self.append(x)


	def pop(self, index=-1):
		"""
		It removes and returns value of a given position.
		When position is provided, it removes the very last data in the list.
		0 based count.
		"""
		if index <= -1:
			current = self.head
			size = self.len()

			while size > 2:
				current = current.next_node
				size -= 1

			item = current.next_node
			current.next_node = None
			return item.data
		else:
			if index == 0:
				current = self.head
				self.head = current.next_node
				return current.data
			else:
				current = self.head
				position = index
		
				while position > 1:
					position -= 1
					current = current.next_node

				prev_node = current
				next_node = current.next_node

				target = prev_node.next_node

				prev_node.next_node = next_node.next_node

				return target.data


	def remove(self, index):
		""" It removes data at a given position from the list. - 0 based count. """
		# Remove at index
		if index == 0:
			current = self.head
			self.head = current.next_node

		if index > 0:
			current = self.head
			position = index

			while position > 1:
				position -= 1
				current = current.next_node

			prev_node = current
			next_node = current.next_node

			prev_node.next_node = next_node.next_node


	def delete(self, key):
		""" Removes node containing data that matches """
		current = self.head
		prev_node = None
		found = None

		while current and not found:
			if current.data == key and current == self.head:
				found = True
				self.head = current.next_node
			elif current.data == key:
				found = True
				prev_node.next_node = current.next_node
			else:
				prev_node = current
				current = current.next_node


	def clear(self):
		""" It clears the entire list """
		self.head = None


	def __repr__(self):
		current = self.head
		nodes = []
		while current:
			if current == self.head:
				nodes.append("[Head: %s]" % current.data)
			elif current.next_node is None:
				nodes.append("[Tail: %s]" % current.data)
			else:
				nodes.append("[%s]" % current.data)
			current = current.next_node
		return "-> ".join(nodes)