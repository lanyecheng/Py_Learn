#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/7/28

from car import Car


class Battery:

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航"""
        mileage = 0
        if self.battery_size == 70:
            mileage = 240
        elif self.battery_size == 85:
            mileage = 270
        message = "This car can go approximately " + str(mileage)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
