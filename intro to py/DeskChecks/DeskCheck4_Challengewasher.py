print("Enter a number between 0-4")
number = []
number.append(int(input(">> ")))
if (number[0]>-1 and number[0]<5):
    print("nice")
elif (number[0]<-1 or number[0]>5):
    print("Hold up something is wrong")
    number.remove[(int(input(">> ")))]
    number.append(int(input("Now lets enter it correctly: ")))
    if (number[0]>-1 and number[0]<5):
        print("Nice")
        number.append(int(input(">> ")))
    elif(number[0]<-1 or number[0]>5):
        print("Hold up something is wrong")
        number.remove(int(input(">> ")))
        number.append(int(input("Now lets enter it correctly: ")))
        if (number[0]>-1 and number[0]<5):
            print("Nice")
            number.append(int(input(">> ")))
        elif (number[0]<-1 or number[0]>5):
            print("Hold up something is wrong")
            number.remove(int(input(">> ")))
            number.append(int(input("Now lets enter it correctly: ")))
print("Enter another number between 0-4")
number.append(int(input(">> ")))
if (number[0]>-1 and number[0]<5):
    print("nice")
    print("Enter another number between 0-4")
    number.append(int(input(">> ")))
elif (number[0]<-1 or number[0]>5):
    print("Hold up something is wrong")
    number.remove(int(input(">> ")))
    number.append(int(input("Now lets enter it correctly: ")))
    if (number[0]>-1 and number[0]<5):
        print("Nice")
        number.append(int(input(">> ")))
    elif(number[0]<-1 or number[0]>5):
        print("Hold up something is wrong")
        number.remove(int(input(">> ")))
        number.append(int(input("Now lets enter it correctly: ")))
        if (number[0]>-1 and number[0]<5):
            print("Nice")
            number.append(int(input(">> ")))
        elif (number[0]<-1 or number[0]>5):
            print("Hold up something is wrong")
            number.remove(int(input(">> ")))
            number.append(int(input("Now lets enter it correctly: ")))
print("Enter another number between 0-4")
number.append(int(input(">> ")))
if (number[0]>-1 and number[0]<5):
    print("nice")
    print("Enter another number between 0-4")
    number.append(int(input(">> ")))
elif (number[0]<-1 or number[0]>5):
    print("Hold up something is wrong")
    number.remove(int(input(">> ")))
    number.append(int(input("Now lets enter it correctly: ")))
    if (number[0]>-1 and number[0]<5):
        print("Nice")
        number.append(int(input(">> ")))
    elif(number[0]<-1 or number[0]>5):
        print("Hold up something is wrong")
        number.remove(int(input(">> ")))
        number.append(int(input("Now lets enter it correctly: ")))
print("Enter another number between 0-4")
number.append(int(input(">> ")))

print(number)