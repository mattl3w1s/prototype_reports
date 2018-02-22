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

def split_list(list_,break_index=18):
    return [list_[:break_index],list_[break_index:]]

def sort_by_name(list_):
    return sorted(list_,key=lambda x:x.name)

def sanjacify(course):
    SJC_course = session.query(SJC).filter(SJC.UHCL_id == course.id).first()
    if(SJC_course):
        setattr(SJC_course,"style","color:green;font-weight:bold;") 
        return SJC_course
    else:
        setattr(course,"style","")
        return course

def trim(string_):
    return string_.replace(' (lecture)','')

env = Environment(loader=FileSystemLoader('.'))
env.filters["sanjacify"] = sanjacify
env.filters["trim"] = trim
env.filters["sort_by_name"] = sort_by_name
env.filters["split_list"] = split_list
template = env.from_string(template_file)

courses = session.query(SJC)
rubrics = [value[0] for value in session.query(SJC.rubric).distinct().order_by(SJC.rubric)]

template_vars = {
    "courses":courses,
    "rubrics":rubrics,
    "SJC":SJC,
    "session":session
}

html_out = template.render(template_vars)
sys.stdout.write(html_out)