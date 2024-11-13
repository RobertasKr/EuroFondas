from odoo import models, fields

class Book(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Short Description")
    page_count = fields.Integer(string="Page Count")
    genre_ids = fields.Many2many('library.genre', string="Genres")
