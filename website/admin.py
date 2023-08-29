from django.contrib import admin
from .models import Post
# Register your models here.

admin.site.register(Post)

from .models import MyModel, MatchHistory

admin.site.register(MyModel)
admin.site.register(MatchHistory)