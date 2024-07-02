from odoo import fields, models


class HospitalDoctor(models.Model):

    _name = 'hospital.doctor'
    _description = 'Hospital doctor'
    _inherit = 'hospital.patient'

    specialization = fields.Selection(
        selection=[
            ('cardiologists', 'Cardiologists'),
            ('sermatologists', 'Dermatologists'),
            ('cndocrinologists', 'Endocrinologists'),
            ('gastroenterologists', 'Gastroenterologists'),
            ('physiatrists', 'Physiatrists'),
            ('familyMedicineSpecialists', 'Family medicine specialists'),
        ],
        string="Specialization"
    )
