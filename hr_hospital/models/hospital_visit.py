from odoo import fields, models


class HospitalVisit(models.Model):
    _name = 'hospital.visit'
    _description = 'Diesease'

    status = fields.Selection(
        selection=[
            ('planned', 'Planned'),
            ('finished', 'Finished'),
            ('canceled', 'Canceled'),
        ]
    )
    planned_date = fields.Datetime()
    fact_date = fields.Datetime(default=fields.Date.today)
    doctor = fields.Many2one(comodel_name='hospital.doctor')
    patient = fields.Many2one(comodel_name='hospital.patient')
    diagnosis = fields.Many2one(comodel_name='hospital.diagnosis')