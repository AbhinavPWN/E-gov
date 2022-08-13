from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import card



CHOICES=[
    ('1', 'Chitwan'), ('2', 'Kathmandu'),
       ('3', 'Bhaktapur'), ('4', 'Lalitpur'),]
gen = [('1', 'Male'), ('2', 'Female'),
       ('3', 'Others'), ]
stat = [('1', 'Married'), ('2', 'Single'),
        ('3', 'Divorce'), ]
Edu_level = [('1', 'Uneducated'), ('2', 'Slc'), ('3', 'Plus 2'),
             ('4', 'Bacehlors'), ('5', 'Masters'), ('6', 'PHDs'), ]
prof = [('1', 'Others'), ('2', 'Service'), ('3', 'Doctor'), ('4', 'Framer'),
        ('5', 'Teacher'), ('6', 'Social Worker'), ('7', 'Lawyer'), ('8', 'Businessman')]
CasteChoice = [('1', 'Others'), ('2', 'Chettri'), ('3', 'Brahmin'), ('4', 'Newar'),
               ('5', 'Thakuri')]
Reli = [('1', 'Others'), ('2', 'Hindu'), ('3', 'Bouddha'), ('4', 'Islam'),
        ('5', 'Christian')]
# Create your models here.
class FilesAdmin(models.Model):
    adminupload = models.FileField(upload_to='uploads/')
    title= models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = 'Files Uploads'
        
    def __str__(self):
        return self.title

class Idcard(models.Model):
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    birthplace = models.CharField(choices=CHOICES, max_length=50)
    citizenship_no = models.IntegerField()
    issue_zone = models.CharField( max_length=50)
    gender = models.CharField(max_length=50)
    marital_status = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    caste = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = 'Id Cards'
        
    def __str__(self):
        return self.firstname

class Gallery(models.Model):
        title = models.CharField(max_length=150)
        image =models.ImageField(upload_to='uploads', null=True, blank=True )
        
        class Meta:
                verbose_name_plural='Galleries'
                
        def __str__(self):
            return self.title
        