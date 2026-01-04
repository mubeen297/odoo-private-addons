# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, AccessError
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta


class FilterManagementWags(models.Model):
    _name = 'filter.management.wags'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = 'Filter Management Wags'
    _rec_name = "model_id"

    _sql_constraints = [
        (
            'unique_model_filter_management',
            'unique(model_id)',
            'You cannot create multiple Filter Management records for the same model.'
        )
    ]


    model_id = fields.Many2one("ir.model",tracking=True,string="Model",ondelete='cascade')
    hide_filter_fields = fields.Many2many("ir.model.fields", 'model_fields_filter',
        'model_fields_filter_record_id',
        'tag_fields_filter_record_id',  tracking=True,string="Hide Filter Fields",ondelete='cascade')
    hide_group_by_fields = fields.Many2many("ir.model.fields",'model_fields_group_by',
        'model_fields_group_by_record_id',
        'tag_fields_group_by_record_id', tracking=True,string="Hide GroupBY Fields",ondelete='cascade')





class BaseInheritFilter(models.AbstractModel):
    _inherit = 'base'


    @api.model
    def fields_get(self, allfields=None, attributes=None):
        res = super().fields_get(allfields=allfields, attributes=attributes)

        filter_records = self.env['filter.management.wags'].sudo().search([
            ('model_id.model', '=', self._name)
        ])

        if not filter_records:
            return res

        # Collect hidden fields
        hide_filter_fields = set()
        hide_group_by_fields = set()

        for rec in filter_records:
            hide_filter_fields.update(rec.hide_filter_fields.mapped('name'))
            hide_group_by_fields.update(rec.hide_group_by_fields.mapped('name'))

        for field_name, field_attrs in res.items():
            if field_name in hide_filter_fields:
                field_attrs['searchable'] = False

            if field_name in hide_group_by_fields:
                field_attrs['groupable'] = False

        return res
