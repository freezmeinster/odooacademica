from odoo import models, fields, api

class Ruangan(models.Model):
    _name = 'academica.ruangan'
    _rec_name = 'nama'

    nama = fields.Char(required=True)
    deskripsi = fields.Text(required=True)