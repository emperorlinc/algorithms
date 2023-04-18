class Node:

	prev_node = None
	next_node = None

	def __init__(self, data):
		self.data = data

	def __repr__(self):
		return "[Node: %s]" % self.data


class LinkedList:

	def __init__(self):
		self.head = None
		self.tail = None

	def append(self, data):
		new_node = Node(data)

		if self.head == None:
			self.head = new_node
			self.tail = new_node
		else:
			current = self.tail
			current.next_node = new_node
			new_node.prev_node = current
			self.tail = new_node

	def insert(self, data, index):
		if index == 0:
			current = self.head
			new_node = Node(data)

			new_node.next_node = current
			current.prev_node = new_node

			self.head = new_node
		else:
			position = 1
			current = self.head
			new_node = Node(data)

			while position < index:
				current = current.next_node
				position += 1

			next_node = current.next_node

			if next_node == None:
				# Can simply call self.add here but it's okay like this for practice purpose
				current.next_node = new_node
				new_node.prev_node = current
				self.tail = new_node

			else:
				current.next_node = new_node
				next_node.prev_node = new_node

				new_node.prev_node = current
				new_node.next_node = next_node

	def len(self):
		current = self.head
		count = 1
		while current is not self.tail:
			count += 1
			current = current.next_node
		return count

	def remove(self, key):
		current = self.head
		found = None

		if self.len() == 1 and current.data == key:
			self.head = None
			self.tail = None
		while current and not found:
			if current == self.head and key == current.data:
				found = True
				next_node = current.next_node

				current.next_node =None
				next_node.prev_node = None
				
				self.head = next_node
			
			elif key == current.data:
				found = True
				
				if current.next_node is not None:
					prev_node = current.prev_node
					next_node = current.next_node

					prev_node.next_node = next_node
					next_node.prev_node = prev_node
				else:
					prev_node = current.prev_node

					prev_node.next_node = None
					current.prev_node = None
					self.tail = prev_node

			else:
				current = current.next_node
		return None

	def clear(self):
		self.head = None

	def extend(self, key):
		for x in key:
			self.append(x)

	def pop(self, index=-1):
		# UNFINISHED
		if index == -1:
			current = self.tail
			prev_node = current.prev_node

			prev_node.next_node = None
			current.prev_node = None

			self.tail = prev_node
			
			return current
		
		else:
			position = index
			current = self.head
			while position > 0:
				current = current.next_node
				position -= 1
			
			prev_node = current.prev_node
			next_node = current.next_node

			prev_node.next_node = next_node
			next_node.prev_node = prev_node

			return current

	def __repr__(self):
		nodes = []
		current = self.head

		while current:
			if current == self.head:
				nodes.append("[Head: %s]" % current.data)
			elif current == self.tail:
				nodes.append("[Tail: %s]" % current.data)
			else:
				nodes.append("[%s]" % current.data)

			current = current.next_node
		return "<==> ".join(nodes)
