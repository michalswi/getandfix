from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime

# https://docs.djangoproject.com/en/1.10/topics/db/models/
# https://docs.djangoproject.com/en/1.9/ref/models/fields/

class DbClient(models.Model):
	id = models.AutoField(primary_key=True)
	client_name = models.CharField(max_length=30, null=False)	# CharField -> varchar
	def __str__(self):
		return self.client_name
		
class DbSystem(models.Model):
	id = models.AutoField(primary_key=True)
	os_platform = models.CharField(max_length=16, null=False)

	def __str__(self):
		return self.os_platform
		
# Many-to-one relationships
# https://docs.djangoproject.com/en/1.10/topics/db/models/#many-to-one-relationships
class DbServer(models.Model):
	id = models.AutoField(primary_key=True)
	
	id_client_name = models.ForeignKey(DbClient)		# one client -> many servers
	id_os_platform = models.ForeignKey(DbSystem)
	
	server_name = models.CharField(max_length=30, null=False)
	
	def __str__(self):
		return self.server_name

#
class DbCommand(models.Model):
	id = models.AutoField(primary_key=True)
	
	cmd = models.CharField(max_length=60, null=False)
	id_os_platform = models.ForeignKey(DbSystem)
	
	def __str__(self):
		return self.cmd

# no relation
class DbLog(models.Model):
	id = models.AutoField(primary_key=True)
	
	username = models.CharField(max_length=30, null=False)
	
	client_name = models.CharField(max_length=30, null=False)
	server_name = models.CharField(max_length=30, null=False)
		
	cmd = models.CharField(max_length=60, null=False)
	# json catched from ansible
	cmd_output = models.TextField()
	run_time = models.DateTimeField(default = timezone.now)
	
	# def ?

# more about models
#http://djangobook.com/advanced-models/
#https://www.tutorialspoint.com/django/django_models.htm
#https://tutorial.djangogirls.org/pl/django_models/

