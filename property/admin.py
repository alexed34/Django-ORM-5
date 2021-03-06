from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner', 'id']
    readonly_fields = ['created_at']
    list_display = ('id', 'address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by']


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'complainer')
    search_fields = ['complainer', 'flat']
    list_display = ['complainer', 'flat']


class OwnerAdmin(admin.ModelAdmin):
    search_fields = ['owner', 'id']
    raw_id_fields = ['flats']
    list_display = ('id', 'owner', 'owner_phone_pure')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
