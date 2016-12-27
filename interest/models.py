from django.db import models
from django.contrib.auth.models import User
from publication.models import Publication



class Interest(models.Model):
    publication_id = models.ForeignKey(Publication)
    user_interest = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = "Interesados"

    def __str__(self):
        return '%s' % (self.id)

