from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# https://docs.djangoproject.com/en/1.10/topics/db/models/
# https://docs.djangoproject.com/en/1.9/ref/models/fields/


class DbMain(models.Model):
	client_name = models.CharField(max_length=30)
	server_name = models.CharField(max_length=30)

class DbCommands(models.Model):
	cmd = models.CharField(max_length=48)
	#cmd_date = models.DateField()
	cmd_date = models.DateTimeField(default = timezone.now)
	cmd_output = models.TextField()					# json catched from ansible
	
class Execute(models.Model):
	main = models.ManyToManyField(DbMain)
	comm = models.ManyToManyField(DbCommands)

class DbLogs(models.Model):
	# get client:server
	# date when executed
	# which command
	# get output
	main_log = models.ForeignKey(DbMain)
	commands_log = models.ForeignKey(DbCommands)
	exe = models.ForeignKey(Execute)


			
"""
# Many-to-one relationships
# https://docs.djangoproject.com/en/1.10/topics/db/examples/many_to_one/
# one client -> many servers
# DbClient -> DbServer

class DbClient(models.Model):
    id = models.AutoField(primary_key=True)			# overwrite default one	
    client_name = models.CharField(max_length=48)
    
    def __unicode__(self):
		return self.client_name
		
# user will select client and get a list of servers related to specific client    
class DbServer(models.Model):
	id = models.AutoField(primary_key=True)
	host = models.ForeignKey(DbClient)
	server_name = models.CharField(max_length=48)
	
	def __unicode__(self):
		return self.server_name

# One-to-one relationship
# https://docs.djangoproject.com/en/1.10/topics/db/examples/one_to_one/
# one server -> run specific command

# DbCommands will use server_name to execute command	
class DbCommands(models.Model):
	id = models.AutoField(primary_key=True)
	scan = models.OneToOneField(DbServer)
	cmd = models.CharField(max_length=48)
	cmd_date = models.DateField()
	cmd_output = models.TextField()					# json catched from ansible
	
# One-to-one relationship
class DbLogs(models.Model):
	# get client:server
	# date when executed
	# which command
	# get output
	client_log = models.ForeignKey(DbClient)
	server_log = models.ForeignKey(DbServer)
	server_info_log = models.ForeignKey(DbCommands)

class Personal(models.Model):
	pass
	
# prepare procedure base on command output	
class AnalyzeCommOut(models.Model):
	pass
"""
