from django.db import models

class Company(models.Model):
    owner = models.ForeignKey(
        "users.User", related_name="owner_company", on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=100, blank=False, null=False)
    
    def __str__(self):
        return f"{self.name} -- {self.owner}"
