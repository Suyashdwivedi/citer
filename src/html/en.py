#! /usr/bin/python
# -*- coding: utf-8 -*-

"""HTML skeleton of the application and its predefined responses."""


from string import Template
from os import name as osname
from zlib import adler32


# Predefined responses
DEFAULT_SFN_CIT_REF = (
    'Generated citation will appear here...', '', '',
)

UNDEFINED_INPUT_SFN_CIT_REF = (
    'Undefined input.',
    'Sorry, the input was not recognized. The error was logged.',
    '',
)

HTTPERROR_SFN_CIT_REF = (
    'HTTP error:',
    'One or more of the web resources required to '
    'create this citation are not accessible at this moment.',
    '',
)

OTHER_EXCEPTION_SFN_CIT_REF = (
    'An unknown error occurred.',
    'The error was logged.',
    '',
)

CSS = open('src/html/en.css', 'rb').read()
CSS_HEADERS = [
    ('Content-Type', 'text/css; charset=UTF-8'),
    ('Content-Length', str(len(CSS))),
    ('Cache-Control', 'immutable, public, max-age=31536000'),
]

JS = open('src/html/en.js', 'rb').read()
# Invalidate cache after css change.
JS_HEADERS = [
    ('Content-Type', 'application/javascript; charset=UTF-8'),
    ('Content-Length', str(len(JS))),
    ('Cache-Control', 'immutable, public, max-age=31536000'),
]

# None-zero-padded day directive is os dependant ('%#d' or '%-d')
# See http://stackoverflow.com/questions/904928/
HTML_SUBST = Template(
    open('src/html/en.html', encoding='utf8').read().replace(
        # Invalidate css cache after any change in css file.
        '"stylesheet" href="./static/en',
        '"stylesheet" href="./static/en' + str(adler32(CSS)),
        1,
    ).replace(
        # Invalidate js cache after any change in js file.
        'src="./static/en',
        'src="./static/en' + str(adler32(JS)),
        1,
    )
    .replace('~d', '%#d' if osname == 'nt' else '%-d')
).substitute


def sfn_cit_ref_to_html(sfn_cit_ref: tuple, date_format: str, input_type: str):
    """Insert sfn_cit_ref into the HTML template and return response_body."""
    date_format = date_format or '%Y-%m-%d'
    sfn, cit, ref = sfn_cit_ref
    return HTML_SUBST(
        sfn=sfn, cit=cit, ref=ref,
    ).replace(date_format + '"', date_format + '" checked', 1).replace(
        '="' + input_type + '"', '="' + input_type + '" selected', 1
    )
