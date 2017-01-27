FROM ubuntu:16.04

RUN apt-get update && apt-get install -y openssh-server

# if UBUNTU without python-minimal (python2) ansible throw MODULE FAILURE
RUN apt-get install -y python-minimal

RUN mkdir /var/run/sshd
RUN echo 'root:dupa' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

RUN mkdir /root/.ssh
ADD test_rsa* /root/.ssh/

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
