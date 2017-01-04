FROM centos:7

RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python get-pip.py
RUN pip install gunicorn

RUN yum install -y python-setuptools \
python-ldap.x86_64 \
epel-release

RUN pip install django \
django_extensions

RUN yum install -y openldap.x86_64 \
openldap-clients.x86_64

RUN yum install -y ansible

RUN yum install -y bind-utils \
iproute

RUN yum install -y MySQL-python \
mariadb-server mariadb

# docker build -t docker_django . , the last . tells the docker client to send the current directory
# COPY use the same directory where Dockerfile is located because of dot* it means you cannot specify the full path to django_app
#COPY /home/vagrant/django_app /django_app    <-- wont work
COPY ./django_app /django_app
CMD ["django_app/start_gun.sh"]

# missing nginx stuff
