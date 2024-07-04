from odoo import fields, models


class HospitalDiagnosis(models.Model):
    _name = 'hospital.diagnosis'
    _description = 'Diagnosis'

    visit_id = fields.Many2one(comodel_name='hospital.visit')
    disease_id = fields.Many2one(comodel_name='hospital.disease')
    description = fields.Text()
    approved = fields.Boolean()
