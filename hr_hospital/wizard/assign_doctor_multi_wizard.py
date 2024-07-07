from odoo import fields, models

class AssignDoctorWizard(models.TransientModel):
    _name = 'assign.doctor.multi.wizard'
    _description = 'Assign doctor to patients'

    doctor_id = fields.Many2one(comodel_name='hospital.patient', string='Doctor')

    def action_assign(self):
        return
