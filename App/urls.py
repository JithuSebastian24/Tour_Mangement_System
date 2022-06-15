from django import views
from django.urls import path
from App import views
app_name='App'

urlpatterns = [
    path('index/',views.index,name='index'),
    path('adventure/<type>',views.packadv,name='packadv'),
    path('holyday/<type>',views.packholy,name='packholy'),
    path('devotional/<type>',views.packdev,name='packdev'),
    path('honeymoon/<type>',views.packhoney,name='packhoney'),
    # path('bookform/',views.bookform,name='bookform'),
    path('bookpack/<int:id>',views.bookpack,name='bookpack'),
    path('confirm/',views.confirm,name='confirm'),
    path('bookingconfirmed/',views.booksave,name='booksave'),
    path('contact/',views.msg,name='msg'),
    path('rating/',views.rate,name='rate'),

]

