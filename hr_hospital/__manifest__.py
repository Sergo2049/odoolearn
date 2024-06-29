{
    'name': 'Hospital',
    'version': '17.0.1.0.0',
    'category': 'Medicine',
    'summary': """Hospital management""",
    'license': 'LGPL-3',
    'author': 'Serhii Vydysh',
    'website': 'http://google.com',
    "sequence": "-200",
    'depends': [
        'base',
    ],
    'data': [
        "security/ir.model.access.csv",
        "views/hospital_views.xml",
    ],
    'demo': [
        "demo/hospital_demo.xml",
    ],
   # 'support': 'school@garazd.biz',
    'application': False,
    'installable': True,
    'auto_install': False,
}