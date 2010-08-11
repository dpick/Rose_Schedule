import cherrypy
#from next_class import *
from Cheetah.Template import Template
from datetime import time, date, datetime

class HomePage:
  
  @cherrypy.expose
  def index(self):
    tmpl = Template(file='rose_schedule_template.html')
    tmpl.period_phrase = 'It is currently: '
    tmpl.period = '1st' #return_difference()
    return str(tmpl)

if __name__ == '__main__':
  cherrypy.root = HomePage()
  cherrypy.server.start()
