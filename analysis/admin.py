from django.contrib import admin
from .models import UserInfo, PostGraduateCourse, UnderGraduateCourse, EducationalInfo


# Register your models here.
admin.site.register(UserInfo)
admin.site.register(UnderGraduateCourse)
admin.site.register(PostGraduateCourse)
admin.site.register(EducationalInfo)