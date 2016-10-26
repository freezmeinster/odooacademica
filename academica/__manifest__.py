{
    'name': "academica",

    'summary': """
        Modul manjemen pendidikan perguruan tinggi""",

    'description': """
        Modul manjemen pendidikan perguruan tinggi
    """,

    'author': "Oleafs Integrasi Mandiri",
    'website': "http://o-leafs.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Academy Fantasy',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/menu.xml',
        'views/dosen.xml',
        'views/mahasiswa.xml',
        'views/ruangan.xml',
        'views/matakuliah.xml',
        'views/jadwalkuliah.xml',
        'views/kontrakkuliah.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}