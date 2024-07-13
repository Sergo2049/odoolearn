from odoo import api, fields, models
from odoo.exceptions import ValidationError

class HospitalDoctor(models.Model):

    _name = 'hospital.doctor'
    _description = 'Hospital doctor'
    _inherit = 'hospital.person'

    specialization = fields.Many2one(
        comodel_name='hospital.doctor.specialization')

    is_intern = fields.Boolean()

    mentor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        domain="[('is_intern', '=', False)]"
    )
    intern_ids = fields.One2many(
        string='interns',
        comodel_name='hospital.doctor',
        inverse_name='mentor_id',
        readonly=True
    )

    @api.onchange('is_intern')
    def check_mentor(self):
        if not self.is_intern:
            self.mentor_id = False

    @api.constrains('is_intern', 'mentor_id')
    def check_mentor_required(self):
        for res in self:
            if res.is_intern and not res.mentor_id:
                raise ValidationError('Intern must have a mentor')

    def get_diagnosis_to_approve(self):

        return {
            'name': 'Diagnosis to approve',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'res_model': 'hospital.diagnosis',
            'target': 'new',
            'domain': "["
                      "('approved', '=', False), "
                      f"('doctor_id', '=', {self.ids})"
                      "]"
        }
