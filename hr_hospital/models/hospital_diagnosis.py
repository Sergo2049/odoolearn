from odoo import fields, models


class HospitalDiagnosis(models.Model):
    _name = 'hospital.diagnosis'
    _description = 'Diagnosis'

    visit = fields.Many2one(comodel_name='hospital.visit')
    disease = fields.Many2one(comodel_name='hospital.visit')
    description = fields.Text()
    approved = fields.Boolean()
