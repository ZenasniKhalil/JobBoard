from django.db import models

index = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

class JobModel(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    vacancy = models.IntegerField(default=1)
    job_type = models.CharField(max_length=50,choices=index)
    salary = models.IntegerField(default=0)
    description = models.TextField(max_length=1000)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Requirements(models.Model):
    require = models.CharField(max_length=100)
    job_title = models.ForeignKey(JobModel, on_delete=models.CASCADE)
    def __str__(self):
        return self.require[:8]
    




