FROM centos:7

RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python get-pip.py
RUN pip install gunicorn
RUN yum install -y python-setuptools python-ldap.x86_64
# to install nginx/ansible you need 'epel-release'
RUN yum install -y epel-release 
RUN yum install -y ansible
RUN pip install django django_extensions
RUN yum install -y openldap.x86_64 openldap-clients.x86_64
RUN yum install -y bind-utils iproute net-tools
RUN yum install -y MySQL-python mariadb-server mariadb

RUN yum install -y openssh
ADD id_rsa* /root/.ssh/

ADD django_app /django_app
ADD settings.py /django_app/django_app/settings.py
ADD start_gun.sh /django_app/start_gun.sh

WORKDIR /django_app

#by default ansible use /etc/ansible (you can verify that running ansible --version)
#export ANSIBLE_CONFIG=/django_app/webapp/ansible_django/ansible.cfg
ENV ANSIBLE_CONFIG /django_app/webapp/ansible_django/ansible.cfg
