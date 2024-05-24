from rest_framework import serializers
from sys_student import models as m_model


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = m_model.College
        fields = '__all__'
        depth = 1


# class MajorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = m_model.Major
#         fields = '__all__'
#         depth = 1


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = m_model.Grade
        fields = '__all__'
        depth = 2


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = m_model.Class
        fields = '__all__'
        depth = 2


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = m_model.Student
        exclude = ['is_delete', 'create_time']
        depth = 3


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = m_model.Course
        exclude = ['is_delete', 'create_time']

        # exclude = ['students', 'system_users']
        depth = 2


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = m_model.StudentCourseMemberShip
        # exclude = ['is_delete', 'create_time']
        fields = '__all__'
        depth = 2
        # read_only_fields=fields


class SystemUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = m_model.SystemUser
        exclude = ['is_delete', 'create_time']
        depth = 1


class SystemUserCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = m_model.SystemUserCourseMembership
        fields = '__all__'
        depth = 4


class SystemUserCollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = m_model.SystemUserCollegeMembership
        fields = '__all__'
        depth = 4


class SystemUserClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = m_model.SystemUserClassMembership
        fields = '__all__'
        depth = 4
