from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.view,name='view'),
    path('view/',views.view,name='view'),
    path('create/',views.create,name='create'),
    path('update/', views.update, name='update'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('importfile/', views.importfile, name='importfile'),
    path('download/<str:id>/', views.download_file, name='download_file')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)