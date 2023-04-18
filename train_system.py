from random import randint


class TrainBookingSystem:

	def __init__(self, tickets=[], suite_class=["platinum", "gold", "silver", "bronze"]):
		""" Constructor creates space for keeping tabs of tickets and options for the suite class upon initialization. """

		self.tickets = tickets
		self.suite_class = suite_class
	
	def __repr__(self):
		""" String representation of when all the passengers are queried. """

		return "Use the get_all_tickets method to view all the tickets purchased."

	def book_ticket(self, passenger_name, origin, destination, suite_class, valid=True):
		"""
		To book train ticket:

		- Generate ticket_id to access and update passenger status.
		- All the neccessary info of the user needs to be taken.
		- When the ticket is not used, value of valid is set to True.
		- Check Suite class input to be correct to options available.
		"""

		if suite_class not in self.suite_class:
			return f"{str(suite_class)} is an invalid choice.\n Options are {self.suite_class}"
		ticket_id = ""
		for x in range(6):
			ticket_id += str(randint(1, 9))
		ticket = {ticket_id: dict(
			passenger_name=passenger_name, origin=origin, destination=destination, suite_class=suite_class, valid=valid
		)}
		self.tickets.append(ticket)
		return "Ticket booked successfully."

	def get_all_tickets(self):
		""" Accessible by the staff to get all tickets in the database. """

		for x in self.tickets:
			print(x)
		# return self.tickets

	def get_ticket(self, ticket_id):
		""" Access a particular ticket by it ID. """
		for x in self.tickets:
			for y in x.keys():
				if y == str(ticket_id):
					return x
		return f"No ticket with id: {ticket_id}"

	def get_total_passenger(self):
		""" Get number of passengers. """

		return f"{len(self.tickets)} passengers"

	def verify_ticket(self, ticket_id):
		""" 
		Validating the ticket to be used.
		Changes the value of valid to False since the passenger is on board.
		Helps to restrict passenger using the same ticket more than one time.
		"""
		for item in self.tickets:
			for k, v in item.items():
				if k == str(ticket_id):
					v["valid"] = False
					return "Ticket Verification Done."
		return f"No ticket with id: {ticket_id}"


	def upgrade_class(self, ticket_id, suite_class):
		""" Change the suite_class value in conformity with certified options. """
		for item in self.tickets:
			for k, v in item.items():
				if k == str(ticket_id):
					if str(suite_class) not in self.suite_class:
						return f"{str(suite_class)} is an invalid choice.\n Options are {suite_class}"
					v["suite_class"] = str(suite_class)
					return "Ticket Class Upgrade Done."
		return f"No ticket with id: {ticket_id}"


