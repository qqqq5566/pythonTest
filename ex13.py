#-*- coding:utf-8 -*-

#运行脚本的时候，传递参数

from sys import argv
#read the WYSS section for how to run this

script,first,second,third = argv


print(argv)

print("The script is called: ",script)
print("The first variable is :",first)
print("The second variable is:",second)
print("The third variable is:",third)
