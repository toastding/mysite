from django.contrib import admin
from read_statistic.models import ReadNum, ReadDetail


@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('read_num', 'content_object')


@admin.register(ReadDetail)
class ReadDetaAdmin(admin.ModelAdmin):
    list_display = ('date', 'read_num', 'content_object')





