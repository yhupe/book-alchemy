
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


## Other things

Tried my web application? I'd love to hear your feedback!  
I'm still at the start of my programming journey, so any thoughts or suggestions would mean a lot.  
 Or if you encounter any bugs or unexpected behaviour, feel free to give me a hint!
  
  Thanks! 

## 🤙🏼
