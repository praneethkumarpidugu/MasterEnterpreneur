from django.db import models
from accounts.models import MyUser
from videos.models import Video
# Create your models here.

class CommentManager(models.Manager):
    def create_comment(self, user=None, comment=None, path=None, video=None):
        if not path:
            raise ValueError("Must include a path when adding a comment")
        if not user:
            raise ValueError("Must include a user when adding a comment")

        comment = self.model(
            user = user,
            path = path,
            comment = comment
        )
        if video is not None:
            comment.video = video
        comment.save(using=self._db_)
        return comment


class Comment(models.Model):
    user = models.ForeignKey(MyUser)
    path = models.CharField(max_length=350)
    video = models.ForeignKey(Video, null=True, blank=True)
    text = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = CommentManager()

    def __unicode__(self):
        return self.user.username

    def get_comment(self):
        return self.text