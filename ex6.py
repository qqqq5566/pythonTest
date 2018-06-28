#-*- coding:utf-8 -*-

#两个字符串相加，是拼接的意思 ‘Hello’ + " world" 结果为 “Hello world"

type_of_people = 10
x= "There are {} types of people".format(type_of_people)

binary = "binary"
do_not = "don't"
y="Those who know {} amd those who {}".format(binary,do_not)

print(x)
print(y)

print("I said:{}".format(x))
print("T also said: {}".format(y))

haiarious = False
joke_evaluation = "Isn't that joke so funny?!{}"
print(joke_evaluation.format(haiarious))

w = "This is the left side of..."
e = "a strin with a right side"

print(w+e)  #
