# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Categoria(models.Model):
    _name = 'categoria'
    _description = 'Categoría de libreria'
    _rec_name="libro"

    nom = fields.Char(string="Nombre", required=True, help="Introduce el nombre de la categoría")
    libro = fields.Char()
    prioridad = fields.Integer()
    urgente = fields.Boolean(compute="_value_urgente", store=True)
    realizada = fields.Boolean()

    @api.depends('prioridad')
    #Funcion para calcular el valor de urgente.
    def _value_urgente(self):
        #Para cada registro
        for record in self:
            #Si la prioridad es mayor que 10, se considera urgente, en otro caso no lo es
            if record.prioridad>10:
                record.urgente = True
            else:
                record.urgente = False
