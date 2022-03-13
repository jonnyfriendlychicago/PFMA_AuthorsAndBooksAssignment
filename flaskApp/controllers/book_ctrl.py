from flaskApp import app
from flask import render_template,redirect,request,session,flash

from flaskApp.models.author_mod import Author_cls
from flaskApp.models.book_mod import Book_cls

@app.route('/books')
def bookHome():
    allBook = Book_cls.getAllBook()
    return render_template("books.html", display_allBook = allBook)

@app.route('/createBook', methods=["POST"])
def createBook():
    data = { # this creates cleared variables, containing cleansed incoming data from the form
        "clr_bookTitle": request.form["frm_bookTitle"]
        , "clr_pageCount": request.form["frm_pageCount"]
        }
    id = Book_cls.save(data) # creates variable... 'id' ... = that we'll use in next line (represents the ID of newly created record.... oh, and runs the "save" method from server.py)
    # return redirect('/DojoProfile/' + str(id)) 
    return redirect('/books') 

@app.route('/bookProfile/<int:id>')
def bookProfile(id):
    data = {
        "clr_id": id
    }
    bookInfo = Book_cls.getOneBook(data)
    allFavesByAuthor = Book_cls.get_allFavesByAuthor(data) 
    
    return render_template(
    "bookProfile.html" 
    , display_bookInfo = bookInfo
    , display_allFavesByAuthor = allFavesByAuthor
    )


"""DON'T TOUCH BELOW :-) below always needs to be at the bottom of the script, yes!"""
# below is stuff you oughta have, per TA Cameron Smith, from Coding Dojo: 

@app.route('/', defaults={'cookies': ''})
@app.route('/<path:cookies>')
def catch_allx(cookies):
    return 'Sorry! No response here. Try url again.'



# from flaskApp import app
# from flask import render_template,redirect,request,session,flash

# # from flaskApp.models.book_mod import Book_class
# from flaskApp.models.author_mod import Author_cls

""" HOME PAGE / INDEX """
# @app.route('/')
# def index():
#     allDojos = Dojo_cls.get_all()
#     return render_template("index.html", display_allDojos = allDojos)

# """ ADD NEW ninja """
# @app.route('/addNewNinja')
# def addNewNinja():
#     allDojos = Dojo_cls.get_all()
#     return render_template("addNewNinja.html", display_allDojos = allDojos)

# """ Route invoked on the Add New Ninja page """
# @app.route('/createNinja', methods=["POST"])
# def createNinja():
#     data = { # this creates cleared variables, containing cleansed incoming data from the form
#         "clr_firstName": request.form["frm_firstName"], 
#         "clr_lastName" : request.form["frm_lastName"],
#         "clr_age" : request.form["frm_age"] , 
#         "clr_dojo_id" : request.form["frm_dojo_id"]
#         }
#     # dojo_id = data.clr_dojo_id
#     id = Ninja_cls.saveNinja(data) # creates variable... 'id' ... = that we'll use in next line (represents the ID of newly created record.... oh, and runs the "save" method from server.py)
#     # return redirect('/DojoProfile/' + str(id)) 
#     # return redirect('/') 
#     return redirect(f"/dojoProfile/{data['clr_dojo_id']}")

# """ ADD NEW ninja -- dojolocked! """
# @app.route('/addNewNinjaDojoLocked')
# def addNewNinjaDojoLocked():
#     allDojos = Dojo_cls.get_all()
#     return render_template("addNewNinjaDojoLocked.html", display_allDojos = allDojos)

# """ Route invoked on the Add New Ninja page """
# @app.route('/createNinjaDojoLocked', methods=["POST"])
# def createNinjaDojoLocked():
#     data = { # this creates cleared variables, containing cleansed incoming data from the form
#         "clr_firstName": request.form["frm_firstName"], 
#         "clr_lastName" : request.form["frm_lastName"],
#         "clr_age" : request.form["frm_age"] , 
#         "clr_dojo_id" : request.form["frm_dojo_id"]
#         }
#     # dojo_id = data.clr_dojo_id
#     id = Ninja_cls.saveNinja(data) # creates variable... 'id' ... = that we'll use in next line (represents the ID of newly created record.... oh, and runs the "save" method from server.py)
#     # return redirect('/DojoProfile/' + str(id)) 
#     # return redirect('/') 
#     return redirect(f"/dojoProfile/{data['clr_dojo_id']}")





# @app.route('/dojoProfile')
# def index():
#     allDojos = Dojo_cls.get_all()
#     return render_template("dojoProfile.html", display_allDojos = allDojos)


# """route invoked by the redirect immediately above"""
# @app.route('/dojoProfile/<int:id>')
# def dojoProfile(id):
#     data = {
#         "clr_id": id
#     }
#     dojoProfile = Dojo_cls.getOne(data)
#     """ ABOVE absolutely essential; below will not work on it's own """
#     # DojoProfile = Dojo_cls.getOne(id)
#     allDojos = Dojo_cls.get_all()
#     return render_template("DojoProfile.html", display_dojoProfile = dojoProfile, display_allDojos = allDojos)

# """ route engaged by the 'edit' button on the DojoProfile.html page"""
# @app.route('/DojoProfile/<int:id>/edit')
# def editDojoProfile(id):
#     data = {
#         "clr_id": id
#     }
#     DojoProfile = Dojo_cls.getOne(data)
#     """ ABOVE absolutely essential; below will not work on it's own """
#     # DojoProfile = Dojo_cls.getOne(id)
#     return render_template("editDojoProfile.html", display_DojoProfile = DojoProfile)

# """ Route invoked by clicking the 'update friend' button on the edit Dojo profile page """
# @app.route('/DojoProfile/<int:id>/update', methods=["POST"])
# def updateDojoProfile(id):
#     data = { # this creates cleared variables, containing cleansed incoming data from the form
#         "clr_id": id, 
#         "clr_firstName": request.form["frm_firstName"],
#         "clr_lastName" : request.form["frm_lastName"],
#         "clr_email" : request.form["frm_email"]
#         }
#     Dojo_cls.update(data) # this line is just "run this update!" this  is getting a whole array of data, not just a single integer/ID
#     return redirect(f"/DojoProfile/{id}")

    
# @app.route('/DojoProfile/<int:id>/delete')
# def deleteDojoProfile(id): 
#     data = {
#         "clr_id": id
#     }
#     Dojo_cls.delete(data) # this line is just "run this update!" this  is getting a whole array of data, not just a single integer/ID
#     return redirect('/')    

