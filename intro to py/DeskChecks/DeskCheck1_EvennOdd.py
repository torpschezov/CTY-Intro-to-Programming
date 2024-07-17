num = input("Enter a number to see if it is Even or Odd>> ")
list1 = []
checker = int(num)%2
if (checker == 0):
    print(f"{num} is even and will be sent to a list")
    list1.append(num)
    num2 = input("Enter another number>> ")
    checker2 = int(num2)%2
    if (checker2 ==0):
        print(f"{num} is even and will be sent to a list")
        list1.append(num2)
    elif (checker2 != 0):
        print("This is odd try again")
        num2 = input(">> ")
        checker2 = int(num2)%2
        if (num2 == 0):
            print("This is even and will be sent to a list")
            list1.append(num2)
elif (checker != 0):
    print("This is odd try again")
    num = input(">> ")
    checker = int(num)%2
    if (checker == 0):
        print(f"{num} is even and will be sent to a list")
        list1.append(num)
print("do you want to see the list?")
yorn = input("y or n>> ")
if (yorn == "y"):
    print(list1)