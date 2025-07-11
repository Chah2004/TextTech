"""
URL configuration for TextTool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TextTech import views

from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import path





urlpatterns = [
    path("admin/", admin.site.urls),
    path('navbar',views.navbar),
    path('footer',views.footer),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('register2',views.register2,name='register2'),

    path('forgot',views.forgot,name='forgot'),
    path('contact',views.contact,name='contact'),
    path('',views.index,name='index'),
    path('base',views.base),
    path('allblog',views.allblog,name='allblog'),
    path('detail_blog/<int:id>',views.detail_blog,name='detail_blog'),
    path('allcontentcreator',views.allcontentcreator,name='allcontentcreator'),
    path('about_us',views.about_us,name='about_us'),

    path('dashboard',views.dashboard,name='dashboard'),
    path('review',views.review,name='review'),
    path('sidebar',views.sidebar),
    path('changepw',views.changepw,name='changepw'),
    path('help',views.help,name='help'),
    path('userprofil',views.userprofil,name='userprofil'),
    path('editprofile',views.editprofile,name='editprofile'),
    path('logout',views.logout,name='logout'),
    path('livenews',views.livenews,name='livenews'),

    path('text_to_speech',views.text_to_speech,name='text_to_speech'),
    # path('tts_output',views.tts_output,name='tts_output'),
    path('tts_output2',views.tts_output2,name='tts_output2'),



    path('speech_to_text',views.speech_to_text,name='speech_to_text'),
    path('word_cloud',views.word_cloud,name='word_cloud'),
    path('sentiment_analysis',views.sentiment_analysis,name='sentiment_analysis'),
    path('language_detection',views.language_detection,name='language_detection'),
    path('language_converter',views.language_converter,name='language_converter'),
    path('text_to_pdf',views.text_to_pdf,name='text_to_pdf'),
    path('text_summarization',views.text_summarization,name='text_summarization'),
    path('count',views.count,name='count'),
    path('transform_text',views.transform_text,name='transform_text'),
    path('text_to_qr',views.text_to_qr,name='text_to_qr'),
    path('ttqr_output',views.ttqr_output,name='ttqr_output'),
    path('linguistic_analysis',views.linguistic_analysis,name='linguistic_analysis'),
    path('spelling_checker',views.spelling_checker,name='spelling_checker'),
    path('pdf_to_text',views.pdf_to_text,name='pdf_to_text'),
    path('ptt_output',views.ptt_output,name='ptt_output'),
    path('pdf_to_audio',views.pdf_to_audio,name='pdf_to_audio'),
    path('pta_output',views.pta_output,name='pta_output'),
    path('word_transformation',views.word_transformation,name='word_transformation'),
    

]



   






urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)