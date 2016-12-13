#!/usr/bin/env python

import os
from webapp.models import DbClient, DbSystem, DbServer, DbCommand, DbLog

def get_ajax(n):
  n.sort()
  print n
  n1 = DbClient.objects.get(id=1) 
  n2 = DbServer.objects.get(id=int(n[2][1]))
  print n2
  n3 = DbCommand.objects.get(id=int(n[1][1]))
  print n3
  f = os.popen("ansible -i django_app/webapp/ansible_django/hosts {} -k -u root -m shell -a '{}'".format(n2, n3))
  return f.read()
