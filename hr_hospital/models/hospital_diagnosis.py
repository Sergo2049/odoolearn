from odoo import fields, models


class HospitalDiagnosis(models.Model):
    _name = 'hospital.diagnosis'
    _description = 'Diagnosis'

    visit_id = fields.Many2one(
        comodel_name='hospital.visit',
        string='Visit'
    )

    description = fields.Text()

    approved = fields.Boolean()

    disease_id = fields.Many2one(
        comodel_name='hospital.disease',
        string='Disease'
    )

    doctor_id = fields.Many2one(
        related='visit_id.doctor_id')
