# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class jpm_trigger(models.Model):
#     _name = 'jpm_trigger.jpm_trigger'
#     _description = 'jpm_trigger.jpm_trigger'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
