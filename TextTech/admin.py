from django.contrib import admin
from TextTech.models import person
from TextTech.models import Blog
from TextTech.models import ContentCreator
from TextTech.models import MyReview
from TextTech.models import Help
from TextTech.models import ContactDetails
from TextTech.models import UserRegister




# Register your models here.
admin.site.register(person)
admin.site.register(Blog)
admin.site.register(ContentCreator)
admin.site.register(MyReview)
admin.site.register(Help)
admin.site.register(ContactDetails)
admin.site.register(UserRegister)


