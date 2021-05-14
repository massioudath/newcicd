from django.db import models

# Create your models here.
class InternetUsers(models.Model):
    nbre_users = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'internet_users'
