import os
import pymysql


# Connect to the database
username = os.getenv('C9_USER')
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='recipe')
email = "debbydrury@mail.com"
  
        
#http://zetcode.com/db/mysqlpython/
"""Fetch data"""
sql_stm = "SELECT * FROM authors WHERE email='"+ email +"2';"
def fetch_one_row(sql_stm):
    data = []
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            rows = cursor.execute(sql_stm)
            data = cursor.fetchone()
            connection.commit()
            if rows > 0:
               return data
            else:
               return data
    finally:
        connection.close()
 
        
def does_user_exist(email):
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql_stm = "SELECT * FROM authors WHERE email='"+ email +"';"
            rows = cursor.execute(sql_stm)
            data = cursor.fetchall()
            print(data[0]["email"])
            connection.commit()
            if rows > 0:
               return True
            else:
               return False
    finally:
        connection.close()

def fetch_all_rows(sql_stm):
    data = []
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            rows = cursor.execute(sql_stm)
            data = cursor.fetchall()
            connection.commit()
            if rows > 0:
               return data
            else:
               return data
    except:
        ""    


"""This function helps fetch all categories"""
def fetch_all_categories(sql_stm):
    data = []
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            rows = cursor.execute(sql_stm)
            data = cursor.fetchall()
            connection.commit()
            if rows > 0:
                concat_str = ""
                for value in data:
                    concat_str += "<option value='"+ str(value["category_id"]) +"'>"+ value["category_name"] +"</option>\n"          
                return concat_str
            else:
               return data
    except:
        "" 
        
"""
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
) ;
INSERT INTO authors2 (author_id,email,password,firstname,lastname,gender,date_of_birth,address,city,state,country,postcode,reg_date,contact_number,public_status,status) VALUES
(1, 'example@example.com', 'samplepassword', 'John', 'Kerry', 'Male', '1997-06-20', '', '', '', '', '', '2018-06-24', '08065487844', '1', '1');


CREATE TABLE IF NOT EXISTS `categories2` (
  `category_id` smallint NOT NULL AUTO_INCREMENT,
  `category_name` varchar(60) DEFAULT NULL,
  `status` char(1) DEFAULT '1',
  PRIMARY KEY (`category_id`)
) ;
INSERT INTO categories2 (category_name,status) VALUES
('Breakfast', '1'),
('Lunch', '1'),
('Beverages', '1'),
('Appetizers', '1'),
('Soups', '1'),
('Salads', '1'),
('Main dishes: Beef', '1'),
('Main dishes: Poultry', '1'),
('Main dishes: Pork', '1'),
('Main dishes: Seafood', '1'),
('Main dishes: Vegetarian', '1'),
('Side dishes: Vegetables', '1'),
('Side dishes: Other', '1'),
('Desserts', '1'),
('Canning / Freezing', '1'),
('Breads', '1'),
('Holidays', '1'),
('Entertaining', '1');

CREATE TABLE IF NOT EXISTS `recipe2` (
  `recipe_id` smallint NOT NULL AUTO_INCREMENT,
  `author_id`  smallint NOT NULL,
  `category_id`  smallint NOT NULL,  
  `recipe_name` varchar(100) DEFAULT NULL,
  `ingredients` text,
  `preparation_description` text,
  `known_allergies` text,
  `nutrition` text,     
  `preparation_time`  smallint NOT NULL,  
  `cooking_time`  smallint NOT NULL,  
  `cuisine` varchar(100) DEFAULT NULL,  
  `votes`  smallint NOT NULL DEFAULT 0,
  `likes`  smallint NOT NULL DEFAULT 0,  
  `dislikes`  smallint NOT NULL DEFAULT 0,
  `views`  smallint NOT NULL DEFAULT 0,  
  `post_date` date DEFAULT NULL,
  `image_link` varchar(100) DEFAULT NULL, 
  `public_status` char(1) DEFAULT '1',   
  `status` char(1) DEFAULT '1',
  PRIMARY KEY (`recipe_id`)
) ;

INSERT INTO recipe (author_id,category_id,recipe_name,ingredients,preparation_description,known_allergies,nutrition,preparation_time,cooking_time,cuisine,votes,likes,dislikes,views,post_date,image_link,public_status,status) VALUES 
(1, 1, 'Baking Bread', 'Flour, sugar, yeast,salt, butter', 'Put some flour into a bowl and add sugar, yeast, salt and butter and mix', 'No allergies', 'Highly nutritious', 10, 20, 'Chinese', 10, 0, 0, 10, '2018-06-24','', '1', '1');
 

"""        
sql_stm = "SELECT * FROM recipe ;"
recipe_data = fetch_all_rows(sql_stm) 
print(recipe_data[0]["category_id"])
        
#print(fetch_one_row(sql_stm))
#sql_stm = "SELECT * FROM categories WHERE status='1';"
#mydata = fetch_all_rows(sql_stm)
#for value in mydata:
#    print(value['category_name'],"\n")
#print(fetch_all_rows(sql_stm))

#sql_stm = "SELECT * FROM categories WHERE status='1';"
#categories = fetch_all_rows(sql_stm)
#print(categories)
