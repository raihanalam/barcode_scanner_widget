# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Barcode Scanner Widget',
    'version': '1.0',
    'category': '',
    'sequence': 1,
    'author': 'Raihan Alam Hridoy',
    'summary': 'Simple Widget For Barcode Scanner Field',
    'description': """

    This module allows you to use a widget 'scanner_field' to make a field automatic with a barcode scanner,
    where your scanner will scan a value from a barcode and it will give a value in a input field and
    this widget will hit a onchange function which is written for this field with business logic.

""",
    'depends': [],
    'data': [

        ],
    'installable': True,
    'assets': {
        'web.assets_backend': [
            'barcode_scanner_widget/static/src/js/**/*',
        ],
    },
    'license': 'OPL-1',
}
