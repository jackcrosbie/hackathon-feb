from django.db import models


class OrgDirectory(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    work = models.CharField(max_length=254, null=False, blank=False)
    location = models.CharField(max_length=254, null=False, blank=False)
    summary = models.CharField(max_length=1000, null=False, blank=False, default="To be added")
    website = models.CharField(max_length=254, null=True, blank=True)
    facebook = models.CharField(max_length=254, null=False, blank=False)
    instagram = models.CharField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.name