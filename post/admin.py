from django.contrib import admin
from .models import Post, Editor, Remark, Contact
# Register your models here.
admin.site.register(Post)
admin.site.register(Editor)
admin.site.register(Remark)
admin.site.register(Contact)