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
sql_stm = "SELECT * FROM recipe ;"
recipe_data = fetch_all_rows(sql_stm) 
print(recipe_data)
        
#print(fetch_one_row(sql_stm))
#sql_stm = "SELECT * FROM categories WHERE status='1';"
#mydata = fetch_all_rows(sql_stm)
#for value in mydata:
#    print(value['category_name'],"\n")
#print(fetch_all_rows(sql_stm))

#sql_stm = "SELECT * FROM categories WHERE status='1';"
#categories = fetch_all_rows(sql_stm)
#print(categories)
