#-*- coding:utf-8 -*-

#argv 和input的同时使用

from sys import argv

script,user_name = argv

promat = '>'

print("Hi {},I'm the {} script.".format(user_name,script))
print("I'd like to ask you a few question.")
print("Dow you like me {}".format(user_name))
likes = input(promat)

print("Where do you live {}".format(user_name))
lives = input(promat)

print("What do you computer do you have?")
computer = input(promat)

print("""
Alright,so you said {} about liking me.
You live in {}. Not sure where that is.
And you hava a {} computer.Nice
""".format(likes,lives,computer))
