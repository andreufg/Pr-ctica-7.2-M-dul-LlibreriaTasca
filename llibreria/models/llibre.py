from odoo import models, fields
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from datetime import datetime

class Llibre(models.Model):
    _name = 'llibre'
    _description = 'Libro'

    nom = fields.Char(string="Nombre", required=True, unique=True)
    preu = fields.Float(string="Precio")
    exemplars = fields.Integer(string="Ejemplares")
    data = fields.Date(string="Fecha", default=fields.Date.today())
    segonama = fields.Boolean(string="Segunda Mano", default=False)
    estat = fields.Selection([('bo', 'Bueno'), ('regular', 'Regular'), ('dolent', 'Dolente')], string="Estado", default='bo')

    @property
    def rotura_estoc(self):
        return self.exemplars < 10

    def __str__(self):
        return self.nom


