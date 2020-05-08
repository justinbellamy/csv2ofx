from __future__ import (
    absolute_import, division, print_function, unicode_literals)

from operator import itemgetter

def date_func(trxn):
    tag = trxn['Clearing Date']
    return '{}/{}/{}'.format(tag[:2], tag[3:5], tag[-4:])

mapping = {
    'has_header': True,
    'is_split': False,
    'ccard': 'master',
    'account': 'Apple Card',
    'account_type': 'CCard',
    'currency': 'USD',
    'delimiter': ',',
    'payee': itemgetter('Merchant'),
    'date': date_func,
    'amount': itemgetter('Amount (USD)'),
    'desc': itemgetter('Description'),
    'notes': itemgetter('Category'),
}
