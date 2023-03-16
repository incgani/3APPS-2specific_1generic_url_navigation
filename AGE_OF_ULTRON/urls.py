from django.urls import path
from AGE_OF_ULTRON.views import *
app_name='AGE_OF_ULTRON'
urlpatterns=[
    path('age_of_ultron/',age_of_ultron,name='age_of_ultron'),
]