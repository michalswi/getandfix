from webapp.models import DbLdap
from django.contrib.auth.backends import RemoteUserBackend
from ldap_stuff.use_ldap import run_main
from django.contrib.auth.models import User

class MyBackend(object):

  def authenticate(self, username=None, password=None):
    if run_main(username, password):
      try:
        #user = DbLdap.objects.get(user_email=username)
        user = User.objects.get(username=username)
      except User.DoesNotExist:
        user = User(username=username)
        user.is_staff = False
        user.is_superuser = False
        user.save()
      return user
    return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


## instead of built-in User use own database
#https://docs.djangoproject.com/en/1.10/topics/auth/customizing/#substituting-a-custom-user-model
#http://stackoverflow.com/questions/1057149/django-users-and-authentication-from-external-source
#https://docs.djangoproject.com/en/1.10/howto/auth-remote-user/
"""
class MyBackend(object):
  def authenticate(self, email=None, password=None):
    #if f(username, password):
    if run_main(email, password):
        # run_main checks first in DbLdap if user is there (based on email) if not will add
        user = DbLdap.objects.get(user_email=email)
        user.is_authenticated = True
        user.save()
        return user
    return None
  def get_user(self, user_id):
    user = DbLdap.objects.get(id=user_id)
    print "user_id:", user_id
    print "user.is_active:", user.is_active
    print "user.user_email:", user.user_email
    if user.is_active:
      return user
    return None
"""
