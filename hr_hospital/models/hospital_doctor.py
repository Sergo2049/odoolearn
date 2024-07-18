from odoo import _, api, fields, models
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
        string='Interns',
        comodel_name='hospital.doctor',
        inverse_name='mentor_id',
        readonly=True
    )

    visit_ids = fields.One2many(
        string="Visits",
        comodel_name="hospital.visit",
        inverse_name='doctor_id'
        )

    patient_ids = fields.One2many(
        comodel_name="hospital.patient",
        inverse_name="personal_doctor_id"
        )

    @api.onchange('is_intern')
    def check_mentor(self):
        if not self.is_intern:
            self.mentor_id = False

    @api.constrains('is_intern', 'mentor_id')
    def check_mentor_required(self):
        for res in self:
            if res.is_intern and not res.mentor_id:
                raise ValidationError(_('Intern must have a mentor'))

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

    def action_create_visit(self):
        return {
            'name': 'New visit',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hospital.visit',
            'target': 'new',
            'context': {'default_doctor_id': self.id}
        }

    def get_patients_last_visits(self):

        self.ensure_one()
        last_patients_visits = []

        for patient in self.patient_ids:
            visits = self.env['hospital.visit'].search([('doctor_id', '=', self.id), ('patient_id', '=', patient.id)])
            visits = visits.sorted(key=lambda r: r.create_date, reverse=True)
            last_patients_visits.append(visits[0])
        print(last_patients_visits)
        return last_patients_visits
