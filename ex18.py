#-*- coding:utf-8 -*-
#函数初步使用

#this one is like your scripts with agrv

#*args 是接受函数传过来的所有参数，放到args列表中
def print_two(*args):
	arg1,arg2 = args
	print("arg1:{},arg2:{}".format(arg1,arg2))

def print_two_again(arg1,arg2):
	print("arg1:{},arg2:{}".format(arg1,arg2))

def print_one(arg1):
	print("arg1:",arg1)


def print_none():
	print("I got nothin")


print_two("Zed",'Shaw')

print_two_again('Zed','Shaw')

print_one("First!")

print_none()
