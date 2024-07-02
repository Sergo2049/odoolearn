from odoo import fields, models


class HospitalPerson(models.AbstractModel):
    _name = 'hospital.person'
    _description = 'Hospital person'

    name = fields.Char(string='Name')
    surname = fields.Char(string='Surname')
    phone = fields.Char(string='Phone')
    gender = fields.Selection(
        selection=[
            ('male', 'Male'),
            ('female', 'Female'),
        ],
        string='Gender'
    )
    image_256 = fields.Image("Image", max_width=256, max_height=256)

