# Generated by Django 3.2.9 on 2021-11-28 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0002_company_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_team', to='company.company')),
                ('members', models.ManyToManyField(blank=True, null=True, related_name='members_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]