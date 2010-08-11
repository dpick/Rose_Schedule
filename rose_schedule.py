import cherrypy
from next_class import *
from Cheetah.Template import Template
from datetime import time, date, datetime

class HomePage:
  @cherrypy.expose
  def index(self):
    return '''
    <a href="/nextperiod/">Time Till Next Period</a>

    '''
  
class TimeTillNextPeriod:
  @cherrypy.expose
  def index(self):
    tmpl = Template(file='rose_schedule_template.html')
    tmpl.period = return_difference()
    return str(tmpl)

root = HomePage()
root.nextperiod = TimeTillNextPeriod()
cherrypy.tree.mount(root)

cherrypy.quickstart()
