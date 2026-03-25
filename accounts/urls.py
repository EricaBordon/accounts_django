from django.urls import path
from .views import login_view, home_view, logout_view

urlpatterns = [
    path('', login_view, name='login'),       # / → login
    path('home/', home_view, name='home'),    # /home/
    path('logout/', logout_view, name='logout'),  # /logout/
]