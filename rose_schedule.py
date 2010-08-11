import cherrypy
from next_class import *
from Cheetah.Template import Template
from datetime import time, date, datetime

class HomePage:
  
  @cherrypy.expose
  def index(self):
    tmpl = Template(file='rose_schedule_template.html')
    tmpl.period = return_difference()
    return str(tmpl)

cherrypy.quickstart(HomePage())
