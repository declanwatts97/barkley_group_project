from django.contrib import admin
from .models import MeetingRequest
# Register your models here.

@admin.register(MeetingRequest)
class MeetingRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'meeting_time', 'created_at')
    list_filter = ('service', 'new_client')
    search_fields = ('name', 'comment')