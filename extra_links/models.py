from django.db import models

class notice_board(models.Model):
    topic=models.CharField(max_length=300)
    date=models.DateTimeField()
    info=models.TextField()
    def __str__(self):
        return self.topic
