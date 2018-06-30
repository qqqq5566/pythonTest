#-*- coding:utf-8 -*-

print("Let's practice everyting")
print("You'd need to know out escapes with \ that do:")
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation 
\n\t\t where there is none
"""

print('-'*20)
print(poem)
print('-'*20)

five = 10 - 2 +3 -6
print('this should be five:',five )

def secret_formule(started):
	jelly_beabs = started * 500
	jars = jelly_beabs / 1000
	crates = jars / 100
	return jelly_beabs,jars,crates

start_point = 10000
beans,jars,crates = secret_formule(start_point)
print("With a starting point of :{}".format(start_point))
print("We'd hava {0} beans {1} jars,and {2} crates.".format(beans,jars,crates))

start_point = start_point / 10
print("We can alse do that this way:")
formula = secret_formule(start_point) 
print("We'd hava {} beans,{} jars,and {} crates.".format(*formula))  #* 是传多个参数
