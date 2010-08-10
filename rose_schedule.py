import cherrypy
from Cheetah.Template import Template
from datetime import time, date, datetime

class HomePage:
  
  @cherrypy.expose
  def index(self):
    tmpl = Template(file='rose_schedule_template.html')
    tmpl.period_phrase = 'It is currently: '
    tmpl.period = self.get_period()
    return str(tmpl)

  def get_period(self):
    periods = [('1st', time( 8,  5)),
               ('2nd', time( 9,  0)),
               ('3rd', time( 9, 55)),
               ('4th', time(10, 50)),
               ('5th', time(11, 45)),
               ('6th', time(12, 40)),
               ('7th', time(13, 35)),
               ('8th', time(14, 30)),
               ('9th', time(16, 25)),
               ('10th', time(17, 20))]

    for period, period_time in periods:
      if datetime.now().time() < period_time:
        return period

if __name__ == '__main__':
  cherrypy.root = HomePage()
  cherrypy.server.start()
