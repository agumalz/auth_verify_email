from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, UserProfile, UserAddress

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profiles'

class UserAddressInline(admin.StackedInline):
    model = UserAddress
    extra = 1

class CustomUserAdmin(BaseUserAdmin):
    inlines = [UserProfileInline, UserAddressInline]

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_email_verified')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    list_display = ('id', 'email', 'is_active', 'is_staff', 'is_email_verified')
    ordering = ('id',)

    def get_fieldsets(self, request, obj=None):
        if obj:  # editing an existing object
            return super().get_fieldsets(request, obj)
        else:  # creating a new object
            return self.add_fieldsets

admin.site.register(CustomUser, CustomUserAdmin)
