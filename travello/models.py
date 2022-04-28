from django.db import models

class Destination:
    id : int
    name : str
    img : str
    desc :str
    price : int
    offer: bool

class ToDoList(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()
    def __str__(self):
        return self.text

class ContactDetails(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class NewsTeller(models.Model):
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.email