from odoo import api, fields, models


class HospitalPerson(models.AbstractModel):
    _name = 'hospital.person'
    _description = 'Hospital person'

    name = fields.Char()

    phone = fields.Char()

    gender = fields.Selection(
        selection=[
            ('male', 'Male'),
            ('female', 'Female'),
        ],
        required=True,
        default='male'
    )
    image_256 = fields.Image("Image", max_width=256, max_height=256)

