import cherrypy
from next_class import *
from Cheetah.Template import Template
from datetime import time, date, datetime

class HomePage:
  @cherrypy.expose
  def index(self):
    return '''
    <a href="/nextperiod/">Time Till Next Period</a>
    <a href="/largefiles/">Large Files</a>

    '''
  
class TimeTillNextPeriod:
  @cherrypy.expose
  def index(self):
    tmpl = Template(file='rose_schedule_template.html')
    tmpl.period = return_difference()
    return str(tmpl)

class LargeFiles:
  @cherrypy.expose
  def index(self):
    return "large files"

root = HomePage()
root.nextperiod = TimeTillNextPeriod()
root.largefiles = LargeFiles()
cherrypy.tree.mount(root)

cherrypy.quickstart()
