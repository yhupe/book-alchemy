import os
from flask import Flask, request, render_template
from data_models import db, Author, Book


app = Flask(__name__)

DB_DIR = "/Users/hannespickel/PycharmProjects/book-alchemy/data"
DB_PATH = os.path.join(DB_DIR, 'library.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'


db.init_app(app)

# creating authors and books table in the library.sqlite database
"""with app.app_context():
    db.create_all()"""


@app.route('/', methods=['GET'])
def home():
    """Endpoint queries books table and passes all
    existing books to the home.html document."""

    books = Book.query.all()

    print(f"All records from table 'books' loaded successful")
    return render_template('home.html', books=books), 200


@app.route('/sort', methods=['GET'])
def sort_books():
    """ Endpoint sorts book objects according to
    what entity was selected and requested through
    the sorting form in the home.html file
    By default sorted by title."""

    # default sorting by title
    sort_by = request.args.get('sort_by', 'title')

    if sort_by == 'title':
        books = Book.query \
            .order_by(Book.title) \
            .all()
    elif sort_by == 'year':
        books = Book.query \
            .order_by(Book.publication_year) \
            .all()
    elif sort_by == 'author':
        books = Book.query \
            .join(Author)\
            .order_by(Author.name)\
            .all()
    else:
        books = Book.query.all()

    print(f"Sorting by {sort_by} was successful")
    return render_template('home.html', books=books), 200


@app.route('/search', methods=['GET'])
def search_books():
    """ Endpoint searches book objects according to
        what key word was requested through
        the searching form in the home.html file.
        The query is similar to SQL LIKE, as it returns all
        objects with the particular search term in their title.
        If not found any, no books are shown."""

    search_query = request.args.get('search_query', None)
    books = Book.query.filter(Book.title.ilike(f'%{search_query}%')).all()

    if len(search_query) > 0 and len(books) > 0:
        print(f"Search for '{search_query}' was successful")
        return render_template('home.html', books=books), 200

    else:
        print(f"Search for '{search_query}' was not successful "
              f"(empty search bar or no matches in DB)")
        return f"No results found for '{search_query}'", 404


@app.route('/book/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    """ Via a delete form (POST method) in the home.html file
    in form of a submit button, the book id is passed to the endpoint
    and then the books table is queried with this book id.
    If found, the book object will be deleted, else, a 404 error is returned.
    In case that the amount of books for an author becomes zero after a book deletion,
    the author will be deleted after the book deletion. """

    book = Book.query.get_or_404(book_id)
    author = book.author

    db.session.delete(book)
    db.session.commit()

    # Checking whether the book deletion deleted the last book object belonging to an author
    remaining_books_by_author = Book.query \
        .filter_by(author_id=author.author_id) \
        .count()
    if remaining_books_by_author == 0:
        db.session.delete(author)
        db.session.commit()

        return (f"Book '{book.title}' and author '{author.name}' "
                f"have been deleted successfully.")

    return f"Book '{book.title}' has been deleted successfully."


@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    """ Get request returns the html file for adding a new author to the authors table.
    Post request fetches details about author as entered to the form and
    creates a new author object which then is being added to the authors table."""

    if request.method == 'GET':
        return render_template('add_author.html'), 200

    if request.method == 'POST':

        author_name = request.form.get('name')
        birth_date = request.form.get('birthdate')
        death_date = request.form.get('date_of_death')

        author = Author(
            name = author_name,
            birthdate = birth_date,
            date_of_death = death_date
        )

        with app.app_context():
            db.session.add(author)
            db.session.commit()
            print(f"New author '{author_name}' has been added successfully")

        return f"New author '{author_name}' has been added successfully"


@app.route('/add_books', methods=['GET', 'POST'])
def add_book():
    """ Get request returns the html file for adding a new book to the authors table.
        Post request fetches details about book as entered to the form and
        creates a new book object which then is being added to the books table."""

    authors = Author.query.all()

    # All authors from 'authors' table are passed to the html template --> dropdown
    if request.method == 'GET':
        return render_template('add_book.html', authors=authors), 200

    if request.method == 'POST':

        book_title = request.form.get('title')
        isbn_number = request.form.get('isbn')
        publication_year = request.form.get('publication_year')
        book_author = request.form.get('author_id')

        with app.app_context():

            author = Author.query.get(book_author)

            if author:
                book = Book(
                    title=book_title,
                    ISBN=isbn_number,
                    publication_year=publication_year,
                    author_id=author.author_id
                )

                db.session.add(book)
                db.session.commit()
                print(f"Book '{book_title}' added successfully!")

        return f"Book '{book_title}' added successfully"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

