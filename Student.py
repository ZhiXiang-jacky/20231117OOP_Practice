# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 21:53:55 2023

@author: ZhiXiang
"""

class Student:
    def __init__(self,name,student_id,age,gender):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.gender = gender
        
    
    def set_grade(self, grade):
        
        self.grade = grade

    def get_grade(self):
        
        return print("成績是" + str(self.grade))
    
    def display_student_info(self):
        print("------------以下為完整資訊------------")
        print("我的名字是"+self.name)
        print("學號是" + str(self.student_id))
        print("年齡為" + str(self.age))
        print("性別是" + str(self.gender))

jacky = Student("游智翔",10415063,15,"男")

#設定成績為多少
jacky.set_grade(100)
#得出成績為多少
jacky.get_grade()
#叫出完整
jacky.display_student_info()