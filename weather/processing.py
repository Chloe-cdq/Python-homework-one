#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from tkinter import ttk
import tkinter as tk
from DATA import *

#按钮点击后的执行函数
def show_info():
    aimed_city = user_text.get() #获取输入控件的信息，得到用户希望查询的城市

    city = City(aimed_city)#城市类实例化，传入用户想要查询的城市名
    city.request()#API请求，获取数据端可查询的城市列表
    city.match()#城市匹配，判断用户想要查询的城市是否在数据端可查列表中
    city.get_weather_info()#获取相应城市天气信息

    # 判断用户想要查询的城市是否在数据端可查列表中
    if city.found :#若在，显示天气信息表格
        tree = ttk.Treeview(root,show="headings")
        tree.pack()
        tree["columns"] = ("item","info")
        tree.column("item", width=100)
        tree.column("info", width=100)
        tree.heading("item", text="项目")
        tree.heading("info", text="信息")
        tree.insert("", 0, values=("日期",city.weather.today_date))
        tree.insert("", 1, values=("星期",city.weather.today_week))
        tree.insert("", 2, values=("城市",city.weather.city))
        tree.insert("", 3, values=("温度",city.weather.today_temperature))
        tree.insert("", 4, values=("天气",city.weather.today_weather))
        tree.insert("", 5, values=("风向风力",city.weather.today_wind))
    else:#若目标城市不在数据端可查列表中，显示错误提示信息
        error_info = tk.Label(root, text="查询的城市不在服务范围！")
        error_info.pack()

#设置主窗口
root = tk.Tk()
root.title("天气查询")
root.geometry("400x220")

#设置输入提示控件
input_promt = tk.Label(root, text="请输入您所要查询的城市中文名：")
input_promt.pack()

#设置输入控件
user_text = tk.Entry(root)
user_text.pack()

#设置按钮控件
tk.Button(root, text="输入完毕请点击", command=show_info).pack()

#窗口循环
root.mainloop()