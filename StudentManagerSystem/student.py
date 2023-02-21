# -*- coding:utf-8 -*-
# @author zhouwei
# @date 2023/2/21 10:46
# @file student.py

"""
需求：
    1、学员信息包括：姓名、性别、手机号
    2、添加 __str__ 方法，方便查看学员对象信息
"""


class Student(object):
    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f"{self.name},{self.gender},{self.tel}"


# Test
if __name__ == "__main__":
    student = Student("张三", "男", "123456789")
    print(student)
