# -*- coding:utf-8 -*-
# @author zhouwei
# @date 2023/2/21 10:46
# @file managerSystem.py


"""
需求：
    - 存储数据的位置：文件（student.data）
        - 加载文件数据
        - 修改数据后保存到文件
    - 存储数据形式：列表存储学员对象
    - 系统功能：
        - 添加学员
        - 删除学员
        - 修改学员
        - 查询学员信息
        - 显示所有学员信息
        - 保存学员信息
"""
from StudentManagerSystem.student import Student

"""
管理系统框架
    需求：系统功能循环使用，用户输入不用的功能序号执行不同的功能
    步骤：
        - 定义程序入口函数
            - 加载数据
            - 显示功能菜单
            - 用户输入功能序号
            - 根据用户输入的功能序号执行不同的功能
        - 定义系统功能函数，添加/删除学员等
"""


class StaudentManager(object):
    def __init__(self):
        # 存储数据所用列表
        self.student_list = []

    def run(self):
        """
        程序入口函数，启动程序后执行的函数
        :return:
        """
        # 加载学员信息
        self.load_student()

        while True:
            # 显示功能菜单
            self.show_menu()

            # 用户端输入功能序号
            menu_num = int(input("请输入您需要的功能序号："))
            # 根据用户输入的功能需要执行不同的功能
            if menu_num == 1:
                # 添加学员
                self.add_student()
            elif menu_num == 2:
                # 删除学员
                self.del_student()
            elif menu_num == 3:
                # 修改学员信息
                self.modify_student()
            elif menu_num == 4:
                # 查询学员信息
                self.search_student()
            elif menu_num == 5:
                # 显示所有学员信息
                self.show_student()
            elif menu_num == 6:
                # 保存学员信息
                self.save_student()
            elif menu_num == 7:
                # 退出系统
                break

    @staticmethod
    def show_menu():
        """
        显示功能菜单
        打印序号功能
        :param self:
        :return:
        """
        print("请选择如下功能：")
        print("1、添加学员")
        print("2、删除学员")
        print("3、修改学员休息")
        print("4、查询学员信息")
        print("5、显示所有学员信息")
        print("6、保存学员信息")
        print("7、退出系统")

    def add_student(self):
        """
        添加学员信息
        用户输入学员姓名、性别、手机号，将学员添加到系统
        - 用户输入姓名、性别、手机号
        - 创建该学员对象
        - 将该学员对象添加到列表
        """
        name = input("请输入学员姓名：")
        gender = input("请输入学员性别：")
        tel = input("请输入学员手机号：")
        student = Student(name, gender, tel)
        self.student_list.append(student)
        print(self.student_list)
        print(student)

    def del_student(self):
        """
        删除学员
        """
        del_name = input("请输入需要删除的学员姓名")
        """
        如果用户输入的目标学员存在则删除，否则提示学员不存在
        """
        for i in self.student_list:
            if i.name == del_name:
                self.student_list.remove(i)
                break
            else:
                print("查无此人")

        # 打印学员列表，验证删除功能
        print(self.student_list)

    def modify_student(self):
        """
        修改学员信息
        """
        modify_name = input("请输入要修改的学员的姓名：")
        # 如果用户输入的目标学员存在则修改姓名/性别/手机号等数据，否则提示学员不存在
        for i in self.student_list:
            if i.name == modify_name:
                i.name = input("请输入学员姓名：")
                i.gender = input("请输入学员性别：")
                i.tel = input("请输入学员手机号：")
                print(f"修改该学员信息成功，姓名：{i.name},性别：{i.gender},手机号：{i.tel}")
                break
            else:
                print("查无此人")

    def search_student(self):
        """
        查询学员信息
        """
        search_name = input("请输入要查询的学员的姓名：")
        for i in self.student_list:
            if i.name == search_name:
                print(f"该学员信息如下，姓名：{i.name}\t,性别：{i.gender}\t,手机号：{i.tel}")
                break
            else:
                print("查无此人")

    def save_student(self):
        """
        保存学员信息
        """
        # 打开文件
        f = open("student.data", "w")
        """
        文件写入学员数据
        文件写入的数据不能是学员对象的内存地址，需要把学员数据转换成列表字典数据再做存储
        """
        new_list = [i.__dict__ for i in self.student_list]
        # 文件内数据要求为字符串类型，需要先转换数据类型为字符串才能写入文件
        f.write(str(new_list))
        f.close()

    def show_student(self):
        """
        显示所有学员信息
        """
        print("姓名\t性别\t手机号")
        for i in self.student_list:
            print(f"{i.name}\t{i.gender}\t{i.tel}")

    def load_student(self):
        """
        加载学员信息
        """
        # 尝试以 r 模式打开数据文件，文件不存在则提示用户，文件存在则读取数据
        try:
            f = open("student.data", "r")
        except BaseException:
            f = open("student.data", "w")
        else:
            # 读取数据
            data = f.read()
            # 文件中读取的数据都是字符串且字符串内部为字典数据，需要转换数据类型再转换字典为对象后存储到学员列表
            new_list = eval(data)
            self.student_list = [
                Student(i["name"], i["gender"], i["tel"]) for i in new_list
            ]
        finally:
            f.close()
