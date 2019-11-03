from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Course, Teacher, Score, Student
import random
from django.db.models import Q, F, Count, Avg, Sum
from django.db import connection

def get_course_score(student):
    scores = Score.objects.all()
    student_course_score = []
    for score in scores:
        if student == score.student:
            student_course_score.append(score.number)
    student_course_score.insert(0, student.name)
    return student_course_score


def index(request):
    courses = Course.objects.all()
    students = Student.objects.all()
    student_score = []
    for student in students:
        student_score.append(get_course_score(student))
    print(student_score)

    context = {
        'scores': student_score,
        'courses': courses,
    }
    return render(request, 'index.html', context=context)

def add(request):
    # name_list = ['丽丽', '小明', '李磊', '王刚', '张伟', 'Jack', 'Lucy', 'Jim']
    # gender_list = [0, 1, 1, 1, 1, 1, 0, 1]
    # score_list = [98, 89, 74, 100, 78, 89, 84.5, 90]

    # 添加学生
    # for i in range(len(name_list)):
    #     student = Student(name=name_list[i], gender=gender_list[i])
    #     student.save()

    # 添加成绩
    # for i in range(1, 9):
    #     student = Student.objects.get(pk=i)
    #     for j in range(1, 5):
    #         course = Course.objects.get(pk=j)
    #         score = Score(number=random.randint(50, 101))
    #         score.student = student
    #         score.course = course
    #         score.save()
    if request.method == 'GET':
        return render(request, 'add.html')
    else:
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        python = request.POST.get('python')
        java = request.POST.get('java')
        front = request.POST.get('front')
        backend = request.POST.get('backend')
        Student(name=name, gender=gender).save()
        student = Student.objects.last()
        print(student.name)
        score_list2 = [python, java, front, backend]
        for i in range(1, 5):
            course = Course.objects.get(pk=i)
            score = Score(number=score_list2[i-1])
            score.course = course
            student.score_set.add(score, bulk=False)
            print(score.number)
            print(student.name)
    return redirect(reverse('index'))

def delete(request):
    # 删除选课数目小于3门的同学
    Student.objects.annotate(course_nums=Count('score__course')).exclude(course_nums__gt=3).delete()

    return HttpResponse('del success')

def query(request):
    # 1. 查询平均成绩大于60分的同学id和平均成绩
    students = Student.objects.annotate(score_avg=Avg('score__number')).filter(score_avg__gt=90).values('name', 'score_avg')
    for student in students:
        print(student)
    # 查看一下原始sql语句是如何写的
    print(connection.queries)
    return HttpResponse('query success')

def query2(request):
    # 2. 查询所有同学的id, 姓名， 选课数， 总成绩
    students = Student.objects.annotate(course_nums=Count('score__course'), total_score=Sum('score__number')).values('id', 'name', 'course_nums', 'total_score')
    for i in students:
        print(i)
    return HttpResponse('query success')

def query3(request):
    # 3. 查询姓李老师的个数
    # teachers = Teacher.objects.annotate(teacher_nums=Count('name')).filter(name__contains='李').values('name', 'teacher_nums')
    # 4. 查询没学过李老师课的同学的id， 和姓名
    # students = Student.objects.annotate(teacher_name=F('score__course__teacher__name')).exclude(teacher_name__contains='李').values('id', 'name', 'teacher_name')
    # 5. 查询学过id为1和2的所有同学的id, 姓名
    students = Student.objects.annotate(course = F('score__course')).exclude(course__name__icontains='python').values('id', 'name', 'course')
    for i in students:
        print(i)
    return HttpResponse('query3 success')