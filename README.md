
# 📚 BOOK ALCHEMY 🧙🏻‍♀️

## Description
This little project called BOOK ALCHEMY is - as you might can guess from it's name already - dedicated to the __ORM library SQLAlchemy__ and represents the next milestone on my journey: __relational databases aka SQL__. 

### 📂 SQLAlchemy
SQLAlchemy, a powerful object-relational mapper (ORM) is used to define the structure of the database. Two main entities (Author and Book) were modeled. A 1:N relationship (One auhor can release many books) between these two entities was built, hence the Author ID is the foreign key in the Books table, linking to the Authors table.

### 🔚 Flask-SQLAlchemy
The Flask extension facilitates the integration of SQLAlchemy into web applications. Endpoints (routes) were defined to fulfil CRUD operations on the database tables 'books' and 'authors'.  

Queries to the database become wrapped up in HTML templates to display the contents, using Jinja2.  
  
Also, HTML forms submitted by the user are being processed to add records to the database. Further, it is possible to sort the records or search within them with key words - all done through HTML forms and Flask-SQLAlchemy.



## How to use 🧭

First, please make sure to install all requirements needed via 

```pip
pip install -r requirements.txt
```

Then, run the web application __app.py__ on port:5000:
```python
python app.py
```
Further, open http://127.0.0.1:5000 in your terminal and you'll be guided to the landing page where you will be able to see all book records added so far.  

http://127.0.0.1:5000/add_author will lead you to the html form to add an author - Name and Date of Birth are required. __You have to add an author first before you continue to add a book title!__. 

http://127.0.0.1:5000/add_books leads you to another form where you can add the acutal book - all fields are required.   
  
The delete button under each book record is self-explanatory but there is one speciality: once you have deleted all books linked to an author, the author will be deleted from the database table 'authors' as well.  

To get back to the landing page, refer to http://127.0.0.1:5000 again since I haven't had the time yet to expand any further. 

## Other things

Tried my web application? I'd love to hear your feedback!  
I'm still at the start of my programming journey, so any thoughts or suggestions would mean a lot.  
 Or if you encounter any bugs or unexpected behaviour, feel free to give me a hint!
  
  Thanks! 

## 🤙🏼
