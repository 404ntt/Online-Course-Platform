from django.contrib import admin
import core.models as model
admin.site.register(model.CustomUser)
admin.site.register(model.Lesson)
admin.site.register(model.Course)