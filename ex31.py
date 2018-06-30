#-*- coding:utf-8 -*-

#作出决定

print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")
try:
	door = int(input('>'))
	if door == 1:
		print("There's a giant bear hear eating a cheese cake.")
		print("What do you do?")
		print("1. Take the cake.")
		print("2. Scream at the brear.")
		bear = int(input('>'))

		if bear == 1:
			print("The bear eats your face off. Good job!")
		elif bear == 2:
			print("The bear eats your legs off. Good job!")
		else:
			print("Well,doing {} is probably better".format(bear))
			print("Bear runs away")

	elif door == 2:
		print("You state into the endless abyss at Cthulhu's retina.")
		print("1. Blueberries.")
		print("2. Yellow jacket clothespins.")
		print("3. Understanding revolvers yelling melodies.")

		insanity = int(input('>'))
		if insanity == 1 or insanity == 2:
			print("Your body survives powered by a mind of jello.")
			print("Good job!")
		else:
			print("The insanity rots eyes into a pool of muck.")
			print("Good job!")
	else:
		print("You stumble around and fall on a knife and die. Good job!")
except:
	print("请输入数字")