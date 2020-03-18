from django.db import models

# Create your models here.


class Message(models.Model):
    sender = models.ForeignKey('auth.User', to_field='username', related_name='sent', on_delete=models.DO_NOTHING)
    receiver = models.ForeignKey('auth.User', to_field='username', related_name='received', on_delete=models.DO_NOTHING)
    message = models.TextField()
    subject = models.CharField(max_length=250)
    creation_date = models.DateField(auto_now_add=True)
    message_status = models.CharField(max_length=6, default='UNREAD')

