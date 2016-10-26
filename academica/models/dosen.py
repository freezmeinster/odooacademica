# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Dosen(models.Model):
    _name = 'academica.dosen'
    _rec_name = "nama"

    nama = fields.Char(required=True)
    alamat = fields.Text(required=True)