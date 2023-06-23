from fabric import Connection

with Connection('22792191') as c:
    c.run('mkdir -p /opt/wwc/mysites')
    c.sudo('apt-get install python3-pip -y')
    c.sudo('apt install python3-django -y')
    c.sudo('pip3 install django')
    c.run('django-admin startproject lab')
    c.sudo('chmod 777 ./lab')
    c.run('cd ./lab && python3 manage.py startapp polls')
    c.sudo('mv ./lab /opt/wwc/mysites')
    c.run('cd /opt/wwc/mysites/lab && python3 manage.py runserver 8001')