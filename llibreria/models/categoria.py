from odoo import models, fields

class Categoria(models.Model):
    _name = 'categoria'
    _description = 'Categoría de Tareas'

    nom = fields.Char(string="Nombre", required=True, help="Introduce el nombre de la categoría")
    descripcio = fields.Text(string="Descripción")


