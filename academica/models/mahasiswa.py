from odoo import models, fields, api

class Mahasiswa(models.Model):
    _name = 'academica.mahasiswa'
    _rec_name="nama"

    nama = fields.Char(required=True)
    nim = fields.Char(required=True)
    alamat = fields.Text(required=True)