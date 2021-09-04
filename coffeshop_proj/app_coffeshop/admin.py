from django.contrib import admin
from .models import Product, Option, Order, OptionValue



class AdminProject(admin.ModelAdmin):
    readonly_fields = []

    def get_readonly_fields(self, request, obj=None):
        if obj:
            if request.user.is_superuser:
                return self.readonly_fields 
            else:
                return self.readonly_fields + ['user', 'product', '_status']
        else:
            return self.readonly_fields 


admin.site.register(Product)
admin.site.register(Option)
admin.site.register(OptionValue)
admin.site.register(Order, AdminProject)
