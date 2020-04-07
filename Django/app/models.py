from django.db import models
from django.utils import timezone
import datetime


#interect with database through shell
#python3 manage.py shell

#CREATE NEW DATABASE IF/WHEN WE START OVER
#terminal:

#rm -f tmp.db db.sqlite3
#rm -r app/migrations
#python manage.py makemigrations app
#python manage.py migrate
class Person(models.Model):
    #column name=datatype

    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    isemployee = models.BooleanField(default=False)
    startemploymentweeks = models.IntegerField()
    endemploymentweeks = models.IntegerField()
    matches =models.ForeignKey('Person', on_delete=models.CASCADE, related_name='matched')
    messages=models.TextField()
    #profile_pic=
    Jobtype=models.TextField()
    swipesinterestedinme=models.ForeignKey('Person',
    on_delete=models.CASCADE, related_name='me')
    swipesiminterestedin=models.ForeignKey('Person', on_delete=models.CASCADE, related_name='them')
    availabilemonday=models.BooleanField(default=False)
    availabiletuesday=models.BooleanField(default=False)
    availabilewednesay=models.BooleanField(default=False)
    availabilethursday=models.BooleanField(default=False)
    availabilefriday=models.BooleanField(default=False)
    availabilesaturday=models.BooleanField(default=False)
    availabilesunday=models.BooleanField(default=False)
    #resume=
    #coverpage=

    #change value displayed for Queries
    def __str__(self):
        return self.email
