# Django Core
from django.db import models
from django.contrib.auth.models import User

# Owner
from reusable.constants import REQUIRED, NULL


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    profession = models.CharField(max_length=50, **NULL)
    location = models.CharField(max_length=250, **NULL)
    about = models.TextField()

    def __str__(self):
        return f'Perfil de: {self.user}'


class LinkModel(models.Model):
    profile = models.ForeignKey(
        Profile,
        related_name='links',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50, **REQUIRED)
    link = models.URLField()

    def __str__(self):
        return f'link {self.name} del perfil: {self.profile.user}'


class ExperienceModel(models.Model):
    profile = models.ForeignKey(
        Profile,
        related_name='experiencias',
        on_delete=models.CASCADE
    )
    picture = models.ImageField(max_length=1000, upload_to='picture-experience/', **NULL)
    name = models.CharField(max_length=70, **NULL)
    start_date = models.DateTimeField(verbose_name='Fecha Inicial', **NULL)
    end_date = models.DateTimeField(verbose_name='Fecha Final', **NULL)
    description = models.TextField()

    def __str__(self):
        return f'Experiencia {self.name} de: {self.profile.user}'


class EducationModel(models.Model):
    profile = models.ForeignKey(
        Profile,
        related_name='educaciones',
        on_delete=models.CASCADE
    )
    picture = models.ImageField(max_length=1000, upload_to='picture-education/', **NULL)
    name = models.CharField(max_length=70, **NULL)
    start_date = models.DateTimeField(verbose_name='Fecha Inicial', **NULL)
    end_date = models.DateTimeField(verbose_name='Fecha Final', **NULL)
    description = models.TextField()

    def __str__(self):
        return f'Education {self.name} de: {self.profile.user}'


class SkillModel(models.Model):
    profile = models.ForeignKey(
        Profile,
        related_name='skills',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=70, **REQUIRED)
    percent = models.PositiveSmallIntegerField(
        verbose_name='Porcentaje',
        default=0
    )

    def __str__(self):
        return f'Skill {self.name} de {self.profile.user}'