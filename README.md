# Brocklyn

## Author 
Built by: [Victoria Beryl](https://github.com/Victoria045)

# Description
This is a neighborhood application that requires a user to sign in the application to start using and allows you to find a list of different businesses in the neighborhood and contact info for the health department. 

#### Prerequisites 
* python3.6
* pip
* Django

## User Story
* Sign in with the application to start using.
* Set up a profile about me and a general location and the neighborhood name.
* Find a list of different businesses in the neighborhood.
* Find Contact Information for the health department and Police authorities near the neighborhood.
* Create Posts that will be visible to everyone in the neighborhood.
* Change the neighborhood when I decide to move out.
* Only view details of a single neighborhood.

## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the application | On application load | Display of Login form |
| Create account by Sign Up | Enter email, username and password| Redirect to login|
| Login selected | Enter username and password you signed up with| Redirect to home page|
| Join neighbourhood button selected | Submit | Upload new hood in a form or join an existing one |
| Click on your hood | CLick | Redirected to page with your hood details and you can create posts or a business |
| Click the user profile icon | Select Profile | Redirected to profile page where you can view profile |
| Click the edit profile icon | Select Edit Profile | A form displays where you can edit profile |
| Click the logout button | Click | Logout and redirected to login page |

# Setup and Installation
#### Cloning the repository
* Open Terminal:
```bash
        $ git clone https://github.com/Victoria045/Broklyn.git
        $ cd Broklyn
        $ code . or atom . based on your text editor 
```
* Navigate into the folder, install and activate virtual environment
```bash
      $ python -m venv virtual

      $ source virtual/bin/acivate
```
* Install all dependencies in requirements.txt
```bash
      $ pip install -r requirements.txt
```
#### Setup the Database
* Setup the database username, password, host then make migrations  
```bash
      $ python manage.py makemigrations 
```
* Run migrations
```bash
      $ python manage.py migrate
```
### Running the Application
* To run the application, open the cloned repo in terminal and run the following commands:
```bash
      $ python3 manage.py runserver
```
### Testing the Application       
* To run unittests for the class application and check if it functions well:
```bash
      $ python3 manage.py test 
```
## Known Bugs
* No known bugs so far, incase a bug is spotted pull requests are allowed.


## Technologies Used
* markdown

* Django_Bootstrap4 - for bootstrap version 4

* Heroku - online deployment


## Support and contact details
Incase of any issues at hand, please email me at victoriaberyl45@gmail.com

### License
[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/Victoria045/Broklyn/blob/master/LICENSE) 