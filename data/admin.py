from django.contrib import admin
from .models import *


# Register your models here.


class admin1(admin.ModelAdmin):
    list_display = ('الاسم', 'رقم_الهاتف', 'العنوان', 'التقييم')
    list_filter = ('التقييم',)


class admin2(admin.ModelAdmin):
    list_display = ('الاسم', 'العمر', 'الصلة', 'العنوان', 'رقم_هاتف_المبلغ', 'رقم_هاتف_المستلم', 'الحالة')
    list_filter = ('الحالة',)


class admin3(admin.ModelAdmin):
    list_display = ('اسم_النقطة', 'مسؤول_النقطة', 'عدد_المتطوعين', 'مكان_النقطة')


class admin4(admin.ModelAdmin):
    list_display = ('النقطة', 'عدد_الاستمارات', 'عدد_الباجات', 'عدد_المفقودين', 'عدد_المتطوعين', 'التاريخ')


admin.site.register(المتظوعين, admin1)
admin.site.register(المفقودين, admin2)
admin.site.register(الموقف_اليومي, admin4)
admin.site.register(النقاط, admin3)
admin.site.register(التقييم)
