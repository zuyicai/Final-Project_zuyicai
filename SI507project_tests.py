import sqlite3
import unittest
import csv
from SI507project_tools import *



class CSV_Tests(unittest.TestCase):# Testing the required data is successfully stored in my .csv file
	def test_for_scraping_states_csv(self):
		self.states_info_file = open('states_info.csv','r')
		self.contents = self.states_info_file.readlines()
		self.states_info_file.close()
		self.assertTrue('GU,Guam\r\n' in self.contents, "Testing that the GU line exists correctly in the scraped states information file")
		self.assertTrue('MI,Michigan\r\n' in self.contents, "Testing that the MI line is correct in resulting file, including its value")

	def test_for_scraping_topics_csv(self):
		self.topics_info_file = open('topics_info.csv','r')
		self.contents1 = self.topics_info_file.readlines()
		self.topics_info_file.close()
		self.assertTrue('24,Dams\r\n' in self.contents1, "Testing that we already successfully get the Dams topic and its value in the scraped topics info file")
		self.assertTrue('143,Fire\r\n' in self.contents1, "Testing that we already successfully get the Fire topic and its value in the scraped topics info file")

	def test_for_scraping_activities_csv(self):
		self.activities_info_file = open('activities_info.csv','r')
		self.contents2 = self.activities_info_file.readlines()
		self.activities_info_file.close()
		self.assertTrue('84,Tubing\r\n' in self.contents2, "Testing that we already successfully get the Tubing activity and its value in the scraped topics info file")
		self.assertTrue('61,Hiking\r\n' in self.contents2, "Testing that we already successfully get the Hiking activity and its value in the scraped topics info file")




class Database_Tests(unittest.TestCase):
	def setUp(self):
		self.conn = sqlite3.connect("parks_collection.db") # Connecting to database that should exist in autograder
		self.cur = self.conn.cursor()

	# Testing the topic named Arts exists. This route need to search parks based on their names.
	def test_for_topics_table(self):
		self.cur.execute("select name, value from Topics where name = 'Arts'")
		data = self.cur.fetchone()
		self.assertEqual(data,('Arts',9), "Testing data that results from selecting topic Arts")

	#Testing database table States
	def test_for_states_table(self):
		res = self.cur.execute("select * from States")
		data = res.fetchall()
		self.assertTrue(data, 'Testing that you get a result from making a query to the States table')

    #Testing inserting data works in the database
	def test_activities_insert_works(self):
		activity = (42,'Test',1000)
		self.cur.execute("insert into Activities(id, name, value) values (?, ?, ?)", activity)
		self.conn.commit()

		self.cur.execute("select id, name, value from Activities where id = 42")
		data = self.cur.fetchone()
		self.assertEqual(data, activity, "Testing a select activity where id = 42")
		self.cur.execute("DELETE FROM Activities where id = 42")

    # Testing "one to many" relatioship works in the database between National_Park and types
	def test_foreign_key_types(self):
		res = self.cur.execute("select * from National_Park INNER JOIN Types ON Types.id = National_Park.type_id")
		data = res.fetchall()
		self.assertTrue(data, "Testing that result of selecting based on relationship between Topics and National_Park does work")
		self.assertTrue(len(data) in [479, 480], "Testing that there is in fact the amount of data entered that there should have been -- based on this query of everything in both tables.{}".format(len(data)))

	def tearDown(self):
		self.conn.commit()
		self.conn.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
