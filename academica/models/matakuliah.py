# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MataKuliah(models.Model):
    _name = 'academica.matakuliah'
    _rec_name = "nama"

    nama = fields.Char(required=True)
    deskripsi = fields.Text(required=True)