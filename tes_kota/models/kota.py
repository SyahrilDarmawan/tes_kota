from odoo import models, fields, api

class tes_kota(models.Model):
    _name = 'vit.kota'

    name = fields.Char("Name")
    state_id = fields.Many2one("res.country.state", string="State")