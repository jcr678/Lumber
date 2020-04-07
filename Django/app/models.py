from django.db import models
from django.utils import timezone
import datetime
# Create your models here. LATER THIS IS THE DATABASE
class Person(models.Model):
    #column name=datatype
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    isemployee = models.BooleanField(default=False)
    startemploymentweeks = models.IntegerField()
    endemploymentweeks = models.IntegerField()
    matches =
    messages=models.TextField()
    profile_pic=
    Jobtype=models.TextField()
    swipesinterestedinme=models.ForeignKey(Person, on_delete=models.CASCADE)
    swipesiminterestedin=models.ForeignKey(Person, on_delete=models.CASCADE)
    availabilemonday=models.BooleanField(default=False)
    availabiletuesday=models.BooleanField(default=False)
    availabilewednesay=models.BooleanField(default=False)
    availabilethursday=models.BooleanField(default=False)
    availabilefriday=models.BooleanField(default=False)
    availabilesaturday=models.BooleanField(default=False)
    availabilesunday=models.BooleanField(default=False)
    resume=
    coverpage=
    introduction=models.TextField()
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    #change value displayed for Queries
    def __str__(self):
        return self.email
