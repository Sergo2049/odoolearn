from odoo import fields, models


class HospitalPatient(models.Model):

    _name = 'hospital.patient'

    _description = 'Hospital patient'

    name = fields.Char()

    surname = fields.Char()

    date = fields.Date()

    active = fields.Boolean()

    yesterday = fields.Date()

    qty = fields.Integer()

    partner_id = fields.Many2one()

    image = fields.Image()
