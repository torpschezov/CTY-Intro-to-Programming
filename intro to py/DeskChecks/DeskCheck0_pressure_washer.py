print("Enter a number between 0-11")
number = []
number.append(int(input(">> ")))
if (number[0]>0 and number[0]<11):
    print("nice")
elif (number[0]<0 or number[0]>11):
    print("Hold up something is wrong")
    number.pop(int(input(">> ")))
    number.append(int(input("Now lets enter it correctly: ")))
    if (number[0]>0 and number[0]<11):
        print("Nice")
    elif(number[0]<0 or number[0]>11):
        print("Hold up something is wrong")
        number.pop(int(input(">> ")))
        number.append(int(input("Now lets enter it correctly: ")))
        if (number[0]>0 and number[0]<11):
            print("Nice")
        elif (number[0]<0 or number[0]>11):
            print("Hold up something is wrong")
            number.pop(int(input(">> ")))
            number.append(int(input("Now lets enter it correctly: ")))