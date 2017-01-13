from django.contrib import admin

# https://docs.djangoproject.com/en/1.10/intro/tutorial02/#make-the-poll-app-modifiable-in-the-admin
# Make the poll app modifiable in the admin
from webapp.models import DbLog
#from .models import *
admin.site.register(DbLog)



