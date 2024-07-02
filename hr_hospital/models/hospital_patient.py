from odoo import fields, models


class HospitalPatient(models.Model):

    _name = 'hospital.patient'
    _description = 'Hospital patient'
    _inherit = 'hospital.person'

