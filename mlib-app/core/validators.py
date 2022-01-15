import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def is_isbn13(value):
    '''Checks if ISBN number is correct'''
    value = str(value)
    if len(value) != 13:
        return False
    product = (sum(int(ch) for ch in value[::2])
               + sum(int(ch) * 3 for ch in value[1::2]))
    return product % 10 == 0


def validate_isbn13(value):
    '''Validator for isbn13 value'''
    if not is_isbn13(value):
        raise ValidationError(
            _('%(value)s is not correct ISBN number'),
            params={'value': value},
        )


def validate_title(value):
    '''Validator for title of the book'''
    if not (2 <= len(value) or len(value) <= 255):
        raise ValidationError(
            _('%(value)s is not correct title, please use 2-255 characters.'),
            params={'value': value},
        )


def validate_pages_count(value):
    '''Validator for numbers in pages_count field.'''
    if isinstance(value, str):
        if value.isnumeric():
            value = float(str)
            result = (value > 1 or value < 10000)
    elif isinstance(value, int):
        result = (value > 1 or value < 10000)
    elif not result:
        raise ValidationError(
            _('''%(value)s is not correct number of pages.
            Please use number between 1-10000.'''),
            params={'value': value},
        )


def validate_pub_lang(value):
    '''Validate two-letters ISO country code'''
    country_codes = ['AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BQ', 'BA', 'BW', 'BV', 'BR', 'IO', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CA', 'CV', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU', 'CW', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'VA', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'KP', 'KR', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MK', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', '""', 'NR', 'NP', 'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'MP', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'BL', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'SS', 'ES', 'LK', 'SD', 'SR', 'SJ', 'SZ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UG', 'UA', 'AE', 'GB', 'US', 'UM', 'UY', 'UZ', 'VU', 'VE', 'VN', 'VG', 'VI', 'WF', 'EH', 'YE', 'ZM', 'ZW']
    value = value.upper()
    if value not in country_codes:
        raise ValidationError(
            _('%(value)s is not correct country code.'),
            params={'value': value},
        )


def validate_cover_link(value):
    '''Validade if value in cover_link is apriopriate'''
    if value:
        result = re.match(r'(?:http\:|https\:)?\/\/.*', value)
        if result is None:
            raise ValidationError(
                _("%(value)s is not correct image link."),
                params={'value': value},
                )


def validate_published_year(value):
    '''Validate if year of publication is between 0-2022'''
    if isinstance(value, str):
        if value.isnumeric():
            value = float(str)
            result = (0 <= value <= 2022)
    elif isinstance(value, int):
        result = (0 <= value <= 2022)
    elif not result:
        raise ValidationError(
            _('%(value)s is not correct year of publication. \
            Please use number between 0-2022.'),
            params={'value': value},
            )
