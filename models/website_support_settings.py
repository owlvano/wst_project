# -*- coding: utf-8 -*-
from odoo import api, fields, models

class WebsiteSupportSettings(models.TransientModel):

    _inherit = "website.support.settings"
    ticket_project_id = fields.Many2one('project.project', string="Website Support Project")

    #-----Website Support Project-----

    @api.multi
    def get_default_ticket_project_id(self, fields):
        return {'ticket_project_id': self.env['ir.values'].get_default('website.support.settings', 'ticket_project_id')}

    @api.multi
    def set_default_ticket_project_id(self):
        for record in self:
            self.env['ir.values'].set_default('website.support.settings', 'ticket_project_id', record.ticket_project_id)
