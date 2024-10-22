from django.db import models

# Create your models here.
class About(models.Model):
    image =True # models.ImageField(upload_to="images")
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    resume = null=True #models.FileField(upload_to='files')
    experience = models.IntegerField()
    project_success = models.IntegerField()
    rate = models.IntegerField()

    def __str__(self) -> str:
        return self.name                   # called it as string representation method. 
                                          #it will return the objects in string format to display in a human readable format
    