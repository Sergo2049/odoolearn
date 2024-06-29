from odoo import fields, models

class HospitalPatient(models.Model):

    _name = 'hospital.patient'

    _description = 'Hospital patient'

    name = fields.Char(string='Name')

    surname = fields.Char(string='Surname')

    date = fields.Date(string='Date')

    active = fields.Boolean(default=True)

    yesterday = fields.Date(string='Yesterday')

    qty = fields.Integer(string='Amount')

    partner_id = fields.Many2one(comodel_name='res.partner')

    image = fields.Image()
