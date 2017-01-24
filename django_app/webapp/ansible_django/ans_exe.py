#!/usr/bin/env python

import os
from webapp.models import DbClient, DbSystem, DbServer, DbCommand, DbLog

def get_ajax(n):
  n.sort()
  print n
  get_client = DbClient.objects.get(id=1) 
  get_server_ip = DbServer.objects.get(id=int(n[2][1])).server_ip
  get_server_host = DbServer.objects.get(id=int(n[2][1])).server_name
  get_command = DbCommand.objects.get(id=int(n[1][1]))
  # each 'os' is by default run in dir getandfix
  # ansible all -i '<hostname/ip>,' comma is required if 'hosts' file is empty

  # server_ip for vagrant
  if get_server_ip:  
    f = os.popen("ansible all -i '{},' -u root -m shell -a '{}'".format(get_server_ip, get_command))
  # server_host for docker (no IP in DB)
  else:
    f = os.popen("ansible all -i '{},' -u root -m shell -a '{}'".format(get_server_host, get_command))

  print f
  return f.read()
