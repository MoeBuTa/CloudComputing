from fabric import Connection
import os

with Connection('22792191') as c:
    c.sudo('rm /opt/wwc/mysites/lab/polls/views.py')
    c.sudo('rm /opt/wwc/mysites/lab/lab/urls.py')
    os.system('scp ./polls/views.py 22792191:/opt/wwc/mysites/lab/polls')
    os.system('scp ./polls/urls.py 22792191:/opt/wwc/mysites/lab/polls')
    os.system('scp ./lab/urls.py 22792191:/opt/wwc/mysites/lab/lab')
    c.run('cd /opt/wwc/mysites/lab && python3 manage.py runserver 8001')