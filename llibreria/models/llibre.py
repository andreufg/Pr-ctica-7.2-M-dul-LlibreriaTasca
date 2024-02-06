from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from datetime import datetime

class Llibre(models.Model):
    _name = 'llibre'
    _description = 'Libro'

    nom = fields.Char(string="nom", required=True, unique=True)
    preu = fields.Float(string="preu")
    exemplars = fields.Integer(string="exemplars")
    data = fields.Date(string="data", default=fields.Date.today())
    segonama = fields.Boolean(string="segonama", default=False)
    estat = fields.Selection([('bo'), ('regular'), ('dolent')], string="estat", default='bo')
    prioridad = fields.Integer()

    @api.depends('exemplars')
    def rotura_estoc(self):
        return self.exemplars < 10

    def __str__(self):
        return self.nom


