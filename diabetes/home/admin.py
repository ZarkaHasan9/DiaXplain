from django.contrib import admin
from .models import Prediction, Report, Feedback
# Register your models here.
admin.site.register(Prediction)
admin.site.register(Report)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('submitted_at',)

admin.site.register(Feedback, FeedbackAdmin)
