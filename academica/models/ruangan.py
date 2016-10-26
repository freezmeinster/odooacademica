from odoo import models, fields, api

class Ruangan(models.Model):
    _name = 'academica.ruangan'

    nama = fields.Char(required=True)
    deskripsi = fields.Text(required=True)