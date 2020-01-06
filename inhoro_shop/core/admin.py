from django.contrib import admin
from inhoro_shop.core.models import NaturalPerson, LegalPerson

@admin.register(LegalPerson)
class LegalPersonAdmin(admin.ModelAdmin):
    fields = [
        ('created_at', 'modified_at'),
        ('name', 'nickname'),
        'document',
        ('phone', 'email'),
        ('state_registration', 'municipal_registration')
    ]
    readonly_fields = ('created_at', 'modified_at')
    list_display = ('document', 'name', 'phone', 'email')
