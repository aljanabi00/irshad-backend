from django.db import models


# Create your models here.

class التقييم(models.Model):
    المستوى = models.CharField(max_length=45)

    def __str__(self):
        return self.المستوى


class المتظوعين(models.Model):
    الاسم = models.CharField(max_length=45)
    رقم_الهاتف = models.CharField(max_length=45, null=True, blank=True)
    العنوان = models.CharField(max_length=45, null=True, blank=True)
    التقييم = models.ForeignKey(التقييم, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.الاسم


class النقاط(models.Model):
    اسم_النقطة = models.CharField(max_length=45)
    مسؤول_النقطة = models.ForeignKey(المتظوعين, on_delete=models.CASCADE, null=True, blank=True)
    عدد_المتطوعين = models.IntegerField()
    مكان_النقطة = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return self.اسم_النقطة


class الموقف_اليومي(models.Model):
    النقطة = models.ForeignKey(النقاط, on_delete=models.CASCADE)
    عدد_الاستمارات = models.IntegerField()
    عدد_الباجات = models.IntegerField()
    عدد_المفقودين = models.IntegerField()
    عدد_المتطوعين = models.IntegerField()
    التاريخ = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.النقطة


class المفقودين(models.Model):
    الاسم = models.CharField(max_length=45, null=True, blank=True)
    العمر = models.IntegerField()
    الصلة = models.CharField(max_length=45, null=True, blank=True)
    العنوان = models.CharField(max_length=45, null=True, blank=True)
    رقم_هاتف_المبلغ = models.CharField(max_length=45, null=True, blank=True)
    رقم_هاتف_المستلم = models.CharField(max_length=45, null=True, blank=True)
    الحالة = models.BooleanField(default=True)

    def __str__(self):
        return self.الاسم
