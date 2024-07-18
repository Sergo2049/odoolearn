{
    'name': 'Hospital',
    'version': '17.0.1.0.0',
    'category': 'Medicine',
    'summary': """Hospital management""",
    'license': 'LGPL-3',
    'author': 'Serhii Vydysh',
    'website': 'http://google.com',
    "sequence": -200,
    'depends': [
        'base',
    ],
    'data': [
        "security/ir.model.access.csv",
        "views/hospital_diagnosis_views.xml",
        "views/hospital_doctor_views.xml",
        "views/hospital_patient_views.xml",
        "views/hospital_visit_views.xml",
        "views/hospital_diasease_views.xml",
        "views/hospital_menus.xml",
        "wizard/assign_doctor_multi_wizard_views.xml",
        "wizard/disease_report_wizard_views.xml",
        "reports/report_doctor.xml"
    ],
    'demo': [
        "demo/hospital_demo.xml",
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
