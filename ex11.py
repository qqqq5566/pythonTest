#-*- coding:utf-8 -*-

#用户输入

print('How old are you?',end=' ')
age = int(input())

print("How tall are you",end=' ')
height = input()
print("How much do you weight",end=' ')
weight = input()

print(type(age))

print("So,you're {} old,{} tall and {} heavy".format(age,height,weight))
