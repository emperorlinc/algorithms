import unittest
from code_test import Robot

class TestRobot(unittest.TestCase):
	def setUp(self):
		self.robot = Robot("Optimus Prime")

	def test_say_name(self):
		self.assertEqual(self.robot.say_name(), "MY NAME IS OPTIMUS PRIME")

	def test_charge(self):
		self.assertEqual(self.robot.charge(), "BATTERY FULLY CHARGED!")

	def test_battery_life(self):
		self.assertEqual(self.robot.battery_life(), 100)

	def test_battery_on_say_name(self):
		self.robot.say_name()
		self.assertTrue(self.robot.battery_life(), 99)

	def test_get_skills(self):
		self.assertEqual(self.robot.get_skills(), [])

	def test_new_skill_added(self):
		self.robot.learn_skill("cooking")
		self.assertTrue(len(self.robot.get_skills()) > 0)

	def test_learn_skill(self):
		self.assertEqual(self.robot.learn_skill("cooking"), "I'VE JUST LEARNT COOKING")

	def test_battery_on_learn_skill(self):
		self.robot.learn_skill("cooking")
		self.assertTrue(self.robot.battery_life(), 90)

	def tearDown(self):
		self.robot.skills.clear()


if __name__=="__main__":
	unittest.main()