from django.db import models
from django.contrib.auth.models import User

from status.models import Status
from category.models import Category

class Publication(models.Model):
    user_creator = models.ForeignKey(User)
    status = models.ForeignKey(Status)
    publish_date = models.DateField(auto_now=True)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    category_id = models.ForeignKey(Category)

    class Meta:
        verbose_name_plural = "Publications"

    def __str__(self):
        return '%s' % (self.title)


