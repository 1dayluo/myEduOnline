from django.db import models

# Create your models here.
from datetime import datetime
from users.models import UserProfile
from courses.models import Course


#用户我要学习表单
class UserAsk(models.Model):
    namee=models.CharField(max_length=20,verbose_name=u"姓名")
    mobile=models.CharField(max_length=11,verbose_name=u"手机")
    course_name=models.CharField(max_length=50,verbose_name=u"课程名")
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"用户咨询"
        verbose_name_plural=verbose_name

#用户对于课程评论
class CourseComments(models.Model):
    course=models.ForeignKey(Course,verbose_name=u"课程",on_delete=models.CASCADE)
    user=models.ForeignKey(UserProfile,verbose_name=u"用户")
    comments=models.CharField(max_length=250,verbose_name=u"评论")
    add_times=models.DateTimeField(default=datetime.now,verbose_name=u"评论时间")
    class Meta:
        verbose_name=u"课程评论"
        verbose_name_plural=verbose_name
#用户对于课程，机构，讲师的收藏
class UserFavorite(models.Model):
    TYPE_CHOICES=(
        (1,u"课程"),
        (2,u"课程机构"),
        (3,u"讲师")
    )
    user=models.ForeignKey(UserProfile,verbose_name=u"用户",on_delete=models.CASCADE)
    fav_id=models.IntegerField(default=0)
    fav_type=models.IntegerField(
        choice=TYPE_CHOICES,
        default=1,
        verbose_name=u"收藏类型"
    )
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u"评论时间")
    class Meta:
        verbose_name=u"用户收藏"
        verbose_name_plural=verbose_name
#用户消息表
class UserMessage(models.Model):
    #为0发给全部用户
    user=models.IntegerField(default=0,verbose_name=u"接受用户")
    messsage=models.CharField(max_length=500,verbose_name=u"消息内容")

    #是否已读
    has_read=models.BooleanField(default=False,verbose_name=u"是否已读")
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")
    class Meta:
        verbose_name=u"用户消息"
        verbose_name_plural=verbose_name

#课程表
class UserCourse(models.Model):
    course=models.ForeignKey(Course,verbose_name=u"课程",on_delete=models.CASCADE)
    user=models.ForeignKey(UserProfile,verbose_name=u"用户",on_delete=models.CASCADE)
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"用户课程"
        verbose_name_plural=verbose_name
