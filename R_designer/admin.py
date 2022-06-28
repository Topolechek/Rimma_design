from django.contrib import admin
from feedback.models import FeedBack
from comment.models import Comment

admin.site.register(FeedBack)
admin.site.register(Comment)