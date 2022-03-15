from sqlite3 import connect # ANYONE explain this line? 
from flaskApp.config.mysqlconnection import connectToMySQL # import the function that will return an instance of a connection
from flaskApp.models import book_mod

class Author_cls:
    def __init__( self , data ):
        self.id = data['id']
        self.authorName = data['authorName']
        self.authorFavBookList = [] 
        self.notAuthorFavBookList = []
    
    @classmethod 
    def saveAuthor(cls, data ):
        q = "INSERT INTO author (authorName, createdAt, updatedAt) VALUES ( %(clr_authorName)s , NOW() , NOW() );"
        return connectToMySQL('authorBook_sch').query_db(q, data )

    @classmethod
    def getOneAuthor(cls, data):
        q = 'select * from author where id = %(clr_id)s;'
        results = connectToMySQL("authorBook_sch").query_db(q, data)
        return cls(results[0])

    @classmethod 
    def getAllAuthor(cls):
        q = "SELECT * FROM author;"
        rez = connectToMySQL('authorBook_sch').query_db(q) 
        authorList = [] 
        for rec in rez:
            authorList.append(cls(rec))
        # print("authorList follows:::") # this is a big ole list of objects
        # print(authorList)
        return authorList

    @classmethod
    def get_authorFavBooks(cls, data):
        # q = "select * from author a left join favorite f on a.id = f.author_id left join book b on f.book_id = b.id where a.id = %(clr_id)s;"
        q = "select * from author a join favorite f on a.id = f.author_id join book b on f.book_id = b.id where a.id = %(clr_id)s;"
        results = connectToMySQL('authorBook_sch').query_db(q, data)
        authorFavObj = cls (results[0]) 
        for row in results:
            favorite_data = {
                "id" : row['b.id'], 
                "bookTitle" : row['bookTitle'], 
                "pageCount" : row['pageCount'], 
            }
            authorFavObj.authorFavBookList.append(book_mod.Book_cls(favorite_data))
        return authorFavObj

    """ trying it again... below is boilerplate from above, with edits"""

    @classmethod
    def get_notAuthorFavBooks(cls, data):
        # q = "select * from author a join favorite f on a.id = f.author_id join book b on f.book_id = b.id where a.id = %(clr_id)s;"
        q = "select * from book b where b.id not in (select f.book_id from favorite f where f.author_id = %(clr_id)s);"
        results = connectToMySQL('authorBook_sch').query_db(q, data)
        authorFavObj2 = cls (results[0]) 
        for row in results:
            favorite_dataX = {
                "id" : row['b.id'], 
                "bookTitle" : row['bookTitle'], 
                "pageCount" : row['pageCount'], 
            }
            authorFavObj2.notAuthorFavBookList.append(book_mod.Book_cls(favorite_dataX))
        return authorFavObj2



    @classmethod 
    def saveFaveOfAuthor(cls, data ):
        q = "INSERT INTO favorite (author_id, book_id) VALUES ( %(clr_author_id)s , %(clr_book_id)s  );"
        return connectToMySQL('authorBook_sch').query_db(q, data )

    """ !!!!! below class method not employed on Dojo_cls, but keeping it for future use"""
    @classmethod 
    def update(cls, data ):
        q = "update dojo set dojoName = %(dojoName)s , updatedAt = NOW() where id = %(clr_id)s;"
        return connectToMySQL('dojoNinja_sch').query_db(q, data )
    
    """ !!!!! below class method not employed on Dojo_cls, but keeping it for future use"""
    @classmethod 
    def delete(cls, data ):
        q = "delete from dojo where id = %(clr_id)s;"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojoNinja_sch').query_db(q, data )
