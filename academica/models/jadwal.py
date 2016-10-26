# -*- coding: utf-8 -*-

from odoo import models, fields, api

class JadwalKuliah(models.Model):
    _name = 'academica.jadwalkuliah'
    _rec_name = "nama"

    nama = fields.Char(required=True)
    deskripsi = fields.Text(required=True)
    dosen = fields.Many2one("academica.dosen")
    ruangan = fields.Many2one("academica.ruangan")
    matakuliah = fields.Many2one("academica.matakuliah")
    mulai_kuliah = fields.Date()
    akhir_kuliah = fields.Date()
    mulai_kontrak = fields.Date()
    akhir_kontrak = fields.Date()
    tahun = fields.Integer(required=True)