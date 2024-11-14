# Import the necessary modules from Odoo
from odoo import models, fields


class Genre(models.Model):
    """
    This model represents a book genre in the library system.
    Each genre serves as a category or classification for books,
    helping users and the library organize books by type or subject.
    """

    # Define the name and description of the model
    _name = 'library.genre'  # Technical name for the model, used internally by Odoo
    _description = 'Book Genre'  # Human-readable description of the model

    # Define fields for the model

    # Name of the genre; required field to ensure each genre has a title or label
    name = fields.Char(string="Genre Name", required=True)
