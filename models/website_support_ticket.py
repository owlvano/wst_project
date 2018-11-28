# -*- coding: utf-8 -*-
from odoo import api, fields, models

class WebsiteSupportTicket(models.Model):
    _inherit = "website.support.ticket"

    task_count = fields.Integer(compute='_compute_task_count', string="Tasks")

    def _compute_task_count(self):
        for ticket in self:
            try:
                ticket.task_count = self.env['project.task'].search_count(
                    [('ticket_id', '=', ticket.id)])
            except:
                ticket.task_count = 0
