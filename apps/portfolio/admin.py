from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(LinkModel)
admin.site.register(EducationModel)
admin.site.register(ExperienceModel)
admin.site.register(SkillModel)

