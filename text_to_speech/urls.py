from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'text_to_speech'
urlpatterns = [
    path('', views.TextToSpeechFormView.as_view(), name='text'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
