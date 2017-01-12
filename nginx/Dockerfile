FROM centos:7
# to install nginx you need 'epel-release'
RUN yum install -y epel-release
RUN yum install -y nginx

#RUN rm -rf /etc/nginx/nginx.conf
ADD nginx.conf /etc/nginx/nginx.conf
ADD ./ssl /ssl
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
CMD ["nginx"]
EXPOSE 5000

