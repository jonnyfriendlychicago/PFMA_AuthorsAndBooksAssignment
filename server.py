# the next two lines always need to be atop this server.py file 
# from collections import UserList # this is a line that's relevant for other stuff; keep out for this assignment, as it's needlessly confusing me

# below commented out, moved to init.py
# from flask import Flask, render_template, request, redirect, session # Import Flask to allow us to create our app

#below added, MVC: 
from flaskApp import app
from flaskApp.controllers import author_ctrl
from flaskApp.controllers import book_ctrl

# below is flask boiler plate; exclude it and stuff won't work    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

# below commented out, moved to init.py
# app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# app.secret_key = 'dsadfdafdfgaf' # this key can always be some junk, it doesn't matter, as long as this line is there. 

# ...server.py

