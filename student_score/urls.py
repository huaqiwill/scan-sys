from django.urls import path

from student_score import views

urlpatterns = [
    path("college_manage", views.college_manage),  # 学校管理页面
    path("college", views.CollegeManage.as_view()),  # 学校管理页面
    path("college_add", views.college_add),  # 学校增加页面
    path("grade_manage", views.grade_manage),  # 年级管理首次渲染
    path("grade", views.GradeManage.as_view()),  # 年级管理
    path("grade_add", views.grade_add),  # 年级增加页面
    path("class_manage", views.class_manage),  # 班级管理首次渲染
    path("class", views.ClassManage.as_view()),  # 班级管理
    path("class_add", views.class_add),  # 班级增加页面
    path(
        "class_query", views.class_query
    ),  # 班级查询--成绩录入页面（点击学校下拉时查询班级）
    path("course_manage", views.course_manage),  # 课程管理首次渲染
    path("course", views.courseManage.as_view()),  # 课程管理
    path("course_add", views.course_add),  # 课程增加页面
    path("student_manage", views.student_manage),  # 学生管理首次渲染
    path("student", views.studentManage.as_view()),  # 学生管理
    path("student_add", views.student_add),  # 学生增加页面
    path("student_upload_add", views.student_upload_add),  ## 弹出批量导入页面
    path("student_multi", views.student_multi),  ## 批量导入
    path("score_manage", views.score_manage),  # 课程管理首次渲染
    path("score", views.ScoreManage.as_view()),  # 成绩管理
    path("score_query", views.score_query),  # 成绩查询
    path("banji_score_count", views.banji_score_count.as_view()),  # 班级成绩管理
    path("banji_score", views.banji_score),  # 班级成绩管理
    path("stu_score_manage", views.stu_score_manage),  # 学生成绩
    path("stu_score", views.stu_ScoreManage.as_view()),  # 成绩管理
]
