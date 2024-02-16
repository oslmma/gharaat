from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Student(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=128, null=True, blank=True)
    score_all = models.IntegerField(default=0)
    pic = models.ImageField(upload_to='media/avatar', blank=True, null=True)

    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} Score: {self.score_all}'
    
    def get_absolute_url(self):
        return reverse("profile", kwargs={"pk": self.pk})
    
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    User.add_to_class("__str__", get_full_name)
    
class Score(models.Model):
    MONTH_CHOICES = (
            ("farvardin", "فروردین"),
            ("ordibehesht", "اردیبهشت"),
            ("khordad", "خرداد"),
            ("tir", "تیر"),
            ("mordad", "مرداد"),
            ("shahrivar", "شهریور"),
            ("mehr", "مهر"),
            ("aban", "آبان"),
            ("azar", "آذر"),
            ("dey", "دی"),
            ("bahman", "بهمن"),
            ("esfand", "اسفند"),
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.CharField(max_length=128, choices=MONTH_CHOICES)
    say_pray = models.IntegerField(default=0)
    setad_namaz = models.IntegerField(default=0)
    payegah = models.IntegerField(default=0)
    gharaat = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name} {self.month}||| نماز جماعت: {self.say_pray} ||||احیای نماز: {self.setad_namaz} ||||پایگاه: {self.payegah} قرائت: {self.gharaat}'

class Score_monthly(models.Model):
    MONTH_CHOICES = (
        ("farvardin", "فروردین"),
        ("ordibehesht", "اردیبهشت"),
        ("khordad", "خرداد"),
        ("tir", "تیر"),
        ("mordad", "مرداد"),
        ("shahrivar", "شهریور"),
        ("mehr", "مهر"),
        ("aban", "آبان"),
        ("azar", "آذر"),
        ("dey", "دی"),
        ("bahman", "بهمن"),
        ("esfand", "اسفند"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.CharField(max_length=128, choices=MONTH_CHOICES)
    score = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}  ||||| {self.month} ||  امتیاز: {self.score}'


class Jozve(models.Model):
    title = models.CharField(max_length=64) 
    description = models.CharField(max_length=128)
    jozve = models.FileField(upload_to='media/jozve')

    def __str__(self) -> str:
        return f'{self.title}'
