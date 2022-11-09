from django.db import models

class Todo(models.Model):
    title = CharField(max_lenght=150)
    description = CharField(max_lenght=300, blank=True)
    date = DateTimeField(auto_now_add=True)
    done = BooleanField(default=False)


    def __str__(self):
        return self.title