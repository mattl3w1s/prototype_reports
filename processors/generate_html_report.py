# -*- coding: utf-8 -*-

"""
Prototype Reports
~~~~~~~~~~~~~~~~~

:copyright: (c) 2017-2018 by San Jacinto College
:license: unspecificed


"""
import sys
from jinja2 import Environment, FileSystemLoader
from db import db_connect,Course,Program,SJC



template_file = sys.stdin.read()

session = db_connect()
def sanjacify(course):
    SJC_course = session.query(SJC).filter(SJC.UHCL_id == course.id).first()
    if(SJC_course):
        return SJC_course
    else:
        return course

def trim(string_):
    return string_.replace(' (lecture)','')


env = Environment(loader=FileSystemLoader('.'))
env.filters["sanjacify"] = sanjacify
env.filters["trim"] = trim
template = env.from_string(template_file)

programs = session.query(Program).order_by(Program.name)

template_vars = {
    "title":"This Title is Test!",
    "programs":programs
}

html_out = template.render(template_vars)
sys.stdout.write(html_out)