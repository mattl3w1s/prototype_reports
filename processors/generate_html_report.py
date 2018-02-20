# -*- coding: utf-8 -*-

"""
Prototype Reports
~~~~~~~~~~~~~~~~~

:copyright: (c) 2017-2018 by San Jacinto College
:license: unspecificed


"""
import sys
from jinja2 import Environment, FileSystemLoader
from db import db_connect,Course,Program

template_file = sys.stdin.read()

session = db_connect()
env = Environment(loader=FileSystemLoader('.'))
template = env.from_string(template_file)

programs = session.query(Program).order_by(Program.name)

template_vars = {
    "title":"This Title is Test!",
    "programs":programs
}

html_out = template.render(template_vars)
sys.stdout.write(html_out)