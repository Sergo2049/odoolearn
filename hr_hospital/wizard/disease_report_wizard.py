from odoo import fields, models


class DiseaseReport(models.TransientModel):
    _name = 'disease.report.wizard'
    _description = 'Disease report'

    doctor_ids = fields.Many2many('hospital.doctor')
    disease_ids = fields.Many2many('hospital.disease')
    start_date = fields.Date(
        required=True
    )
    end_date = fields.Date(
        required=True
    )

    def action_open_wizard(self):
        return {
            'name': 'Create disease report',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'disease.report.wizard',
            'target': 'new',
        }

    def action_create_report(self):

        self.ensure_one()
        domain = [
            ('visit_id.fact_date', '>=', self.start_date),
            ('visit_id.fact_date', '<=', self.end_date)
        ]

        if self.disease_ids:
            domain.append(('disease_id', 'in', self.disease_ids.ids))
        if self.doctor_ids:
            domain.append(('visit_id.doctor_id', 'in', self.doctor_ids.ids))
        return {
            'name': 'Diagnosis',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'res_model': 'hospital.diagnosis',
            'target': 'new',
            'domain': domain,
            'context': {'group_by': 'disease_id'}
        }
