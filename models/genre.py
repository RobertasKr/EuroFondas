from odoo import models, fields

class Genre(models.Model):
    _name = 'library.genre'
    _description = 'Book Genre'

    name = fields.Char(string="Genre Name", required=True)
