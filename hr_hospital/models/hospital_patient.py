from odoo import api, fields, models
from dateutil.relativedelta import relativedelta


class HospitalPatient(models.Model):

    _name = 'hospital.patient'
    _description = 'Hospital patient'
    _inherit = 'hospital.person'

    personal_doctor_id = fields.Many2one(comodel_name='hospital.doctor')
    birth_date = fields.Date()
    age = fields.Integer(compute='compute_age')
    passport_data = fields.Text()
    contact_person = fields.Char()

    @api.depends('birth_date')
    def compute_age(self):
        for rec in self:
            rec.age = relativedelta(fields.Date.today(), self.birth_date).years


