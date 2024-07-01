from odoo import fields, models


class HospitalVisit(models.Model):
    _name = 'hospital.visit'
    _description = 'Diesease'

    date = fields.Date(default=fields.Date.today)
    patient = fields.Many2one(comodel_name='hospital.patient')
    disease = fields.Many2one(comodel_name='hospital.disease')
