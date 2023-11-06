from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import ShowImage,ShowImageDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ShowImage.as_view(),name='images'),
    path('view-details/<int:pk>',ShowImageDetails.as_view(),name='details')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
