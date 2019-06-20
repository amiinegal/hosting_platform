from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url('^$',views.home,name = 'homePage'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^edit/profile/$',views.edit_profile,name='edit_profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
