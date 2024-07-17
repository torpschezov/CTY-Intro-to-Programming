chelsea =[]
x=-1
yorn = "y"
yesorno ="y"
while yorn == "y":
    chelsea.append(input("Type your message >> "))
    x+=1
    yorn = input("Do you want to continue? y or n>> ")
while yesorno =="y":
    num = input(f"you have {x} messages which one to you want 0-{x}: ")
    print(chelsea[int(num)])
    yesorno = input("Would you like to see another? y or n: ")
