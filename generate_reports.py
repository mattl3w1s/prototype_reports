# -*- coding: utf-8 -*-

"""
Prototype Reports
~~~~~~~~~~~~~~~~~

:copyright: (c) 2017-2018 by San Jacinto College
:license: unspecificed


"""

from jinja2 import Environment, FileSystemLoader
from db import db_connect,Course

session = db_connect()
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("templates/template.html")

template_vars = {
    "title":"This Title is Test!"
}

html_out = template.render(template_vars)
with open('finished/file.html','w') as f:
    f.write(html_out) 