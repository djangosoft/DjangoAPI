from django.db import models


class Member(models.Model):
    ok = models.BooleanField(primary_key=True)


class Emp(models.Model):
    members = models.ForeignKey(Member, null=True, related_name='members', on_delete=models.CASCADE)
    id = models.CharField(max_length=100, primary_key=True)
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=100)


class Active(models.Model):
    emp = models.ForeignKey(Emp, related_name='activity_status', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
