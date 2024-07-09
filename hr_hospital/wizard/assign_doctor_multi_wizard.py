from odoo import fields, models


class AssignDoctorWizard(models.TransientModel):
    _name = 'assign.doctor.multi.wizard'
    _description = 'Assign doctor to patients'

    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        string='Doctor')

    def action_assign(self):
        self.ensure_one()
        active_ids = self.env.context.get('active_ids')
        for patient_id in active_ids:
            patient = self.env['hospital.patient'].browse(patient_id)
            patient.personal_doctor_id = self.doctor_id.id
