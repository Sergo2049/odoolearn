from odoo import fields, models
import datetime


class HospitalPatient(models.Model):

    _name = 'hospital.patient'
    _description = 'Hospital patient'
    _inherit = 'hospital.person'

    personal_doctor = fields.Many2one(comodel_name='hospital.doctor')
    birth_date = fields.Date()
    age = fields.Integer(compute='compute_birth_date')
    contact_person = fields.Char()


    def compute_birth_date(self):
        today = datetime.today()
        birthdate = self.birth_date
        self.age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
