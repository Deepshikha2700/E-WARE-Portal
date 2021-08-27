# from django.contrib import admin
from django.urls import path,include
from django.conf.urls import include, url


from login import views

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
# app_name="eware"

urlpatterns = [
 path('', views.log_in, name='login'),
    # path('login/', include('login.urls'))
     path('home', views.home, name='home'),
      path('about/', views.about, name='about'),
      path('contact/', views.contact, name='contact'),
      path('profile/', views.profile, name='profile'),
      path('form/', views.form, name='form'), 
      path('account_recovery', views.account_recovery, name='account_recovery'), 
      path('amazon', views.amazon, name='amazon'), 
      path('company_ann', views.company_ann, name='company_ann'), 

      path('consumer_shopping', views.consumer_shopping, name='consumer_shopping'), 
      path('covid', views.covid, name='covid'), 
      path('gmail', views.gmail, name='gmail'),
      path('D_D',views.D_D,name='D_D') ,

      path('health', views.health, name='health'), 
      path('office_mailer', views.office_mailer, name='office_mailer'), 
      path('socialpassword', views.socialpassword, name='socialpassword'), 
      path('signup', views.handleSignUp, name="handleSignUp"),
      path('login', views.handeLogin, name="handleLogin"),
      path('logout', views.handleLogout, name="handleLogout"),
      path('mail_template',views.mail_template,name="mail_template"),
      path('analyze',views.analyze,name="analyze"),
      path('index',views.index,name="index"),
      path('reports',views.reports,name="reports"),
      path('sendemail',views.send_email,name="sendemail"),



      
      # path('template', views.insertTemplate, name="handleLogin"),
      url(r'^amazon', TemplateView.as_view(template_name="amazon.html"),
                   name='amazon'),
      # url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),



       path('about/home', views.aboutHome, name='about_home'),
          ]

 
# if settings.DEBUG:
#    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
 


