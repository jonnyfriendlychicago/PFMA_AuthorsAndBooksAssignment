# from typing_extensions import dataclass_transform
from flaskApp import app
from flask import render_template,redirect,request,session,flash

from flaskApp.models.author_mod import Author_cls
from flaskApp.models.book_mod import Book_cls

""" HOME PAGE / INDEX """
@app.route('/')
def authorHome():
    allAuthor = Author_cls.getAllAuthor()
    return render_template("index.html", display_allAuthor = allAuthor)

""" Route invoked on the Add New Dojo page """
@app.route('/createAuthor', methods=["POST"])
def createAuthor():
    data = { # this creates cleared variables, containing cleansed incoming data from the form
        "clr_authorName": request.form["frm_authorName"]
        }
    id = Author_cls.save(data) # creates variable... 'id' ... = that we'll use in next line (represents the ID of newly created record.... oh, and runs the "save" method from server.py)
    # return redirect('/DojoProfile/' + str(id)) 
    return redirect('/') 

@app.route('/authorProfile/<int:id>')
def authorProfile(id):
    data = {
        "clr_id": id
    }
    authorInfo = Author_cls.getOneAuthor(data)
    allBook = Book_cls.getAllBook()
    allAuthorFavBook = Author_cls.get_allAuthorFavBook(data) 
    

    return render_template(
    "authorProfile.html" 
    , display_authorInfo = authorInfo
    , display_allBook = allBook
    , display_allAuthorFavBook = allAuthorFavBook
    
    )

@app.route('/createAuthorFavBook/<int:author_id>', methods=["POST"])
def createAuthorFavBook(author_id):
    data = { # this creates cleared variables, containing cleansed incoming data from the form
        "clr_book_id": request.form["frm_book_id"], 
        "clr_author_id": author_id 
        }
    # dojo_id = data.clr_dojo_id
    id = Author_cls.saveFaveOfAuthor(data) # creates variable... 'id' ... = that we'll use in next line (represents the ID of newly created record.... oh, and runs the "save" method from server.py)
    # return redirect('/DojoProfile/' + str(id)) 
    return redirect('/') 
    # return redirect(f"/dojoProfile/{data['clr_dojo_id']}")

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

"""DON'T TOUCH BELOW :-) below always needs to be at the bottom of the script, yes!"""
# below is stuff you oughta have, per TA Cameron Smith, from Coding Dojo: 

@app.route('/', defaults={'cookies': ''})
@app.route('/<path:cookies>')
def catch_all(cookies):
    return 'Sorry! No response here. Try url again.'


