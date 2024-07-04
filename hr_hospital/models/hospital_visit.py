from odoo import api, fields, models
from odoo.exceptions import ValidationError


class HospitalVisit(models.Model):
    _name = 'hospital.visit'
    _description = 'Diesease'

    status = fields.Selection(
        selection=[
            ('planned', 'Planned'),
            ('finished', 'Finished'),
            ('canceled', 'Canceled'),
        ],
        default='planned',
        required=True,
    )
    planned_date = fields.Datetime()
    fact_date = fields.Datetime(default=fields.Date.today)
    doctor_id = fields.Many2one(comodel_name='hospital.doctor')
    patient_id = fields.Many2one(comodel_name='hospital.patient')
    diagnosis_ids = fields.One2many(comodel_name='hospital.diagnosis',
                                    inverse_name='visit_id')

# @api.ondelete