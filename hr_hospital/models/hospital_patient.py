from odoo import fields, models


class HospitalPatient(models.Model):

    _name = 'hospital.patient'

    _description = 'Hospital patient'

    name = fields.Char()

    surname = fields.Char()
