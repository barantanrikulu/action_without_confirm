from django.db import models
from django.db.models.fields import BooleanField, CharField, DateTimeField
from autoslug import AutoSlugField


class Mission(models.Model):
    title = CharField(max_length=100, null=False,
                      blank=False, default='What to do?')
    created_date = DateTimeField(auto_now_add=True)
    finished = BooleanField(default=False)
    slug = AutoSlugField(populate_from="title", unique=True)

    class Meta:
        db_table = 'Mission'
        verbose_name_plural = 'Missions'
        verbose_name = 'Mission'

    def __str__(self):
        return self.title
