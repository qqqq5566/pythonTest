#-*- coding:utf-8 -*-
from sys import argv
import os

script,from_file,out_file = argv

print("Copying from {} to {}".format(from_file,out_file))

#we could do these two on one line,how?

in_file = open(from_file)
indata = in_file.read()

#len(indata)  计算字符串的长度
print("This input file is {} bytes long.".format(len(indata)))

print("Dose the output file exiset? ",os.path.exists(out_file))

print("Ready,hit RETURN tu continue,CTRL-C to abort.")
input()

to_file = open(out_file,'w')
to_file.write(indata)

print("Alright,all done.")
in_file.close()
to_file.close()
