from django.db import models
from django.contrib.auth.models import User

from vote.models import VoteModel

from users.models import Author


class Story(VoteModel, models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    blacklist = models.ManyToManyField(User, blank=True)

    class Meta:
        ordering = ['-posted_on']
        verbose_name_plural = 'stories'

    def __str__(self):
        return '{} by {} ({})'.format(self.title, self.author, self.posted_on)


class StoryLine(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['posted_on']
        unique_together = ('story', 'content')

    def __str__(self):
        return 'Story line #{} - {}'.format(self.id, self.story)
