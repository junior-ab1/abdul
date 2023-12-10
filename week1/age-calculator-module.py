# you can not do operation on integer and strings all together unless you convert the string to an integer.Also,all results of an input are strings and needs to be converted to integers before doing operations on them.
name=input('what is your name? ')
year_of_birth=int(input('which year were you born? '))
age=2023-year_of_birth
print('\n'+name,'you are',age,'years old','\n')