from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

#from .users.models import Teacher, Student

class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title

class Course(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='courses_created',
        on_delete=models.CASCADE
    )
    subject = models.ForeignKey(
            Subject,
            related_name='courses',
            on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    overview = models.TextField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

class CourseFlow (models.Model):
    course = models.ForeignKey(
        Course,
        related_name='flows',
        on_delete=models.CASCADE
    )
    start = models.DateTimeField()
    duration = models.DurationField()
    students = models.ManyToManyField(
        User,
        related_name='courses_joined',
        blank=True
    )

    def __str__ (self):
        return f"{self.course.title} {self.start}"

class Module(models.Model):
    course = models.ForeignKey(
            Course,
            related_name='modules',
            on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.title

class Lesson(models.Model):
    module = models.ForeignKey(
            Module,
            related_name='lessons',
            on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    youtube_id = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title

class HomeTask(models.Model):
    lesson = models.ForeignKey(
            Lesson,
            related_name='home_tasks',
            on_delete=models.CASCADE
    ) 
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class EvaluationCriterion (models.Model):
    hometask = models.ForeignKey(
            HomeTask,
            related_name='evaluation_criterions',
            on_delete=models.CASCADE
            )
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Content(models.Model):
    module = models.ForeignKey(
            Module,
            related_name='contents',
            on_delete=models.CASCADE
    )
    content_type = models.ForeignKey(
            ContentType,
            on_delete=models.CASCADE,
            limit_choices_to={'model__in':(
                'text',
                'video',
                'image',
                'file'
                )
            }
    )
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')


class ItemBase(models.Model):
    owner = models.ForeignKey(
            User,
            related_name='%(class)s_related',
            on_delete=models.CASCADE
    )
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    def __str__(self):
        return self.title

class Text(ItemBase):
    content = models.TextField()

class File(ItemBase):
    file = models.FileField(upload_to='files')

class Image(ItemBase):
    file = models.FileField(upload_to='images')

class Video(ItemBase):
    url = models.URLField()

class AnonymusQuestion (models.Model):
    sender = models.ForeignKey(
            User,
            related_name='questions',
            on_delete=models.CASCADE,
            blank = True
            )
    name = models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Телефон должен быть в формате: '+999999999'. До 15 цифр разрешено.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) 
    def __str__(self):
        return self.title

