from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.TextField(max_length=60,null = True, blank = True)
    description=models.TextField(max_length=200000,null = True, blank = True, default = '')
    industry=models.TextField(max_length=20000,null = True, blank = True, default = '')
    phone=models.TextField(max_length=20000,null = True, blank = True, default = '999-999-999')
    
    def __str__(self):
        return str(self.name)

class Contact(models.Model):
    first_name = models.TextField(max_length=60,null = True, blank = True)
    last_name=models.TextField(max_length=200000,null = True, blank = True, default = '')
    fax=models.TextField(max_length=20000,null = True, blank = True, default = '')
    phone=models.TextField(max_length=20000,null = True, blank = True, default = '999-999-999')
    email = models.TextField(verbose_name="email", max_length=60,null=True,blank=True)
    
    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)

class User(models.Model):
    username = models.CharField(verbose_name="username", max_length=60, unique=True,null=True,blank=True)
    email = models.TextField(verbose_name="email", max_length=60,null=True,blank=True)
    name = models.TextField(verbose_name="name", max_length=60, blank = True, null = True)
    phone = models.TextField(max_length=200,null = True, blank = True)
    country=models.TextField(max_length=20000,null = True, blank = True, default = '')

    def __str__(self):
        return str(self.username)

