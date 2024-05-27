# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    number = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    register_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Student(models.Model):
    number = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    cross = models.CharField(max_length=255, blank=True, null=True)
    register_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'student'


class StudentGraduateAnswer(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    brief = models.CharField(max_length=255, blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    student_name = models.CharField(max_length=255, blank=True, null=True)
    teacher_id = models.IntegerField(blank=True, null=True)
    teacher_name = models.CharField(max_length=255, blank=True, null=True)
    third_score = models.CharField(max_length=255, blank=True, null=True)
    third_remark = models.CharField(max_length=255, blank=True, null=True)
    graduate_rank = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'student_graduate_answer'

'''
name: 文章名称，类型为 CharField，最大长度为 255，可以为空。
brief: 文章简介，类型为 CharField，最大长度为 255，可以为空。
student_id: 学生的 ID，类型为 IntegerField，可以为空。
student_name: 学生的姓名，类型为 CharField，最大长度为 255，可以为空。
teacher_id: 教师的 ID，类型为 IntegerField，可以为空。
teacher_name: 教师的姓名，类型为 CharField，最大长度为 255，可以为空。
guide_score: 导师评分，类型为 CharField，最大长度为 255，可以为空。
guide_remark: 导师评语，类型为 CharField，最大长度为 255，可以为空。
view_score: 审阅评分，类型为 CharField，最大长度为 255，可以为空。
view_remark: 审阅评语，类型为 CharField，最大长度为 255，可以为空。
article_docx: 文章文档路径，类型为 CharField，最大长度为 255，可以为空。
total_docx: 总评文档路径，类型为 CharField，最大长度为 255，可以为空。
'''
class StudentGraduateArticle(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    brief = models.CharField(max_length=255, blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    student_name = models.CharField(max_length=255, blank=True, null=True)
    teacher_id = models.IntegerField(blank=True, null=True)
    teacher_name = models.CharField(max_length=255, blank=True, null=True)
    guide_score = models.CharField(max_length=255, blank=True, null=True)
    guide_remark = models.CharField(max_length=255, blank=True, null=True)
    view_score = models.CharField(max_length=255, blank=True, null=True)
    view_remark = models.CharField(max_length=255, blank=True, null=True)
    article_docx = models.CharField(max_length=255, blank=True, null=True)
    total_docx = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'student_graduate_article'


class StudentGroup(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    student_id = models.CharField(max_length=11, blank=True, null=True)
    student_name = models.CharField(max_length=255, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'student_group'

'''
name: 标题名称，最大长度为 255 个字符，可以为空。
brief: 简介，最大长度为 255 个字符，可以为空。
student_id: 学生ID，整数类型，可以为空。
student_name: 学生姓名，最大长度为 255 个字符，可以为空。
teacher_id: 教师ID，整数类型，可以为空。
teacher_name: 教师姓名，最大长度为 255 个字符，可以为空。
second_score: 第二次评分，最大长度为 255 个字符，可以为空。
second_remark: 第二次评语，最大长度为 255 个字符，可以为空。
这些字段描述了学生中期检查的各个方面，包括学生和教师的身份信息、选题名称、简介以及第二次评分和评语。
'''
class StudentMiddleCheck(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    brief = models.CharField(max_length=255, blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    student_name = models.CharField(max_length=255, blank=True, null=True)
    teacher_id = models.IntegerField(blank=True, null=True)
    teacher_name = models.CharField(max_length=255, blank=True, null=True)
    second_score = models.CharField(max_length=255, blank=True, null=True)
    second_remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'student_middle_check'

'''
name: 标题名称，最大长度为 255 个字符，可以为空。
brief: 简介，最大长度为 255 个字符，可以为空。
student_id: 学生ID，整数类型，可以为空。
student_name: 学生姓名，最大长度为 255 个字符，可以为空。
teacher_id: 教师ID，整数类型，可以为空。
teacher_name: 教师姓名，最大长度为 255 个字符，可以为空。
task_docx: 任务文档，最大长度为 255 个字符，可以为空。
guide_docx: 指导文档，最大长度为 255 个字符，可以为空。
这些字段描述了学生选题信息的各个方面，包括学生和教师的身份信息、选题名称、简介以及相关文档的路径。
'''
class StudentSelectTitle(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    brief = models.CharField(max_length=255, blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    student_name = models.CharField(max_length=255, blank=True, null=True)
    teacher_id = models.IntegerField(blank=True, null=True)
    teacher_name = models.CharField(max_length=255, blank=True, null=True)
    task_docx = models.CharField(max_length=255, blank=True, null=True)
    guide_docx = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'student_select_title'

'''
name: 标题名称，最大长度为 255 个字符，可以为空。
brief: 简介，最大长度为 255 个字符，可以为空。
student_id: 学生ID，整数类型，可以为空。
student_name: 学生姓名，最大长度为 255 个字符，可以为空。
teacher_id: 教师ID，整数类型，可以为空。
teacher_name: 教师姓名，最大长度为 255 个字符，可以为空。
first_score: 第一次评分，最大长度为 255 个字符，可以为空。
first_remark: 第一次评语，最大长度为 255 个字符，可以为空。
english_score: 英语评分，最大长度为 255 个字符，可以为空。
english_remark: 英语评语，最大长度为 255 个字符，可以为空。
title_docx: 标题文档，最大长度为 255 个字符，可以为空。
english_docx: 英语文档，最大长度为 255 个字符，可以为空。
apply_docx: 申请文档，最大长度为 255 个字符，可以为空。
这些字段描述了学生选题信息的各个方面，包括学生和教师的身份信息、评分、评语以及相关文档的路径。
'''
class StudentTitleMsg(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    brief = models.CharField(max_length=255, blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    student_name = models.CharField(max_length=255, blank=True, null=True)
    teacher_id = models.IntegerField(blank=True, null=True)
    teacher_name = models.CharField(max_length=255, blank=True, null=True)
    first_score = models.CharField(max_length=255, blank=True, null=True)
    first_remark = models.CharField(max_length=255, blank=True, null=True)
    english_score = models.CharField(max_length=255, blank=True, null=True)
    english_remark = models.CharField(max_length=255, blank=True, null=True)
    title_docx = models.CharField(max_length=255, blank=True, null=True)
    english_docx = models.CharField(max_length=255, blank=True, null=True)
    apply_docx = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'student_title_msg'


class Teacher(models.Model):
    number = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    group_type = models.CharField(max_length=255, blank=True, null=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    register_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'teacher'

'''
name: CharField 类型，用于存储组名，是必填字段。
teacher: ForeignKey 类型，关联到 Teacher 模型，使用级联删除。
count: IntegerField 类型，用于存储组成员数，默认为 0，可以为空。
teacher_type: CharField 类型，用于存储教师类型，可以为空。
Meta 类: 设置表名为 teacher_group，并在 name 字段上添加索引以提高查询性能。
'''
class TeacherGroup(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    teacher_id = models.CharField(max_length=11, blank=True, null=True)
    teacher_name = models.CharField(max_length=255, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    teacher_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'teacher_group'


class teachertopic(models.Model):
    topic = models.CharField(max_length=255, blank=True, null=True)
    teacher_id = models.CharField(max_length=11,blank=True, null=True)
    teacher_name = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'teacher_topic'