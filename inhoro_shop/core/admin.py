from django.contrib import admin
from inhoro_shop.core.models import NaturalPerson, LegalPerson

@admin.register(LegalPerson)
class LegalPersonAdmin(admin.ModelAdmin):
    fields = [
        ('created_at', 'updated_at'),
        ('name', 'nickname'),
        'document',
        ('phone', 'email'),
        ('state_registration', 'municipal_registration')
    ]
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('document', 'name', 'phone', 'email')

@admin.register(NaturalPerson)
class NaturalPersonAdmin(admin.ModelAdmin):
    fields = [
        ('created_at', 'updated_at'),
        ('name', 'nickname'),
        'document',
        ('phone', 'email'),
        ('birthday', 'gender', 'nationality', 'naturalness')
    ]
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('document', 'name', 'phone', 'email')

# Tips
# 1 - Fields are the model data that appeared when creating or changing an instance.
