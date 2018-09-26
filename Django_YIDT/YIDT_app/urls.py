from django.conf.urls import url
from YIDT_app import views

app_name = "YIDT_app"

urlpatterns = [
    #url(r'^$', views.index, name = 'index'),
    url(r'^$',views.user_login, name = "user_login"),
    url(r'^details/$',views.details, name="details"),
    url(r'^registration/$',  views.registration, name = 'registration'),
    url(r'^index/$', views.index, name = 'index'),
    url(r'^add_new_car/$', views.form_name_view, name = "New_Car"),
    url(r'^user_login/$', views.user_login, name = "user_login"),
    url(r'^logout/$',  views.user_logout, name = 'logout'),
]
