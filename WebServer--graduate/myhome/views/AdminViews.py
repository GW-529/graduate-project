from django.shortcuts import render
from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from ..models import *
import datetime
import math


# 管理平台主页
def index(request):
    # data = request.session.get("userinfo",None)
    # 1.获取5个最新的数据(教师和学生信息)
    data_len = 5
    data_list = []

    # （1.学生信息
    # 获取了最新的学生信息，并将每个学生的学号、姓名、注册时间等信息添加到 data_list 列表中，同时标记这些条目的类型为学生。
    data_list1 = Student.objects.filter().order_by('register_time')[:data_len]
    for item in data_list1:
        data_list.append({
            'number': item.number,
            'name':item.name,
            'register_time':item.register_time,
            'type':'学生',
        })

    # （2.教师信息（如果数量不够，则教师来补）
    # 如果 学生 数量不足 5 条，就从教师信息中获取足够数量的条目来填充，然后将其添加到 data_list 中。
    if len(data_list) < data_len:
        last_len = data_len - len(data_list)
        data_list2 = Teacher.objects.filter().order_by('register_time')[:last_len]
        for item in data_list2:
            data_list.append({
                'number':item.number,
                'name':item.name,
                'register_time':item.register_time,
                'type':'教师',
            })
    # 2.获取展示栏信息
    # 计算了过去 90 天内的学生和教师的注册数量，以及学生毕业文章的数量。
    last_time = datetime.datetime.now() - datetime.timedelta(days=90)
    data1_1 = Student.objects.all().count()
    data1_2 = len(Student.objects.filter(register_time__gte=last_time).values())
    data2_1 = Teacher.objects.all().count()
    data2_2 = len(Teacher.objects.filter(register_time__gte=last_time).values())
    data3_1 = StudentGraduateArticle.objects.all().count()
    data3_2 = math.ceil(StudentGraduateArticle.objects.all().count() / 2)

    # 将获取的展示栏信息存储在一个字典 show_data 中，准备传递给模板。
    show_data = {
        'show_count1':data1_1,
        'show_add1':data1_2,
        'show_count2':data2_1,
        'show_add2':data2_2,
        'show_count3':data3_1,
        'show_add3':data3_2,
    }
    # 将获取的数据和展示栏信息传递给名为 admin/index.html 的模板，并进行渲染。
    return render(request,'admin/index.html',{'data_list':data_list,'show_data':show_data})


# 教师管理
def teacher_list(request):
    # 获取数据库教师所有信息
    data_list = Teacher.objects.all()
    # 跳转
    return render(request,'admin/teacher_list.html',{'data_list':data_list})


def doDeleteTeacher(request):
    # 获取POST请求的数据
    data = request.POST.dict()
    # 从 Teacher 表中筛选出 id 等于 data['id'] 的记录，并将其删除
    if StudentSelectTitle.objects.filter(teacher_id=data['id']).exists():
        return JsonResponse({'msg': "无法删除,已有指导学生", 'code': 201})
    else:
        Teacher.objects.filter(id = data['id']).delete()
        return JsonResponse({'msg':"删除成功",'code':200})


def doSearchTeacher(request):
    # 将前端传来的 POST 请求中的数据转换为一个字典，并将其存储在变量 data 中。
    data = request.POST.dict()

    # 从 data 字典中提取出 keywords_name 和 keywords_value，分别表示要搜索的字段名和搜索的值。
    keywords_name = data['keywords_name']
    keywords_value = data['keywords_value']
    if keywords_value:
        # 创建一个名为 searchdata 的字典。__icontains，表示要在指定字段名上进行模糊查询
        searchdata = {f'{keywords_name}__icontains': keywords_value}
        # 用 Django ORM 的 filter 方法，根据 searchdata 中的条件筛选 Teacher 表中的数据，并将结果存储在 data_list 中。
        # **searchdata 是将字典解包成关键字参数。
        data_list = Teacher.objects.filter(**searchdata)
        # 返回一个 JSON 响应
    else:
        data_list = Teacher.objects.all()

    return JsonResponse({'msg':"查询成功",'data':serializers.serialize("json",data_list),'code':200})


# 学生管理
def student_list(request):
    data_list = Student.objects.all()
    return render(request,'admin/student_list.html',{'data_list':data_list} )


def doDeleteStudent(request):
    data = request.POST.dict()
    Student.objects.filter(id = data['id']).delete()
    return JsonResponse({'msg':"删除成功",'code':200})


def doSearchStudent(request):
    data = request.POST.dict()
    keywords_name = data['keywords_name']
    keywords_value = data['keywords_value']
    if keywords_value:
        searchdata = {f'{keywords_name}__icontains': keywords_value}
        data_list = Student.objects.filter(**searchdata)
    else:
        data_list = Student.objects.all()
    return JsonResponse({'msg':"查询成功",'data':serializers.serialize("json",data_list),'code':200})


# 课题管理
def title_list(request):
    data_list = StudentGraduateArticle.objects.all()
    return render(request,'admin/title_list.html',{'data_list':enumerate(data_list)})


def doDeleteTitle(request):
    data = request.POST.dict()
    StudentGraduateArticle.objects.filter(id = data['id']).delete()
    return JsonResponse({'msg':"删除成功",'code':200})


def doSearchTitle(request):
    data = request.POST.dict()
    keywords_name = data['keywords_name']
    keywords_value = data['keywords_value']
    if keywords_value:
        searchdata = {f'{keywords_name}__icontains': keywords_value}
        data_list = StudentGraduateArticle.objects.filter(**searchdata)
    else:
        data_list = StudentGraduateArticle.objects.all()
    return JsonResponse({'msg':"查询成功",'data':serializers.serialize("json",data_list),'code':200})