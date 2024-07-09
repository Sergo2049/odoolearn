from odoo import api, fields, models


class HospitalPerson(models.AbstractModel):
    _name = 'hospital.person'
    _description = 'Hospital person'

    name = fields.Char(string='Name',
                       required=True)
    surname = fields.Char(string='Surname',
                          required=True)
    phone = fields.Char(string='Phone')
    gender = fields.Selection(
        selection=[
            ('male', 'Male'),
            ('female', 'Female'),
        ],
        string='Gender',
        required=True,
        default='male'
    )
    image_256 = fields.Image("Image", max_width=256, max_height=256)

    @api.depends('name', 'surname')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f'{rec.name} {rec.surname}'


