# from django.contrib.auth.models import User

from django.db import models
from manage.models import User, Role

# Create your models here.

class BaseModel(models.Model):
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    # 设置 abstract = True 来声明基表，作为基表的Model不能在数据库中形成对应的表
    class Meta:
        abstract = True

class SystemUser(BaseModel):
    """
    扩展用户表
    """
    # user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=100, null=True, help_text='工号',unique=True)
    name = models.CharField(max_length=100, null=True, help_text='姓名')
    sex = models.CharField(null=True, max_length=100, help_text='性别')
    phone = models.CharField(null=True, max_length=100, help_text='手机号')
    role = models.CharField(null=True, max_length=100, help_text='角色, 教师, 导员，管理员， 主任')
    audit = models.BooleanField(default=False, null=True, max_length=100, help_text='审核')

class College(BaseModel):
    """
    学院表
    """
    name = models.CharField(verbose_name="学校名称",max_length=100, null=True, help_text='名称')
    system_users = models.ManyToManyField(SystemUser, through='SystemUserCollegeMembership')

    def __str__(self):
        return self.name

class Grade(BaseModel):
    """
    年级表
    """
    level_choices = (
        ('一年级', '一年级'),
        ('二年级', '二年级'),
        ('三年级', '三年级'),
        ('四年级', '四年级'),
        ('五年级', '五年级'),
        ('六年级', '六年级'),
    )
    college = models.ForeignKey(College, verbose_name="所属学校",help_text='所属学校', related_name='grade', null=True, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="年级",choices=level_choices,max_length=100, null=True, help_text='名称')

    def __str__(self):
        return self.college.name

class Class(BaseModel):
    """
    班级
    """

    grade = models.ForeignKey(Grade, help_text='所属年级', related_name='t_class', null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, help_text='名称')
    system_users = models.ManyToManyField(SystemUser, through='SystemUserClassMembership',
                                          help_text='导员和班级多对多关系')

class Student(BaseModel):
    """
    学生表
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # t_college = models.ForeignKey(College, verbose_name="所属学校", help_text='所属学校', related_name='college_student', null=True,on_delete=models.CASCADE)
    # t_grade = models.ForeignKey(Grade, verbose_name="所属年级", help_text='所属年级', related_name='grade_student', null=True,on_delete=models.CASCADE)
    t_class = models.ForeignKey(Class, verbose_name="所属班级",help_text='所属班级',  related_name='class_student',null=True, on_delete=models.CASCADE)
    # student_id = models.CharField(verbose_name="学号",max_length=100, null=True, help_text='学号', unique=True)
    name = models.CharField(verbose_name="学生姓名",max_length=100, null=True, help_text='名称')
    # sex = models.CharField(null=True, max_length=100, help_text='性别')
    # phone = models.CharField(null=True, max_length=100, help_text='手机号')
    # position = models.CharField(null=True, max_length=100, help_text='担任班级职位')
    # audit = models.BooleanField(default=False, null=True, max_length=100, help_text='审核')

class Course(BaseModel):
    """
    课程表
    """
    MODE_CHOICES = (
        ('必修', '必修'),
        ('选修', '选修'),
    )
    level_choices = (
        ('语文', '语文'),
        ('数学', '数学'),
        ('英语', '英语'),
    )
    grade = models.ForeignKey(Grade, verbose_name="所属年级",help_text='所属年级', related_name='course', null=True, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="课程名称",choices=level_choices,max_length=100, null=True, help_text='名称')
    # point = models.FloatField(verbose_name="学分",null=True, help_text='学分')
    students = models.ManyToManyField(Student, verbose_name="学生姓名",through='StudentCourseMemberShip')
    system_users = models.ManyToManyField(SystemUser, verbose_name="用户名",through='SystemUserCourseMembership', help_text='教师和课程多对多关系')

    def __str__(self):
        return self.name

class StudentCourseMemberShip(BaseModel):
    """
    学生和课程，多对多关系
    """
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    result = models.FloatField(null=True, blank=True,help_text='实际得分')
    when = models.CharField(null=True, max_length=100, help_text='什么时候的考试， 第一学期，第二学期')

    def class_ranking(self, when='第一学期'):
        """
        班级排名
        """
        pass

    def grade_ranking(self, when='第一学期'):
        """
        年级的排名
        """
        pass

    def not_passed_course(self):
        """
        不及格课程
        """
        pass


class SystemUserCourseMembership(BaseModel):
    """
    老师(用户)和课程的关系，多对多
    """
    system_user = models.ForeignKey(SystemUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class SystemUserClassMembership(BaseModel):
    """
    导员（用户）和班级的关系，多对多
    """
    system_user = models.ForeignKey(SystemUser, on_delete=models.CASCADE)
    t_class = models.ForeignKey(Class, on_delete=models.CASCADE)
class SystemUserCollegeMembership(BaseModel):
    """
    主任（用户）和院系的关系，多对多
    """
    system_user = models.ForeignKey(SystemUser, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

