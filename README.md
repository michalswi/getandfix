# getandfix

[in progress]

Getandfix is a web app to verify (in future could be extended to fix) specific tasks like check CPU, memory, filesystems usage etc. for specific customer and server. App use LDAP to authenticate user.

### How it works? 
Please read all before run app.
#### First steps
Main application (django_app) you can find [here](https://github.com/michalswi/getandfix/tree/master/django_app)

First you should install all required packages: TODO

Next step is to create database.
 
There are two ways:
  1. Create DB and build from scratch using python makemigrations/migrate.
  2. Use myproject.sql (password: password).

After that you can run django app:
```bash
$ python django_app/manage.py runserver
```

[Here](https://github.com/michalswi/getandfix/tree/master/django_app/webapp/ansible_django/os) you can find vagrant machine for tests. Just run `vagrant up` in this dir. VM is already placed in DB.

#### Authentication
You don't have to create/request any account. I use [here](https://github.com/michalswi/ldap_stuff) LDAP to verify user.

Before run you have to place script [here](https://github.com/michalswi/getandfix/tree/master/django_app/webapp/ldap_stuff) and add to script:
```text
LDAP_SERVER = 'example.ldap.com'
LDAP_BASEDN = 'ou=example,o=ldap.com'
```

#### Docker
App is ready to be used by docker. All files you can find [here](https://github.com/michalswi/getandfix/tree/master/docker). 

Of course all files like ssh_keys, ssl_certs are only for tests purposes (remember to change them). 

All you have to do is:
  - copy main django_app/ to web/ directory
  - create db/mysql/ directory

After copied you don't have to change anything in web/django_app/ directory because all necessary files are going to be changed.

To better understand what's going on here please read docker-compose.yml and Dockerfiles for each container.

Move to docker/ directory and run:
```bash
$ docker-compose build
$ docker-compose up -d
```
Finally you will get sth like that:
```bash
$ docker-compose ps
  Name                Command             State           Ports          
------------------------------------------------------------------------
ans_host1   /usr/sbin/sshd -D             Up      22/tcp                 
ans_host2   /usr/sbin/sshd -D             Up      22/tcp                 
mariadb     docker-entrypoint.sh mysqld   Up      3306/tcp               
nginx       nginx                         Up      0.0.0.0:8000->5000/tcp 
web         ./start_gun.sh                Up      8080/tcp
```
On your host machine open web browser, paste https://0.0.0.0:8000/ and that's all.

If you want to use it somewhere else, just zip docker/.

For tests you have two containers(already added to DB) ans_host1/2 where as you can see above sshd service is active.

#### Vagrant
Vagrant part you can find [here](https://github.com/michalswi/getandfix/tree/master/vagrant). Vagrantfile for dbserver is ready but for webserver not yet.

#### Authors:

*  [Michal Swierczewski](https://github.com/michalswi)
*  [Damian Lubawy](https://github.com/pag-r)

