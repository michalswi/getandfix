FROM centos:7

RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python get-pip.py
RUN pip install gunicorn

RUN yum install -y python-setuptools \
python-ldap.x86_64

# to install nginx you need 'epel-release'
RUN yum install -y epel-release \
nginx

RUN pip install django \
django_extensions

RUN yum install -y openldap.x86_64 \
openldap-clients.x86_64

RUN yum install -y ansible

RUN yum install -y bind-utils \
iproute \
net-tools

RUN yum install -y MySQL-python \
mariadb-server mariadb

RUN echo "daemon off;" >> /etc/nginx/nginx.conf

#EXPOSE 80
#EXPOSE 443
#CMD ["nginx"]

RUN rm -rf /etc/nginx/nginx.conf

ADD nginx.conf /etc/nginx/nginx.conf
ADD django_app /django_app

WORKDIR /django_app

EXPOSE 5000
CMD ["nginx"]
CMD ["./start_gun.sh"]



