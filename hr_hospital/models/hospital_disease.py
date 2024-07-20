from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class HospitalDisease(models.Model):
    _name = 'hospital.disease'
    _description = 'Disease'
    _parent_store = True
    _parent_name = 'parent_id'

    name = fields.Char(required=True)
    parent_id = fields.Many2one(comodel_name='hospital.disease',
                                index=True,
                                ondelete='cascade'
                                )
    parent_path = fields.Char(index=True,
                              unaccent=False)

    child_ids = fields.One2many(comodel_name='hospital.disease',
                                inverse_name='parent_id')

    @api.constrains('parent_id')
    def _check_parent_id(self):
        if not self._check_recursion():
            raise ValidationError(_("You cannot create recursive groups."))
