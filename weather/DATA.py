#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
import json
import urllib

#天气类
class Weather:
    def __init__(self,aimed_cityname):#用户想要查询的城市
        self.aimed_cityname=aimed_cityname

    def request(self):#API请求，获取相应城市的天气信息
        self.raw_weathers_info = requests.get('http://v.juhe.cn/weather/index?format=2&cityname=%s&key=d9e072c6f2f175e99c56e7413253ac80' % self.aimed_cityname)
        self.weathers_info = json.loads(self.raw_weathers_info.text)

    def sort(self):#整理接收的天气信息
        self.today_info=self.weathers_info["result"]["future"][0]#今日各类信息
        self.today_date=self.today_info["date"]#今日日期
        self.today_week = self.today_info["week"]#今日星期数
        self.today_temperature = self.today_info["temperature"]#今日温度
        self.today_weather = self.today_info["weather"]#今日天气
        self.today_wind = self.today_info["wind"]#今日风力
        self.city = self.weathers_info["result"]["today"]["city"]#城市中文名

#城市类
class City:
    def __init__(self,aimed_city): #用户想要查询的城市
        self.aimed_city=aimed_city
        self.found = 0  # 指示变量，为1时表示用户想要查询的城市在数据端可查列表中

    def request(self): #API请求，获取数据端可查询的城市列表
        self.raw_cities = requests.get('http://v.juhe.cn/weather/citys?key=d9e072c6f2f175e99c56e7413253ac80')
        self.cities = json.loads(self.raw_cities.text)

    def match(self): #城市匹配，判断用户想要查询的城市是否在数据端可查列表中
        for index in self.cities["result"]:
            if index["city"] == self.aimed_city:
                self.found = 1
                break

    def get_weather_info(self): #获取相应城市天气信息
        if self.found:#仅在相应城市可查时执行
            self.aimed_cityname = urllib.parse.quote(self.aimed_city)  # 对城市名做UTF-8转换以满足后续查询天气时对请求格式的要求
            self.weather=Weather(self.aimed_cityname)#天气类实例化
            self.weather.request()#API请求，获取相应城市的天气信息
            self.weather.sort()#整理接收的天气信息
