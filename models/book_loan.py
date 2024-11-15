# Import the necessary modules from Odoo
from odoo import models, fields, api
from datetime import date


class BookLoan(models.Model):
    """
    This model represents a book loan record in the library system.
    It tracks the details of a loan transaction, including start and end dates,
    the books borrowed, the contact (borrower), and the loan's status.
    """

    # Define the name and description of the model
    _name = 'library.book.loan'  # Technical name for the model, used internally by Odoo
    _description = 'Book Loan'  # Human-readable description of the model

    # Define fields for the model

    # Start date of the loan; required field to ensure each loan has a start date
    start_date = fields.Date(string="Start Date", required=True)

    # End date of the loan; required field to ensure each loan has an end date
    end_date = fields.Date(string="End Date", required=True)

    # Many-to-many relationship with books, allowing multiple books to be borrowed in a single loan
    book_ids = fields.Many2many('library.book', string="Books")

    # Many-to-one relationship with contact (partner), linking a loan to a specific contact (borrower)
    contact_id = fields.Many2one('res.partner', string="Contact", required=True)

    # Selection field representing the status of the loan
    # Initial status defaults to 'reserved' when a new loan is created
    state = fields.Selection([
        ('reserved', 'Reserved'),  # Reserved: Loan reserved but not yet issued
        ('issued', 'Issued'),  # Issued: Loaned out to the contact
        ('returned', 'Returned'),  # Returned: Loan returned to the library
        ('canceled', 'Canceled'),  # Canceled: Loan canceled before completion
    ], string="Status", default='reserved', required=True)

    @api.model
    def send_overdue_reminders(self):
        """
        Checks all book loans for overdue entries and sends reminders
        to the associated contacts.
        """
        overdue_loans = self.search([
            ('end_date', '<', date.today()),  # End date is in the past
            ('state', '=', 'issued')          # Loan is still issued
        ])
        for loan in overdue_loans:
            if loan.contact_id.email:
                # Logically, here you would send an email, but we'll log for now.
                self.env['mail.mail'].create({
                    'subject': 'Overdue Book Reminder',
                    'body_html': f'<p>Dear {loan.contact_id.name},</p>'
                                 f'<p>You have overdue books. Please return them as soon as possible.</p>',
                    'email_to': loan.contact_id.email,
                }).send()

        return True
