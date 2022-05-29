from django.urls import path
from services import views

app_name = 'services'

urlpatterns=[
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('service/',views.service,name='service'),
    path('contact/',views.contact,name='contact'),
    path('blog-details/',views.blog_details,name='blog_details'),
]
