# Import models to register them with Odoo's ORM system
# This file ensures that the specified models are recognized by Odoo when the module is loaded

# Import the Book model, representing individual books in the library
# Import the Genre model, representing categories or classifications of books
# Import the BookLoan model, representing book loan transactions and their details
from . import book, genre, book_loan
