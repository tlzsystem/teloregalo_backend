from django.db import models

class Status(models.Model):
    status_name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Status"

    def __str__(self):
        return '%s' % (self.status_name)
