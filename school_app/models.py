from django.db import models

class Admission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)

    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)

    father_name = models.CharField(max_length=100, null=True, blank=True)
    mother_name = models.CharField(max_length=100, null=True, blank=True)

    course = models.CharField(max_length=100)
    previous_school = models.CharField(max_length=200, null=True, blank=True)

    photo = models.ImageField(upload_to='admission/photo/', null=True, blank=True)
    aadhar_card = models.ImageField(upload_to='admission/aadhar/', null=True, blank=True)
    birth_certificate = models.ImageField(upload_to='admission/birth/', null=True, blank=True)

    status = models.CharField(max_length=20, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Student
class Student(models.Model):
    student_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)
    status = models.CharField(max_length=20, default="Approved")

    def __str__(self):
        return self.name


# News
class News(models.Model):
    title = models.CharField(max_length=200)
    is_new = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# Upcoming Events
class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.date})"

#  Notice Board
class Notice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

#  Gallery
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/', null=True, blank=True)

    def __str__(self):
        return f"Image {self.id}"
    
class LiveNews(models.Model):
    text = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text
    
  
class HeroSection(models.Model):
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=200, blank=True)

    slide1 = models.ImageField(upload_to='hero/', blank=True, null=True)
    slide2 = models.ImageField(upload_to='hero/', blank=True, null=True)
    slide3 = models.ImageField(upload_to='hero/', blank=True, null=True)  
    

class About(models.Model):
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    description = models.TextField()

class PrincipalManager(models.Model):
    # Principal
    principal_image = models.ImageField(upload_to='principal/', blank=True, null=True)
    principal_p1 = models.TextField()
    principal_p2 = models.TextField()
    principal_p3 = models.TextField()
    principal_name = models.CharField(max_length=100)

    # Manager
    manager_image = models.ImageField(upload_to='manager/', blank=True, null=True)
    manager_p1 = models.TextField()
    manager_p2 = models.TextField()
    manager_p3 = models.TextField()
    manager_name = models.CharField(max_length=100)
     

class CampusEvent(models.Model):
    image = models.ImageField(upload_to='events/')
    date = models.CharField(max_length=100)
    description = models.TextField()    
   

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')  


class Contact(models.Model):
    map_link = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField() 
    

class ContactInfo(models.Model):
    map_link = models.TextField()
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    address = models.TextField()          


class StudentLife(models.Model):
    image = models.ImageField(upload_to="student_life/")
    title = models.CharField(max_length=200)      