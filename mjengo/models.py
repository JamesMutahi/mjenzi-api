from django.db import models
from django.contrib.auth.models import User
# from django.contrib.gis.db import models
from model_utils import Choices


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=40, null=False)
    contractor_email = models.CharField(max_length=100, null=False)
    description = models.TextField(default="no description")
    # location = models.PointField()

    def __str__(self):
        return "{} - {}".format(self.name, self.contractor_email)


class Materials(models.Model):
    MATERIALS = Choices('Cement', 'Brick', 'Sand', 'Ballast', 'Metal rods', 'Roofing tiles')
    name = models.CharField(choices=MATERIALS, default=MATERIALS.Cement, max_length=20)
    # quantity
    quantity = models.IntegerField(null=False)
    # project reference
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.name, self.quantity)


class Requests(models.Model):
    MATERIALS = Choices('Cement', 'Brick', 'Sand', 'Ballast', 'Metal rods', 'Roofing tiles')
    name = models.CharField(choices=MATERIALS, default=MATERIALS.Cement, max_length=20)
    quantity = models.IntegerField(null=False)
    photo = models.ImageField(default='projects/default.jpeg', upload_to='projects')
    # location = models.PointField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
