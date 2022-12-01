name = "prateek"
print(len(name))
print(f"character count: {name.count('chr')}")
#strings
first_name = "prateek"
last_name = "Agarwal"
full_name = first_name+last_name
print(full_name*3)
#user input
#input function
#name = input("Enter your name")
#print("hello " + name)
#string
agw = input("what is your age")
print("your age "+agw)
#22#
number_one = input("enter first number")
number_two = input("enter second number")
total=number_one + number_two
print("total is " +str(total))
name, age = "prateek", 24
print("hello " + name+ "your age is" + age)
x=y=z=1
print(x+y+z)
#two input
name ,  age = input("enter your name and age").split(",")
print(name)
print(age)
#string formatting
print("hello {} your age is {}".format(name , age))
#Average/3
num1,num2,num3 = input("Enter three numbers cima seprated").split(" ")
#string_indexing
language = "prateek"
print(language[4])
print("prateek"[3:1])
name = input("enter your name: ")
print(f"reverse of your name is name{-1::-1]} ")
#string method
print(len("prateek"))
#lower merthod
print(name.lower())
print(name.capitalize())
#title me phela capital baaki small hoge isme
print(name.title())
name = "prateek"
print(len(name))
print(f"character count: {name.count(chr)}")
print(name + "dots")
print(name.lstrip()+ "dots")
print(name.strip() + "dots")
print(name.replace(" ","")+"dots")
string = "she is beautiful and she is a gooddancer "
print(string.replace("is","was"))
print(string.find("is",1))
#4 pr kra search pr apn 5 se krege
is_pos1 = string.find("is")
is_pos2 = string.find("is",is_pos1+1) 
print(is_pos2)
#center method
name= "harshit"
#length is jyda type krna number
print(name.center(11,"*"))
name=input("enter your name: ")
print(name.center(len(name)+8,"*"))
#immutable strings-cannot change
string = "string"
print(string.replace('t','T'))
(string[1])  = 'T'
name = "prateek"
name = name + "Agarwal"
print(name)
age = 23
age += 3
print(age) 