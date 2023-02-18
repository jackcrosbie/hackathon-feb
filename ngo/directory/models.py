from django.db import models


class OrgDirectory(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    work = models.CharField(max_length=254, null=False, blank=False)
    location = models.CharField(max_length=254, null=False, blank=False)
    summary = models.CharField(max_length=2000, null=False, blank=False, default="To be added")
    website = models.CharField(max_length=254, null=False, blank=False)
    facebook = models.CharField(max_length=254, null=True, blank=True)
    instagram = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    time = models.TimeField()
    date = models.DateField()
    org = models.ForeignKey(OrgDirectory, null=True, on_delete=models.SET_NULL)
    location = models.CharField(max_length=254, null=False, blank=False)
    summary = models.CharField(max_length=2000, null=False, blank=False)
    website = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
