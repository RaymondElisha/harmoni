from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from harmoniconnect import views
from harmoniconnect.views import ServiceViewSet, ServiceProviderViewSet, BookingViewSet, ReviewViewSet, SignUpView, ServiceSearchViewSet,home, register,login,review,service,search,client_dashboard,service_provider_dashboard,payment, post_service
from django.contrib.auth import views as auth_views


router = routers.DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'serviceproviders', ServiceProviderViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'services/search', ServiceSearchViewSet, basename='service-search')

urlpatterns = [
    path("admin/", admin.site.urls),
    #path('api/', include(router.urls)),  # Dedicated path for all API endpoints
    #path('', views.home, name='home'),
    #path('about/', views.about, name='about'),
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('signup/', SignUpView.as_view(), name='signup'),
    # The lines below for service_list and service_detail are not needed because router takes care of it
    # path('services/', service_list, name='service-list'),
    # path('services/<int:pk>/', service_detail, name='service-detail'),
    path('book_service/<int:service_id>/', views.book_service, name='book_service'),
    path('', home, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', login, name='login'),
    path('review/', review, name='review'),
    path('service/', service, name='service'),
    #path('login/', CustomLoginView.as_view(), name='login'),
    path('search/', search, name='search'),
    path('client-dashboard/', client_dashboard, name='client_dashboard'),
    path('service-provider-dashboard/', service_provider_dashboard, name='service_provider_dashboard'),
    path('payment/', payment, name='payment'),
    path('api/', include(router.urls)),
    path('post_service/', views.post_service, name='post_service'),
    path('process_payment/', views.process_payment, name='process_payment'),
]

# Handling static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Optional: Add custom error handling views
# handler404 = 'your_app.views.custom_404_view'
# handler500 = 'your_app.views.custom_500_view'
