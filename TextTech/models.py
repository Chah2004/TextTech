from django.db import models

# Create your models here.            
class person (models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)


class ContentCreator(models.Model):
	name=models.CharField(max_length=100)
	bio=models.TextField()
	website=models.URLField()
	image=models.ImageField(upload_to='media', null=True, blank=True)
	def __str__(self):
		return self.name

class Blog(models.Model):
	title=models.CharField(max_length=200)
	content=models.TextField()
	pub_date=models.DateTimeField('date published')
	creator=models.ForeignKey(ContentCreator, on_delete=models.CASCADE, related_name='blogs')
	image=models.ImageField(upload_to='media', null=True, blank=True)
	def __str__(self):
		return self.title

class MyReview(models.Model):
	title=models.CharField(max_length=200)
	message=models.TextField()

class Help(models.Model):
	title=models.CharField(max_length=200)
	message=models.TextField()

class ContactDetails(models.Model):
	name=models.CharField(max_length=100)
	number=models.CharField(max_length=10)
	email=models.EmailField()
	message=models.TextField()

class UserRegister(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField()
	password=models.CharField(max_length=200)
	birthday=models.CharField(max_length=20,blank=True,null=True)
	gender=models.CharField(max_length=30,blank=True,null=True)
	state=models.CharField(max_length=30,blank=True,null=True)
	country=models.CharField(max_length=30,blank=True,null=True)
	pincode=models.CharField(max_length=30,blank=True,null=True)
	number=models.CharField(max_length=20,blank=True,null=True)
	age=models.CharField(max_length=30,blank=True,null=True)
	address=models.CharField(max_length=1000,blank=True,null=True)
	image=models.ImageField(upload_to='media',blank=True,null=True)



		