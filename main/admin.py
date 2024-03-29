from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Supplier
from .models import Category
from .models import Payment
from .models import Cart
from .models import Shipper, UserProfile, OrderDetails, Orders, Product,  Address_details
from django.contrib.auth.models import Group
from .forms import UserAdminCreationForm, UserAdminChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'admin')
    list_filter = ('admin','staff','active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin','staff','active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)



# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)

#admin.site.register(User)
admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(Payment)
admin.site.register(Shipper)
admin.site.register(UserProfile)
admin.site.register(Orders)
admin.site.register(Product)
admin.site.register(OrderDetails)
admin.site.register(Cart)
admin.site.register(Address_details)