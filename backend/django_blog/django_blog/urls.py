from django.contrib import admin
from django.urls import include, path
from . import views
# For production, do not store static files in Django.
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', article_views.article_list, name="home"),
  path('about/', views.about),
  path('articles/', include('articles.urls')),
  path('accounts/', include('accounts.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)