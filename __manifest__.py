{
    'name': 'Custody',
    'version': '17.0.1.0',
    'author': 'Tijus Academy',
    'summary': 'Handle Properties of Employees where given as from the office',
    'depends': ['base', 'hr'],
    'data': [
        'security/custody_group.xml',
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
        'data/custody_sequence_number.xml',
        'views/view_custody.xml',
        'views/view_custody_property_type.xml',
        'views/hr_employee_inherit.xml',
        'views/view_custody_property.xml',
        'wizard/property_return_date_wizard.xml',
        'views/custody_menu.xml',
    ],
    'application': True,
    'license': 'LGPL-3',

}