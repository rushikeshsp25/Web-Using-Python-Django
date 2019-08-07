from django.urls import path
from . import views

urlpatterns = [
    path('feed/',views.feed),
    path('post/<int:year>/',views.year_archive),
    path('post/<int:year>/<int:month>',views.month_archive),
    path('post/<int:year>/<int:month>/<int:pk>/',views.post_detail),
]