class Node:

	next_node = None

	def __init__(self, data):
		self.data = data

	def __repr__(self):
		return "<Node: %s>" % self.data


class LinkedList:
	
	def __init__(self):
		self.head = None

	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.next_node
		return count

	def add(self, data):
		new_node = Node(data)
		new_node.next_node = self.head
		self.head = new_node

	def is_empty(self):
		return self.head == None

	def search(self, key):
		current = self.head
		while current:
			if current == key:
				return current
			else:
				current = current.next_node
		return None



	def __repr__(self):
		nodes = []
		current = self.head
		while current:
			if current is self.head:
				nodes.append("[Head: %s]" % current.data)
			elif current.next_node is None:
				nodes.append("[Tail: %s]" % current.data)
			else:
				 nodes.append("[%s]" % current.data)
			current = current.next_node
		return "-> ".join(nodes)