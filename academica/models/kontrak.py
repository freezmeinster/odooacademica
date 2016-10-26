# -*- coding: utf-8 -*-

from odoo import models, fields, api

class KontrakKuliah(models.Model):
    _name = 'academica.kontrakkuliah'
    
    SEMESTER_TYPE = (
        ("semester_1","Semester 1"),
        ("semester_2","Semester 2"),
        ("semester_3","Semester 3"),
        ("semester_4","Semester 4"),
        ("semester_5","Semester 5"),
        ("semester_6","Semester 6"),
        ("semester_7","Semester 7"),
        ("semester_8","Semester 8"),
        ("semester_9","Semester 9"),
        ("semester_10","Semester 10"),
        ("semester_11","Semester 11"),
        ("semester_12","Semester 12"),
        ("semester_pendek","Semester Pendek"),
    )
    
    jadwal_kuliah = fields.Many2one("academica.jadwalkuliah")
    mahasiswa = fields.Many2one("academica.mahasiswa")
    nilai_akhir = fields.Char(size=2)
    semester = fields.Selection(selection=SEMESTER_TYPE)