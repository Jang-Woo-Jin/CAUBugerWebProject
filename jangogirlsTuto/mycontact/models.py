from django.db import models
from django.utils import timezone
from django.conf import settings
class User(models.Model):
    userId = models.CharField(max_length=200, primary_key=True)
    userPw = models.CharField(max_length=200)
    userName = models.CharField(max_length=200)
    def publish(self):
        self.save()
    def __str__(self):
        return self.userId

class Menu(models.Model):
    menuName = models.CharField(max_length=200, primary_key=True)
    menuCal = models.CharField(max_length=200)
    menuPrice = models.CharField(max_length=200)
    menuImg = models.CharField(max_length=200)
    def publish(self):
        self.save()

    def __str__(self):
        return self.menuName

class Seat(models.Model):
    seatNo = models.IntegerField(primary_key=True)
    isFull = models.BooleanField()
    isReal = models.BooleanField()

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.seatNo)

class Order(models.Model):
    orderId = models.IntegerField(primary_key=True)
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    menuId = models.CharField(max_length=2000)
    isDone = models.BooleanField()
    orderTime = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.orderId)

class Notice(models.Model):
    noticeName = models.CharField(max_length=200)
    noticeContent = models.TextField()
    noticeCount = models.IntegerField()
    noticeTime = models.DateTimeField(default=timezone.now)
    def publish(self):
        self.save()

    def __str__(self):       
        return self.noticeName

    @property
    def update_counter(self):
        self.noticeCount = self.noticeCount + 1
        self.save()