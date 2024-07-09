from odoo import api, fields, models


class HospitalDoctor(models.Model):

    _name = 'hospital.doctor'
    _description = 'Hospital doctor'
    _inherit = 'hospital.patient'

    specialization = fields.Many2one(
        comodel_name='hospital.doctor.specialization')
    is_intern = fields.Boolean()
    mentor_id = fields.Many2one(comodel_name='hospital.doctor',
                                domain="[('is_intern', '=', False)]")
    @api.onchange('is_intern')
    def check_mentor(self):
        if not self.is_intern:
            self.mentor_id = False
    def get_diagnosis_to_approve(self):
        return{
            'name': 'Diagnosis to approve',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'res_model': 'hospital.diagnosis',
            'target': 'new',
            'domain' : f"[('approved', '=', False), ('doctor_id', '=', {self.ids})]"
        }
