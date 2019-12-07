from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import home_page, about_page, contact_page
from products.views import ProductList, ProductDetail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('about-us/', about_page, name='about'),
    path('contact-us/', contact_page, name='contact'),
    path('products/<category>/<slug>/', ProductList.as_view(), name='list'),
    path('item/<category>/<slug>/<sku>/', ProductDetail.as_view(), name='detail'),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)