from odoo import fields, models

class HospitalDoctor(models.Model):

    _name = 'hospital.doctor'
    _description = 'Hospital patient'

    name = fields.Char(string='Name')

    surname = fields.Char(string='Surname')

    type = fields.Selection(
        selection=[
            ('cardiologists', 'Cardiologists'),
            ('sermatologists',' Dermatologists'),
            ('cndocrinologists', 'Endocrinologists'),
            ('gastroenterologists','Gastroenterologists'),
            ('physiatrists', 'Physiatrists'),
            ('familyMedicineSpecialists', 'Family medicine specialists'),
        ],
    )
