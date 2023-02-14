# -*- coding:utf-8 -*-
# @author zhouwei
# @date 2023/2/14 15:08
# @file 烤地瓜.py


"""
1、定义类：
    初始化属性，被烤和添加调料的方法，显示对象信息的str
"""


class SweetPotato:
    def __init__(self):
        # 状态
        self.cook_static = "生的"
        # 调料列表
        self.condiments = []
        # 被烤的时间
        self.cook_time = 0

    def cook(self, time):
        """烤地瓜的方法"""
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_static = "生的"
        elif 3 <= self.cook_time < 5:
            self.cook_static = "半生不熟"
        elif 5 <= self.cook_time <= 8:
            self.cook_static = "熟的"
        elif self.cook_time > 8:
            self.cook_static = "烤糊了"

    def add_condiments(self, condiment):
        """
        添加调料
        :param condiment:
        :return:
        """
        self.condiments.append(condiment)

    def __str__(self):
        return f"这个地瓜烤了{self.cook_time}分钟，状态是{self.cook_static}，添加的调料有{self.condiments}"


# 2、创建对象并调用对应的实例方法
digua1 = SweetPotato()
print(digua1)

digua1.cook(2)
digua1.add_condiments("酱油")
print(digua1)

digua1.cook(2)
digua1.add_condiments("辣椒面")
print(digua1)
