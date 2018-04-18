from django.db import models
from datetime import  datetime
# Create your models here.


class Course(models.Model):
    DEGREE_CHOICES = (
        ("cj",u"初级"),
        ("zj",u"中级"),
        ("gj",u"高级")
    )

    name=models.CharField(max_length=50,verbose_name=u"课程名")
    desc=models.CharField(max_length=300,verbose_name=u"课程描述")
    detail=models.TextField(verbose_name=u"课程详情")
    degree=models.CharField(choices=DEGREE_CHOICES,max_length=2)
    learn_times = models.IntegerField(default==0,verbose_name=u"学习时长（分钟）")
    students=models.IntegerField(default=0,verbose_name=u"学习人数")
    fav_nums=models.IntegerField(default=0,verbose_name=u"收藏人数")
    image=models.ImageField(
        upload_to="courses/%Y/%m",
        verbose_name=u"封面图",
        max_length=100
    )
    click_nums=models.IntegerField(default=0,verbose_name=u"点击数")
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"课程"
        verbose_name_plural=verbose_name

#章节
class Lesson(models.Model):
    course = models.ForeignKey(Course,verbose_name=u"课程",on_delete=models.CASCADE)
    name=models.CharField(max_length=100,verbose_name=u"章节名")
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")
    class Meta:
        verbose_name=u"章节"
        verbose_name_plural=verbose_name

#每章视频
class Video(models.Model):
    lesson=models.ForeignKey(Lesson,verbose_name=u"章节",on_delete=models.CASCADE)
    name=models.CharField(max_length=100,verbose_name=u"视频名")
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"视频"
        verbose_name_plural=verbose_name

#课程资源
class CourseResource(models.Model):
    course=models.ForeignKey(Course,verbose_name=u"课程",on_delete=models.CASCADE)
    name=models.CharField(max_length=100,verbose_name=u"名称")
    #这里定义文件类型的field 后台对应上传按钮
    download=models.FileField(
        upload_to="course/resource/%Y/%m",
        verbose_name=u"资源文件",
        max_length=100
    )
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"课程资源"
        verbose_name_plural=verbose_name