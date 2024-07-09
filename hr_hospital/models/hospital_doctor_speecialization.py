from odoo import fields, models


class HospitalDoctorSpecialization(models.Model):

    _name = 'hospital.doctor.specialization'
    _description = 'Doctor specialization'

    name = fields.Char()
