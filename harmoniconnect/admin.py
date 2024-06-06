from django.contrib import admin
from .models import CustomUser, ServiceProvider, Client, Service, Booking, Review, Payment, EventDetails
#from django.contrib.auth.admin import UserAdmin
#from .forms import CustomUserCreationForm, CustomUserChangeForm


# Unregister CustomUser if already registered to avoid duplicate registration
try:
    admin.site.unregister(CustomUser)
except admin.sites.NotRegistered:
    pass


#class CustomUserAdmin(UserAdmin):
#    add_form = CustomUserCreationForm
#    form = CustomUserChangeForm
#    model = CustomUser
#    list_display = ['username', 'email', 'user_type', 'is_staff']

#admin.site.register(CustomUser, CustomUserAdmin)


class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = ('user', 'location')
    search_fields = ['user__username', 'location']

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'provider', 'price', 'category')
    list_filter = ('category', 'provider')
    search_fields = ['name', 'provider__user__username']

class BookingAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'booking_date', 'status')
    list_filter = ('status', 'booking_date')
    search_fields = ['client__user__username', 'service__name']

admin.site.register(CustomUser)
admin.site.register(ServiceProvider, ServiceProviderAdmin)
admin.site.register(Client)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Review)
admin.site.register(Payment)
admin.site.register(EventDetails)
