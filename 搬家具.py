# -*- coding:utf-8 -*-
# @author zhouwei
# @date 2023/2/14 16:15
# @file 搬家具.py


class Furniture:
    """
    家具类
    """

    def __init__(self, name, area):
        # 家具名称
        self.name = name
        # 家具占地面积
        self.area = area


class Home:
    """
    房子类
    """

    def __init__(self, address, area):
        # 地理位置
        self.address = address
        # 房屋面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.furniture = []

    def __str__(self):
        return f"房子坐落于{self.address}，占地面积{self.area}，剩余面积{self.free_area}，家具有{self.furniture}"

    def add_furnture(self, item):
        """容纳家具"""
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            # 家具搬进后，房屋剩余面积 = 之前的面积 - 该家具面积
            self.free_area -= item.area
        else:
            print("家具太大，剩余面积不足，无法容纳！！！")


# 双人床
bed = Furniture("双人床", 6)
sofa = Furniture("沙发", 10)
dashuigan = Furniture("大水看", 10000)

home = Home("北京", 1000)
home.add_furnture(bed)
print(home)
home.add_furnture(dashuigan)
print(home)
