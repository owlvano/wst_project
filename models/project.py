# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models

class Task(models.Model):
    _inherit = "project.task"

    ticket_id = fields.Many2one('website.support.ticket', string='Support Ticket', default=lambda self: self._get_default_ticket_id())

    def _get_default_ticket_id(self):
        """ Gives default ticket_id """
        return self.env.context.get('default_ticket_id') or False
