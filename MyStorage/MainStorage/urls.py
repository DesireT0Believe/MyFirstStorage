from django.urls import path

from . views import *

urlpatterns = [
    path('', loginUser, name='home'),
    path('UserStorage', storage, name='storage'),
    path('addfile', addFile, name='add_file'),
    path('delete/<int:id>/', delFile, name='delete_file'),
    path('register/', registerUser, name='register'),
    path('logout', logout, name='logout')

]