from . import views
from django.urls import path
from django.urls.conf import include  # Добавить к существующим маршрутов, маршруты нового приложения
from django.conf.urls import url

urlpatterns = [
    path("", views.index, name = "index"),
    url(r'^(?P<category_slug>[-\w]+)/$',
         views.product_list,
         name="product_list_by_category"),
    path("about_us/", views.about),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),
]