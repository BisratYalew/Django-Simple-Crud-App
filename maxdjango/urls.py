from django.conf.urls import url, include
from django.contrib import admin
from maxdjango import views
from maxdjango.views import login_redirect
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.login_redirect, name="login_redirect"),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('accounts.urls', namespace='accounts')),
    url(r'^home/', include('home.urls', namespace='home')),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
