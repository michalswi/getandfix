FROM centos:7
# to install nginx you need 'epel-release'
RUN yum install -y epel-release
RUN yum install -y nginx

#RUN rm -rf /etc/nginx/nginx.conf
ADD nginx.conf /etc/nginx/nginx.conf
ADD ./ssl /ssl
ADD ./static /static
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
# CMD/ENTRYPOINT
CMD ["nginx"]
EXPOSE 5000

