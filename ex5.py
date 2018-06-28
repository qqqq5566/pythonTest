#-*- coding:utf-8 -*-

#python 中的格式化输出变量
#如果在{0}有数字，则其他的{n}，必须也是数字

my_name = 'Zend A. Shaw'
my_age = 35
my_height = 74
my_weight = 180
my_eyes = 'blue'
my_teeth = 'White'
my_hair = 'Brown' 

#f 是format的意思
#print(f'Let\'s talk about {my_name}')  #这中格式化字符串从Python3.6开始使用
print("Let's talk about {}.".format(my_name))
print("He's {0} inches tall".format(my_height))
print("He's {} pounds heavy".format(my_weight))
print("Actually that's not too heavy")

print("He's got {0} eyes and {1} hair.".format(my_eyes,my_hair))
print("He's teeth are usually {} depending on the coffee.".format(my_teeth))


#this line is tricky,try to get it exactly right

total = my_age + my_height + my_weight
print("If I add {0},{1},and {2} I get {3}".format(my_age,my_height,my_weight,total))
