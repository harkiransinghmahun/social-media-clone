from django.contrib import admin
from groups import models

# Register your models here.

# With the TabularInline you dont have to register the child model
# In this case the child model is GroupMember and parent model is Group
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
