# Online Recipe / Cook book
###### This is an online recipe book.
It allows people to create and manage their recipes online.

### Name of the app:
Online Cookbook

###  Description:
The is on online recipe book that allows anyone who registers to be able to create, manage, and search for recipes. Once a user registers an account by providing an email and password, the user will then be able to login and create recipes online.
The user can manage the recipes by Creating, Editing, or Deleting any recipe anytime. There are no limits to the number of recipes allowed by users. And there are no access restrictions.

The recipe book is created in such a way that it is visually easy to navigate. From registration to login, editing and delete, there are visual icons to make the navigation process easy. When a user loggs in, there is a navigatiion menu to enable the user perform the tasks of managing their recipes.

One is not required to register to be able to search. The search and viewing of recipe is available to everyone, registered or non-registered members.
## Rules:

To be able to create or manage recipe one is required to registered. Registration is done by providing an email address, and a password. This way, every user is unique as no multiple registration by the same email address is allowed.


#### Public or Private Recipe:
When a user create a recipe, the user can opt for the recipe to be available online for others to see or disable that option. If the user chose for their recipe to be available for others online, it means other people will be able to view their recipe whenever their search criteria matches a publicly available recipe.

#### Database Used:
Mysql is the database of choice used. A recipe database was created, and tables to provide the storage for users and recipes details.


#### Cookies and session variables:
Users login are stored in session variables and given 5 minutes to time out if the user is inactive for that period of time. After being inactive for more than 5 minutes the user is automatically logged out. This provides some form of security to the user account.

#### Registering an account:
To register an account the user is required to provide First name, Last name, Email, and Password. Once these details are provided the registration is done. But before the registration process is complete the email is checked if it has been previously used to register. 
If the email has been previously used, the user is informed, and asked to login since the email has already been used to create an account. Alternatively, the user can use a different email. The app does not provide recover password.

#### Search For Recipe:
When a user visits the site, the index pages has icons that can be used to search for different recipes based on categories. A search by typing a search word is also possible on top of all pages visited.

#### Pages on visting the site for the first time:
HOME - This is the index page.  
LOG IN - This page allows a user that has already created an account to login to their account.
SIGN UP - This page provide the user the opportunity to register. Recipes can only be created by registered users.


#### Pages when a user logs in:
YOUR DETAILS - This is the user details page. With this page the user can edit their details.
CREATE RECIPE - This pages allows the user to create a new recipe.
YOUR RECIPES - This page allows the user to view their already created recipes.
EDIT RECIPES - This page allows user to edit their recipe.
RECIPE DETAILED VIEW. This page allows the user to view their recipes in detailed view.
DELETE RECIPE. This allows the user to delete their recipe.

### Views
Whenever someone searches for a recipe, all the recipes that met the search criteria are displayed in a list form from highest votes first and sorted again by views. Once a user clicks on one of the results, the recipe view is incremented by 1.

### Votes
When as a recipe is opened a user can vote for it. Each vote carries one point. And the number of votes are always displayed next to the recipe when opened in details view.



### Technologies used
The site was developed using html / html 5, CSS / CSS 3, Bootstrap, Javascript, Flask, Python3, MySQL, Cloud9, and git/github for version control. Also assessible on Heroku.

#### Limitations
Recipe pictures and images are not allowed presently to be uploaded. As images files are big, allowing upload of images might fill the permitted server space too quickly.


#### Support:
There is much room to develop this app into a full-fledge app by migrating or uploaded the app to a bigger server and allowing upload of recipe images. I'm open to any suggestions as to how to move it forward.


#### Source:
Google is always my first call for help. Images used on the app were all sourced from google free images. I did some modifications and editing to the images using Macromedia Fireworks, but all original images were sourced through google.