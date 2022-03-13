from flaskApp.config.mysqlconnection import connectToMySQL
# from flaskApp.controllers.book_ctrl import bookHome # import the function that will return an instance of a connection
from flaskApp.models import author_mod

class Book_cls:
    def __init__( self , data ):
        self.id = data['id']
        self.bookTitle = data['bookTitle']
        self.pageCount = data['pageCount']
        self.FavesByAuthorList = [] # needs work in sections below

    @classmethod 
    def getAllBook(cls):
        q = "SELECT * FROM book;"
        rez = connectToMySQL('authorBook_sch').query_db(q) 
        bookList = [] 
        for rec in rez:
            bookList.append(cls(rec))
        return bookList

    @classmethod 
    def save(cls, data ):
        q = "INSERT INTO book (bookTitle, pageCount, createdAt, updatedAt) VALUES ( %(clr_bookTitle)s , %(clr_pageCount)s,  NOW() , NOW() );"
        return connectToMySQL('authorBook_sch').query_db(q, data )

    @classmethod
    def getOneBook(cls, data):
        q = 'select * from book where id = %(clr_id)s;'
        results = connectToMySQL("authorBook_sch").query_db(q, data)
        return cls(results[0])

    @classmethod
    def get_allFavesByAuthor(cls, data):
        q = "select * from book b left join favorite f on b.id = f.book_id left join author a on f.author_id = a.id where b.id = %(clr_id)s;"
        rez = connectToMySQL('authorBook_sch').query_db(q, data)
        book = cls (rez[0]) 
        for row in rez:
            favorite_data = {
                "id" : row['id'], 
                "authorName" : row['authorName'], 
            }
            book.FavesByAuthorList.append(author_mod.Author_cls(favorite_data))
        return book

"""

    @classmethod 
    def saveNinja(cls, data ):
        q = "INSERT INTO ninja (firstName, lastName, age,  dojo_id, createdAt, updatedAt) VALUES ( %(clr_firstName)s , %(clr_lastName)s, %(clr_age)s, %(clr_dojo_id)s, NOW() , NOW() );"
        return connectToMySQL('dojoNinja_sch').query_db(q, data )








    @classmethod 
    def get_allx(cls):
        q = "SELECT * FROM ninja;"
        rez = connectToMySQL('dojoNinja_sch').query_db(q) 
        ninjaList = [] 
        for rec in rez:
            ninjaList.append(cls(rec))
        return ninjaList





    @classmethod
    def getOnex(cls, data):
        q = 'select * from ninja where id = %(clr_id)s;'
        results = connectToMySQL("dojoNinja_sch").query_db(q, data)
        return cls(results[0])


    @classmethod 
    def updatex(cls, data ):
        q = "update dojo set ninja = %(dojoName)s , updatedAt = NOW() where id = %(clr_id)s;"
        return connectToMySQL('dojoNinja_sch').query_db(q, data )
    

    @classmethod 
    def deletex(cls, data ):
        q = "delete from ninja where id = %(clr_id)s;"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojoNinja_sch').query_db(q, data )
"""