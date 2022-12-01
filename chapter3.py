age = input("enter your age")
age = int(age)
if age>= 14:
    print("you are above 14")
    #pass statement
    x = 18
    if x >18:
        pass
    #else statement
    else:
        print("sorry, you can't play")
    #exercise
        winning_number = 25
        user_input = input("guess a number b/w 1 and 100: ")
        user_input = int(user_input)
        if user_input ==winning_number:
            print("You win !!")
        else:
            if user_input < winning_number:
                print("too low")
            else:
                print("too high")
                #and or py
                name = 'abc'
                age = 19
            if name=='abc' and age==19:
                print("condition True")
            else:
                print("condition false")    

#vdeo50 if-elif-else statement
age = input("please input your age")
age = int(age)
if age==0 or age <0:
  print("you can't watch")
elif 0<age<=3:
  print("Ticket price : Free")
elif 3<age<=10:
  print("Ticket price : 150")
elif 10<age<=60:
  print("Ticket price: 300")
else:
  print("Ticket price : 190")
  
                            
#in keyword51 vdeo
name = "prateek"
if 'a' in name:
  print("a is present in name")
else:
  print("not present")


#check empty or not in pythobn video52
name = input("enter your name")
if name:
  print(f"your name is{name}")
else:
  print("you didnt write anything")

#loops video 53
#print("prateek is good
i = 1
while i<=10:
  print("prateek is good boy")
  i=i+2

#sum of numbers video=54
total = 0
i = 1
while i<=40:
  total = total+i
  i = i+1
print(total)


#exercise prac vdeo 56
n = input("enter a number")
n = int(n)
total = 0
i = 1
while i<=n:
  total +=i
  i +=1
  print(total)

#exercise58
number = input("enter a number")
int(number[i]) 
total = 0
i = 0
while  i < len(number):
   total += int(number[i])
   i +=1
   print(total)
   #exercise59
name = input("please enter your name")
#Prateek Agarwal
#name.count("p") , name.count(name[0]) 
#name.count("r") , name.count(name[1])
#name.count("a") , name.count(name[2])
#name.count("t") , name.count(name[2])
#name.count("e") , name.count(name[2])
#name.count("e") , name.count(name[2])
#name.count("e") , name.count(name[2])
temp_var = "e"
i = 0
while i < len(name):
    print(f"{name[i]} : {name.count(name[i])}")
    i += 1
    # infinite loop
    i = 0
    while i <=10:
      print("hello world")
      i += 1
      #or
      while True:
        print("hello world")
        # for loop with range function
        i = 0
        #while i <=10:
        #range function
        for i in range(1,10):
          print("hello world")
