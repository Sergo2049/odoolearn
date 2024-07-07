from odoo import api, fields, models
from odoo.exceptions import ValidationError


class HospitalDisease(models.Model):
    _name = 'hospital.disease'
    _description = 'Disease'

    name = fields.Char()
    parent_id = fields.Many2one(comodel_name='hospital.disease',
                                index=True)
    parent_path = fields.Char()

    @api.constrains('parent_id')
    def _check_recursion(self):
        if not self._check_recursion():
            raise ValidationError("You cannot create recursive groups.")