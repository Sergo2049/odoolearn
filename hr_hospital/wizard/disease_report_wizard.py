from odoo import fields, models

class DiseaseMonthlyReport(models.TransientModel):
    _name = 'disease.report.wizard'
    _description = 'Disease monthly report'

    doctor_ids = fields.Many2many('hospital.doctor')
    disease_ids = fields.Many2many('hospital.disease')
    start_date = fields.Date()
    end_date = fields.Date()


    def action_open_wizard(self):
        return {
            'name': 'Create disease monthly report',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'disease.monthly.report.wizard',
            'target': 'new',
            # TODO: add dates by default this minth
            # 'context': {'default_start_date': self.env.user.country_id.id},
        }
    def action_create_report(self):
        self.ensure_one()
        domain = [('disease_id', 'in', self.disease_ids.ids)]

        return {
            'name': 'Diagnosis',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'res_model': 'hospital.diagnosis',
            'target': 'new',
            'domain' : domain
        }
