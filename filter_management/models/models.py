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
        res = super().fields_get(allfields, attributes)
        filter_record = self.env['filter.management.wags'].search([('model_id.model','=',self._name)])
        if filter_record:
            all_field = self.env['ir.model.fields'].search([('model_id.model','=',self._name)])
            hide_fields_filter = []
            hide_fields_group_by = []
            for x in filter_record:
                [hide_fields_filter.append(y.name) for y in x.hide_filter_fields]
                [hide_fields_group_by.append(y.name) for y in x.hide_group_by_fields]
            for field in all_field:
                if hide_fields_filter:
                    if field.name in hide_fields_filter:
                        if res.get(field.name):
                            res[field.name]['searchable'] = False
                if hide_fields_group_by:
                    if field.name in hide_fields_group_by:
                        if res.get(field.name):
                            res[field.name]['sortable'] = False
        return res



