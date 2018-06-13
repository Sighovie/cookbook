import os
import datetime
import pymysql
from flask import Flask
from flask import Flask, render_template, request, json, url_for,redirect, session, escape
from datetime import timedelta
import pymysql
#from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secret_key511"
# Connect to the database
username = os.getenv('C9_USER')
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='recipe')
                             

"""To ensure that sessions used timedout in 30 minutes of inactivities"""
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)


# Connect to the database
#connection = pymysql.connect(host='localhost', user="si_user",password="si_allow_pass_through", db='recipe')
"""Function to validate login for all pages available when a user is logged in"""
def validate_login():
    try:
        if session["email"] and session["password"]:   
            return 1
        else:
            return 0 
    except:
        return 0   
        
""" Update database Function"""
def update_database(sql_stm):
    rows = 0
    try:
        with connection.cursor() as cursor:
            rows = cursor.execute(sql_stm)
            connection.commit()
    except:
        ""
    return rows
    
    
"""The function is used to return one row only"""
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
    except:
        ""

"""The function is used to return all rows"""
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


"""Check if the email address is registered already"""    
def does_user_exist(email):
    try:
        with connection.cursor() as cursor:
            sql_stm = "SELECT * FROM authors WHERE email='"+ email +"';"
            rows = cursor.execute(sql_stm)
            connection.commit()
            if rows > 0:
               return True
            else:
               return False
    except:
        ""
        
@app.route("/")
def main():
    return render_template('index.html') 
 
"""Dashboard when successfully logged in"""          
@app.route("/dashboard")
def dashboard():
    enable_entry = validate_login()
    if enable_entry == 1:
        return render_template('dash_index.html') 
    else:
        notice = "Your session has expired. Please Login again!"
        notice_type = '0'
        return render_template('login.html',notice=notice, notice_type=notice_type)              

@app.route("/Login")
def login():
    return render_template('login.html')  
    
@app.route("/LogOut")
def LogOut():
    notice = """You have successfully logged out!"""
    notice_type = '1'
    session.pop("email", None)
    session.pop("password", None)  
    session.pop("firstname", None)
    session.pop("lastname", None)
    session.pop("public_status", None)    
    session.pop("author_id", None)
    session.pop("public_status", None)
    return render_template('login.html',notice=notice,notice_type=notice_type)    
    
@app.route('/OpenSignUp')
def OpenSignUp():
    return render_template('register.html')
    
@app.route('/edit_details')
def edit_details():
    enable_entry = validate_login()
    if enable_entry == 1:
        sql_stm = "SELECT * FROM authors WHERE author_id ='"+ str(session["author_id"]) + "' LIMIT 1;"
        edit_data = fetch_one_row(sql_stm)
        return render_template('edit_details.html',data=edit_data) 
    else:
        notice = "Your session has expired. Please Login again!"
        notice_type = '0'
        return render_template('login.html',notice=notice, notice_type=notice_type)              

"""This is to create a new recipe"""
@app.route('/create_recipe')
def create_recipe():
    enable_entry = validate_login()
    if enable_entry == 1:
        sql_stm = "SELECT * FROM categories WHERE status='1';"
        categories = fetch_all_rows(sql_stm)
        return render_template('create_recipe.html',cat=categories) 
    else:
        notice = "Your session has expired. Please Login again!"
        notice_type = '0'
        return render_template('login.html',notice=notice, notice_type=notice_type)              

"""This is to edit  recipe"""
@app.route('/edit_recipe', methods=['GET'])
def edit_recipe():
    enable_entry = validate_login()
    if enable_entry == 1:
        sql_stm = "SELECT * FROM categories WHERE status='1';"
        categories = fetch_all_rows(sql_stm)
        
        sql_stm = "SELECT * FROM recipe WHERE recipe_id='" + str(request.args.get('id')) + "' AND author_id ='" + str(session["author_id"]) + "';"
        recipe_data = fetch_all_rows(sql_stm)        
        
        return render_template('edit_recipe.html',cat=categories, data=recipe_data) 
    else:
        notice = "Your session has expired. Please Login again!"
        notice_type = '0'
        return render_template('login.html',notice=notice, notice_type=notice_type)     
        
        
"""This is to open recipe_detailed_view page"""
@app.route('/recipe_detailed_view')
def recipe_detailed_view():
    enable_entry = validate_login()
    if enable_entry == 1:

        sql_stm = "SELECT * FROM categories WHERE status='1';"
        categories = fetch_all_rows(sql_stm)
                
        sql_stm = "SELECT * FROM recipe WHERE recipe_id='" + str(request.args.get('id')) + "';"
        recipe_data = fetch_all_rows(sql_stm)        
                
        return render_template('recipe_detailed_view.html',cat=categories, data=recipe_data)    

    else:
        notice = "Your session has expired. Please Login again!"
        notice_type = '0'
        return render_template('login.html',notice=notice, notice_type=notice_type) 
        
"""This is to open delete recipee"""
@app.route('/delete_recipe')
def delete_recipe():
    enable_entry = validate_login()
    if enable_entry == 1:
        #now is time to delete the recipe if the conditions are met
        sql_stm = "DELETE FROM recipe WHERE recipe_id='"+ str(request.args.get('id')) +"' AND author_id='"+ str(session["author_id"]) +"' LIMIT 1"
        try:
            with connection.cursor() as cursor:
                rows = cursor.execute(sql_stm)
                connection.commit()
                if rows > 0:
                   notice="Your recipe has been successfully deleted!" 
                   notice_type="1"
                else:
                   notice="The recipe could not be deleted!" 
                   notice_type="0"
        except:
            ""        
        
        sql_stm = "SELECT * FROM recipe WHERE author_id='"+ str(session["author_id"]) +"' AND status='1' Order By recipe_id DESC;"
        recipes = fetch_all_rows(sql_stm)
        return render_template('view_your_recipes.html',recipes=recipes,notice=notice, notice_type=notice_type)  

    else:
        notice = "Your session has expired. Please Login again!"
        notice_type = '0'
        return render_template('login.html',notice=notice, notice_type=notice_type)   
        
        

@app.route('/view_your_recipes')
def view_your_recipes():
    enable_entry = validate_login()
    if enable_entry == 1:
        sql_stm = "SELECT * FROM recipe WHERE author_id='"+ str(session["author_id"]) +"' AND status='1' Order By recipe_id DESC;"
        recipes = fetch_all_rows(sql_stm)
        return render_template('view_your_recipes.html',recipes=recipes) 
    else:
        notice = "Your session has expired. Please Login again!"
        notice_type = '0'
        return render_template('login.html',notice=notice, notice_type=notice_type)        
        
""" Search result""" 
@app.route('/search', methods=['GET', 'POST'])
def search():
    enable_entry = validate_login()
    if enable_entry == 1:
        search_words = ""
        search = ""
        try:
            if request.form['search']:
                search_words = request.form['search']
                search = search_words
            elif request.args.get('s'):
                search_words = request.args.get('s')   
                search = search_words
        except:
            ""
        sql_stm = "SELECT * FROM recipe WHERE recipe_name LIKE '%"+ search_words +"%' OR ingredients LIKE '%"+ search_words +"%' OR preparation_description LIKE '%"+ search_words +"%' OR known_allergies LIKE '%"+ search_words +"%' OR nutrition LIKE '%"+ search_words +"%' OR cuisine LIKE '%"+ search_words +"%' AND public_status='1' AND status='1' ORDER BY votes DESC, views DESC;"
        recipes = fetch_all_rows(sql_stm)
        return render_template('search_results.html',recipes=recipes,search=search) 
    else:
        notice = "Your session has expired. Please Login again!"
        notice_type = '0'
        return render_template('login.html',notice=notice, notice_type=notice_type)          



        
""" This is for Search detailed result searchDetail"""       
@app.route('/searchDetail',methods=['GET'])
def searchDetail():
    enable_entry = validate_login()
    if enable_entry == 1:
        #First update view with + 1
        
        sql_stm = "SELECT recipe_id,views FROM recipe WHERE recipe_id='"+ str(request.args.get('id')) +"';"
        data = fetch_one_row(sql_stm)        
        new_views = 1 + int(data["views"])
        sql_stm = "UPDATE recipe SET views ='" + str(new_views) + "' WHERE recipe_id = '" + str(request.args.get('id')) + "' LIMIT 1;"
        rows = update_database(sql_stm)

        sql_stm = "SELECT * FROM categories WHERE status='1';"
        categories = fetch_all_rows(sql_stm)
        
        sql_stm = "SELECT * FROM recipe WHERE recipe_id='" + str(request.args.get('id')) + "' AND public_status ='1';"
        recipe_data = fetch_all_rows(sql_stm)        
        
        search = request.args.get('s')
        return render_template('search_result_detailed.html',cat=categories, recipes=recipe_data,search=search) 
    else:
        notice = "Your session has expired. Please Login again!"
        notice_type = '0'
        return render_template('login.html',notice=notice, notice_type=notice_type)    
        

        
""" Outside Search result""" 
@app.route('/search_cat', methods=['GET', 'POST'])
def search_cat():
     search_words = ""
     search = ""
     try:
         if request.form['search']:
             search_words = request.form['search']
             search = search_words

             sql_stm = "SELECT * FROM recipe WHERE recipe_name LIKE '%"+ search_words +"%' OR ingredients LIKE '%"+ search_words +"%' OR preparation_description LIKE '%"+ search_words +"%' OR known_allergies LIKE '%"+ search_words +"%' OR nutrition LIKE '%"+ search_words +"%' OR cuisine LIKE '%"+ search_words +"%' AND public_status='1' AND status='1' ORDER BY votes DESC, views DESC;"
             recipes = fetch_all_rows(sql_stm) 

             return render_template('outside_search_results.html',recipes=recipes,search=search)              
     except:
         ""

""" Outside Search result query """ 
@app.route('/search_cat_get', methods=['GET'])
def search_cat_get():
     search_words = ""
     search = ""
     try:
         if request.args.get("s"):
             search_words = request.args.get("s")   
             search = search_words
             
             sql_stm = "SELECT * FROM recipe WHERE recipe_name LIKE '%"+ search_words +"%' OR ingredients LIKE '%"+ search_words +"%' OR preparation_description LIKE '%"+ search_words +"%' OR known_allergies LIKE '%"+ search_words +"%' OR nutrition LIKE '%"+ search_words +"%' OR cuisine LIKE '%"+ search_words +"%' AND public_status='1' AND status='1' ORDER BY votes DESC, views DESC;"
             recipes = fetch_all_rows(sql_stm) 
             return render_template('outside_search_results.html',recipes=recipes,search=search) 
         elif request.args.get("c"):    
             sql_stm = "SELECT * FROM categories WHERE category_name LIKE '%"+ request.args.get('c') + "%' AND status='1';"
             
             data = fetch_all_rows(sql_stm)             
             data[0]["category_id"] 
             sql_stm = "SELECT * FROM recipe WHERE category_id = '%"+  '2' +"%' AND public_status='1' AND status='1' ORDER BY votes DESC, views DESC;"
             recipes = fetch_all_rows(sql_stm)
             return render_template('outside_search_results.html',recipes=recipes,search=search)  
     except:
           ""


""" Outside index categories Search result query """ 
@app.route('/search_index_get', methods=['GET'])
def search_index_get():
     search_words = ""
     search = ""
     try:
         if request.args.get("c"):    
             sql_stm = "SELECT * FROM categories WHERE category_name LIKE '%"+ request.args.get('c') + "%' AND status='1';"
             data = fetch_all_rows(sql_stm)             
             sql_stm = "SELECT * FROM recipe WHERE category_id = '"+  str(data[0]["category_id"])  +"' AND public_status='1' AND status='1' ORDER BY votes DESC, views DESC;"
             recipes = fetch_all_rows(sql_stm)
             search = request.args.get('c')
             return render_template('outside_search_results.html',recipes=recipes,search=search)  
     except:
           ""           
             
""" This is for Search detailed result searchDetail"""       
@app.route('/outsideSearchDetail',methods=['GET'])
def outsideSearchDetail():
        sql_stm = "SELECT recipe_id,views FROM recipe WHERE recipe_id='"+ str(request.args.get('id')) +"';"
        data = fetch_one_row(sql_stm)        
        new_views = 1 + int(data["views"])
        sql_stm = "UPDATE recipe SET views ='" + str(new_views) + "' WHERE recipe_id = '" + str(request.args.get('id')) + "' LIMIT 1;"
        rows = update_database(sql_stm)

        sql_stm = "SELECT * FROM categories WHERE status='1';"
        categories = fetch_all_rows(sql_stm)
        
        sql_stm = "SELECT * FROM recipe WHERE recipe_id='" + str(request.args.get('id')) + "' AND public_status ='1';"
        recipe_data = fetch_all_rows(sql_stm)        
        
        search = request.args.get('s')
        return render_template('outside_search_result_detailed.html',cat=categories, recipes=recipe_data,search=search) 

        
""" VoteNow """
""" This is for for votes """       
@app.route('/VoteNow',methods=['GET'])
def VoteNow():
    enable_entry = validate_login()
    if enable_entry == 1:
        #First update view with + 1
        
        sql_stm = "SELECT recipe_id,votes FROM recipe WHERE recipe_id='"+ str(request.args.get('id')) +"';"
        data = fetch_one_row(sql_stm)        
        new_votes = 1 + int(data["votes"])
        sql_stm = "UPDATE recipe SET votes ='" + str(new_votes) + "' WHERE recipe_id = '" + str(request.args.get('id')) + "' LIMIT 1;"
        rows = update_database(sql_stm)

        sql_stm = "SELECT * FROM categories WHERE status='1';"
        categories = fetch_all_rows(sql_stm)
        
        sql_stm = "SELECT * FROM recipe WHERE recipe_id='" + str(request.args.get('id')) + "' AND public_status ='1';"
        recipe_data = fetch_all_rows(sql_stm)        
        search = request.args.get('s')
        return render_template('search_result_detailed.html',cat=categories, recipes=recipe_data,search=search) 
    else:
        notice = "Your session has expired. Please Login again!"
        notice_type = '0'
        return render_template('login.html',notice=notice, notice_type=notice_type)    

""" Out VoteNow """
""" This is for for votes """       
@app.route('/OutVoteNow',methods=['GET'])
def OutVoteNow():

    #First update view with + 1
        
    sql_stm = "SELECT recipe_id,votes FROM recipe WHERE recipe_id='"+ str(request.args.get('id')) +"';"
    data = fetch_one_row(sql_stm)        
    new_votes = 1 + int(data["votes"])
    sql_stm = "UPDATE recipe SET votes ='" + str(new_votes) + "' WHERE recipe_id = '" + str(request.args.get('id')) + "' LIMIT 1;"
    rows = update_database(sql_stm)

    sql_stm = "SELECT * FROM categories WHERE status='1';"
    categories = fetch_all_rows(sql_stm)
        
    sql_stm = "SELECT * FROM recipe WHERE recipe_id='" + str(request.args.get('id')) + "' AND public_status ='1';"
    recipe_data = fetch_all_rows(sql_stm)        
    search = request.args.get('s')
    return render_template('outside_search_result_detailed.html',cat=categories, recipes=recipe_data,search=search) 

        
""" This is to enter recipe details"""
@app.route('/createNewRecipe',methods=['POST'])
def createNewRecipe():
    notice = ""
    notice_type = ""    
    sql_stm = "SELECT * FROM categories WHERE status='1';"
    categories = fetch_all_rows(sql_stm)    
    enable_entry = validate_login()
    if enable_entry == 1:
        now = datetime.datetime.now()
        author_id = session["author_id"]
        category_id = request.form['category_id']
        recipe_name = request.form['recipe_name']
        ingredients = request.form['ingredients']
        preparation_description = request.form['preparation_description']
        known_allergies = request.form['known_allergies']
        nutrition = request.form['nutrition']
        preparation_time = request.form['preparation_time']
        cooking_time = request.form['cooking_time']
        cuisine = request.form['cuisine']
        votes = 0
        likes = 0
        dislikes = 0 
        views = 0
        post_date = now.strftime("%Y-%m-%d")
        image_link = ""
        public_status  = request.form['public_status']
        

        if recipe_name and ingredients and preparation_description:

            try:
                with connection.cursor() as cursor:
                    
                    sql_stm = """INSERT INTO recipe (author_id,category_id,recipe_name,ingredients,preparation_description,known_allergies,nutrition,preparation_time,cooking_time,cuisine,votes,likes,dislikes,views,post_date,image_link,public_status,status) 
                    VALUES ('"""+ str(author_id) +"""','"""+ str(category_id) +"""','"""+ recipe_name +"""','"""+ ingredients +"""','"""+ preparation_description +"""','"""+ known_allergies +"""','"""+ nutrition + """','"""+ str(preparation_time) +"""','"""+ str(cooking_time) +"""','"""+ cuisine +"""','"""+ str(votes) +"""','"""+ str(likes) +"""','"""+ str(dislikes) +"""','""" + str(views) +"""','"""+ str(post_date) +"""','"""+ image_link +"""','"""+ str(public_status) +"""','1');"""
                    rows = cursor.execute(sql_stm)
                    connection.commit()
                    if rows > 0:
                        notice = """New Recipe Successfully Created."""
                        notice_type = '1'
                    else:
                        notice = """Recipe could not be created."""
                        notice_type = '0'                       
            except:
                ""
                  
                   
            return render_template('create_recipe.html',cat=categories, notice=notice, notice_type=notice_type)
        else:
            notice = "All details required. Registration has not been successful. Please try again!"
            notice_type = '0'
            return render_template('create_recipe.html',cat=categories, notice=notice, notice_type=notice_type)

         
    else:
        notice = "Your session has expired. Please Login again!"
        notice_type = '0'
        return render_template('login.html',notice=notice, notice_type=notice_type)          
    
            
    
@app.route('/signUp',methods=['POST'])
def signUp():
    notice = ""
    notice_type = ""
    email = request.form['email']
    password = request.form['password'] #generate_password_hash() 
    firstname = request.form['firstname']
    lastname = request.form['lastname']

    now = datetime.datetime.now()

    if email and password and firstname and lastname:
        if not does_user_exist(email):
            try:
                with connection.cursor() as cursor:
                    sql_stm = "INSERT INTO authors (email,password,firstname,lastname,gender,date_of_birth,address,city,state,country,postcode,reg_date,contact_number,public_status,status) VALUES('"+ email +"','"+ password +"','"+ firstname +"','"+ lastname +"','','','','','','','','"+ now.strftime("%Y-%m-%d %H:%M") +"','','0','1');"
                    rows = cursor.execute(sql_stm)
                    connection.commit()
                    notice = "Registration successful. Please Login!"
                    notice_type = '1'
                    
            except:
                ""

            return render_template('login.html',notice=notice, notice_type=notice_type)              
        else:
            notice = "This email has previously been used to register an account. Please use a different email, or Login!"
            notice_type = '0'
            return render_template('register.html',notice=notice, notice_type=notice_type)                
    else:
        notice = "All details required. Registration has not been successful. Please try again!"
        notice_type = '0'
        return render_template('register.html',notice=notice, notice_type=notice_type)            

@app.route('/updateUser',methods=['POST'])
def updateUser():
    enable_entry = validate_login()
    if enable_entry == 1:
        email = request.form['email']
        password = request.form['password'] #generate_password_hash() 
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        country = request.form['country']
        contact_number = request.form['contact_number']
        public_status = request.form['public_status']
        try:
            with connection.cursor() as cursor:
                sql_stm = "UPDATE authors SET email ='" + email + "',password ='" + password + "',firstname ='" + firstname + "',lastname ='" + lastname+ "',address ='" + address + "',city ='" + city + "',state ='" + state + "',country ='" + country + "',contact_number ='" + contact_number + "',public_status ='" + public_status +"' WHERE author_id = '" + str(session["author_id"]) + "' LIMIT 1;"
                rows = cursor.execute(sql_stm)
                connection.commit()
                
                sql_stm = "SELECT * FROM authors WHERE author_id ='"+ str(session["author_id"]) + "' LIMIT 1;"
                edit_data = fetch_one_row(sql_stm)
                
        
                notice = """Details updated successful!"""
                notice_type = '1'
        except:
            ""
        return render_template('edit_details.html',data=edit_data,notice=notice, notice_type=notice_type) 
    else:
        notice = "Your session has expired. Please Login again!"
        notice_type = '0'
        return render_template('login.html',notice=notice, notice_type=notice_type)              


"""Used to update recipe"""
@app.route('/UpdateRecipe',methods=['POST'])
def UpdateRecipe():
    enable_entry = validate_login()
    if enable_entry == 1:
        recipe_id = str(request.form['recipe_id'])
        author_id = str(session["author_id"])
        category_id = str(request.form['category_id'])
        recipe_name = request.form['recipe_name']
        ingredients = request.form['ingredients']
        preparation_description = request.form['preparation_description']
        known_allergies = request.form['known_allergies']
        nutrition = request.form['nutrition']
        preparation_time = str(request.form['preparation_time'])
        cooking_time = str(request.form['cooking_time'])
        cuisine = request.form['cuisine']
        public_status = str(request.form['public_status'])
        try:
            with connection.cursor() as cursor:
                sql_stm = "UPDATE recipe SET category_id ='" + category_id + "',recipe_name ='" + recipe_name + "',ingredients ='" + ingredients + "',preparation_description ='" + preparation_description+ "',known_allergies ='" + known_allergies + "',nutrition ='" + nutrition + "',preparation_time ='" + preparation_time + "',cooking_time ='" + cooking_time + "',cuisine ='" + cuisine + "',public_status ='" + public_status +"' WHERE recipe_id = '" + str(recipe_id) + "' LIMIT 1;"
                rows = cursor.execute(sql_stm)
                connection.commit()

                notice = """Recipe updated successfully!"""
                notice_type = '1'
                
                sql_stm = "SELECT * FROM categories WHERE status='1';"
                categories = fetch_all_rows(sql_stm)
                
                sql_stm = "SELECT * FROM recipe WHERE recipe_id='" + recipe_id + "';"
                recipe_data = fetch_all_rows(sql_stm)        
                
                return render_template('edit_recipe.html',cat=categories, data=recipe_data,notice=notice, notice_type=notice_type)                 
        except:
            ""
            return render_template('edit_recipe.html',cat=categories, data=recipe_data,notice="Could not be updated!", notice_type="0") 
    else:
        notice = "Your session has expired. Please Login again!"
        notice_type = '0'
        return render_template('login.html',notice=notice, notice_type=notice_type)  
        

@app.route('/LoginUser',methods=['POST'])
def LoginUser():
    email = request.form['email']
    password = request.form['password'] #generate_password_hash() 

    if email and password:
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
               sql_stm = "SELECT * FROM authors WHERE email = '"+ email +"' AND password = '"+  password+"';"
               rows = cursor.execute(sql_stm)
               data = cursor.fetchone()
               connection.commit()
               if rows > 0:
                   session["email"] = email
                   session["password"] = password
                   session["firstname"] = data["firstname"]
                   session["lastname"] = data["lastname"] 
                   session["author_id"] = data["author_id"] 
                   session["public_status"] = data["public_status"] 

                   return redirect(url_for('dashboard'))
               else:
                   notice = "Login failed. Please try again"
                   notice_type = '0'
                   return render_template('login.html',notice=notice, notice_type=notice_type)                       
        except:
                ""
    else:
        notice = "Invalid details. Please enter your Email and Password correctly to login!"
        notice_type = '0'
        return render_template('login.html',notice=notice, notice_type=notice_type)              

        
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        
        
