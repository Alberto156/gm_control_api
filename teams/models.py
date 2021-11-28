from django.db import models

class Team(models.Model):
    name = models.CharField("Name", max_length=100)
    company = models.ForeignKey(
        "company.Company", related_name="company_team", on_delete=models.CASCADE)
    members = models.ManyToManyField(
        "users.User", blank=True, related_name="members_users")
    
    status = models.BooleanField("Status" , default=False)

    def __str__(self):
        return f"{self.name} - {self.company}"
