#!/usr/bin/env python

import os
from webapp.models import DbClient, DbSystem, DbServer, DbCommand, DbLog

def get_ajax(n):
  n.sort()
  print n
  n1 = DbClient.objects.get(id=1) 
  n2 = DbServer.objects.get(id=int(n[2][1])).server_ip
  n3 = DbCommand.objects.get(id=int(n[1][1]))
  # each 'os' is by default run in dir getandfix
  # ansible all -i '<hostname/ip>,' comma is required if 'hosts' file is empty
  f = os.popen("ansible all -i '{},' -u root -m shell -a '{}'".format(n2, n3))
  print f
  return f.read()
