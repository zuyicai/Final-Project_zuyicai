import sqlite3
import unittest


class Final_DBTests(unittest.TestCase):

	def setUp(self):
		self.conn = sqlite3.connect("parks_collection.db") # Connecting to database that should exist in autograder
		self.cur = self.conn.cursor()

	def test_for_topics_table(self):
		self.cur.execute("select value where name = 'Arts'")
		data = self.cur.fetchone()
		self.assertEqual(data,('Arts', 9), "Testing data that results from selecting topic Arts")

    # def test_for_activities_table(self):
    #     self.cur.execute("select name where value = 71")
	# 	data = self.cur.fetchone()
	# 	self.assertEqual(data,('Ice Skating', 71), "Testing data that results from selecting activity with value=71")

	def test_for_states_table(self):
		res = self.cur.execute("select * from State")
		data = res.fetchall()
		self.assertTrue(data, 'Testing that you get a result from making a query to the States table')

	def test_foreign_key_states(self):
		res = self.cur.execute("select * from State INNER JOIN National_Park ON National_Park.id = states.park_id")
		data = res.fetchall()
		self.assertTrue(data, "Testing that result of selecting based on relationship between States and National_Park does work")
		self.assertTrue(len(data) in [23, 24], "Testing that there is in fact the amount of data entered that there should have been -- based on this query of everything in both tables.{}".format(len(data)))


	def tearDown(self):
		self.conn.commit()
		self.conn.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
