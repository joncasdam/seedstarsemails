# -*- encoding: utf-8 -*-
from django.db import models


class Person(models.Model):
    name = models.CharField(u'Name', max_length=200, null=False, blank=False)
    email = models.EmailField(u'E-mail')

    class Meta:
        verbose_name = u'Person'
        verbose_name_plural = u'People'

    def __unicode__(self):
        return '%s' % self.name

    def to_dict(self):
        return {'id': self.id,
                'name': self.name,
                'email': self.email}

    @classmethod
    def get_all_people(cls):
        return [p.to_dict() for p in cls.objects.all()]
