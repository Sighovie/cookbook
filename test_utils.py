import os
import pymysql
import unittest
from utils import *
# Connect to the database
username = os.getenv('C9_USER')
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='recipe')

class TestMyData(unittest.TestCase):

    def setUp(self):
        print('Test entered SetUp')
        sql_stm = """
            CREATE TABLE IF NOT EXISTS `authors2` (
              `author_id` smallint NOT NULL AUTO_INCREMENT,
              `email` varchar(150) DEFAULT NULL,
              `password` varchar(80) DEFAULT NULL,
              `firstname` varchar(100) DEFAULT NULL,
              `lastname` varchar(100) DEFAULT NULL,
              `gender` varchar(8) DEFAULT NULL,
              `date_of_birth` date DEFAULT NULL,
              `address` text,
              `city` varchar(150) DEFAULT NULL,
              `state` varchar(150) DEFAULT NULL,
              `country` varchar(150) DEFAULT NULL,
              `postcode` varchar(15) DEFAULT NULL,
              `reg_date`  date DEFAULT NULL,
              `contact_number` varchar(40) DEFAULT NULL,
              `public_status` char(1) DEFAULT '1',   
              `status` char(1) DEFAULT '1',
              PRIMARY KEY (`author_id`)
            ) ;"""
        rows = update_database(sql_stm)
        sql_stm = """
            INSERT INTO authors2 (email,password,firstname,lastname,gender,date_of_birth,address,city,state,country,postcode,reg_date,contact_number,public_status,status)VALUES('testemail@mail.com','passpass','John','Peru','Male','1989-06-15','Address','City','State','Country','245845','2018-07-15','0807543565','1','1');"""
        rows = update_database(sql_stm)

    def test_fetch_one_row(self):
        query = "SELECT * FROM authors2 WHERE firstname='John';"
        data = fetch_one_row(query)
        self.assertEqual(data['firstname'], 'John')
        self.assertEqual(data['firstname'] + ' ' + data['lastname'], 'John Peru')
        #self.assertEqual(data['firstname'] + ' ' + data['lastname'], 'John Peru2')#this should fail
        
    def test_update_database(self):
        sql_stm = "UPDATE authors2 SET firstname='Michael', lastname='Bush' WHERE firstname='John' AND lastname='Peru';"
        rows = update_database(sql_stm)
        
        query = "SELECT * FROM authors2 WHERE firstname='Michael' AND lastname='Bush';"
        data = fetch_one_row(query)        
        self.assertEqual(data['firstname'], 'Michael')
        self.assertEqual(data['firstname'] + ' ' + data['lastname'], 'Michael Bush')
 
    """This test below is tested against the production table authors. So if the email provided is not available in that table, the test will fail"""
    def test_does_user_exist(self):
        #Note that this test might fail when the email provided here is not available in the table authors. Other tests above are done on the created table authors2. 
        self.assertEqual(does_user_exist('debbydrury@mail.com'), True)

        
    def tearDown(self):
        print('Test entered tearDown')
        sql_stm = "DROP TABLE authors2;"
        rows = update_database(sql_stm)


if __name__ == '__main__':
    unittest.main()        