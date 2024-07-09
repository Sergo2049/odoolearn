from datetime import datetime, time
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class HospitalVisit(models.Model):
    _name = 'hospital.visit'
    _description = 'Diesease'

    active = fields.Boolean(default=True)
    status = fields.Selection(
        selection=[
            ('planned', 'Planned'),
            ('finished', 'Finished'),
            ('canceled', 'Canceled'),
        ],
        default='planned',
        required=True,
    )
    planned_date = fields.Datetime(
        required=True)
    fact_date = fields.Datetime(
        default=fields.Datetime.now(),
        copy=False)
    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        required=True)
    patient_id = fields.Many2one(
        comodel_name='hospital.patient',
        required=True)
    diagnosis_ids = fields.One2many(
        comodel_name='hospital.diagnosis',
        inverse_name='visit_id')

    @api.ondelete(at_uninstall=False)
    def check_visit(self):
        for rec in self:
            if rec.diagnosis_ids:
                raise ValidationError(
                    _('You can not delete vesit with diagnosis.'))

    @api.constrains('doctor_id', 'patient_id', 'fact_date', 'active')
    def check_is_visit_took_plase(self):
        for rec in self:
            if (not rec.new and rec.fact_date
                    and fields.Datetime.now() > rec.fact_date):
                raise ValidationError(
                    _('You can not change doctor, '
                      'patient or date in confirmed visit.'))

            if self.planned_date:
                if rec.search_count([
                    ('patient_id', '=', rec.patient_id.id),
                    ('doctor_id', '=', rec.doctor_id.id),
                    ('planned_date', '>=', datetime.combine(
                        rec.planned_date.date(), time.min)),
                    ('planned_date', '<=', datetime.combine(
                        rec.planned_date.date(), time.max)),

                ]) > 1:
                    raise ValidationError(
                        _('You can not plan more then one '
                          'patient visit to same doctor in that day.'))
            if self.diagnosis_ids and not self.active:
                raise ValidationError(
                    _('You can not archive when visit conteins diagnosis.'))

    @api.depends('planned_date', 'patient_id', 'doctor_id')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = (f'{rec.planned_date} '
                                f'-- P: {rec.patient_id.name} '
                                f'--D: {rec.doctor_id.name}')
