import os
from fabric import Connection


with Connection('22792191') as c:
    c.sudo('apt update -y')
    c.sudo('apt upgrade -y')
    c.sudo('apt install nginx -y')
    c.sudo('rm /etc/nginx/sites-enabled/default')
    os.system('scp default 22792191:/home/ubuntu')
    c.sudo('mv /home/ubuntu/default /etc/nginx/sites-enabled/')
    c.sudo('service nginx restart')