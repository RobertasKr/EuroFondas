# Import the necessary modules from Odoo
from odoo import models, fields


class Book(models.Model):
    """
    This model represents a book in the library.
    It contains essential information about the book, such as its title,
    description, page count, and associated genres.
    """

    # Define the name and description of the model
    _name = 'library.book'  # Technical name for the model, used in database
    _description = 'Library Book'  # Human-readable description of the model

    # Define fields for the model

    # Title of the book; required field to ensure each book has a name
    name = fields.Char(string="Title", required=True)

    # Short description of the book, providing additional details (optional)
    description = fields.Text(string="Short Description")

    # Total number of pages in the book; integer field
    page_count = fields.Integer(string="Page Count")

    # Many-to-many relationship with the genre model, allowing a book to belong to multiple genres
    genre_ids = fields.Many2many('library.genre', string="Genres")
