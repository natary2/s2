a = int(input("Введите число "))
if (a%2 == 0) and ((a/2)<0):  print("отрицательное четное число")
elif (a/2 == 0):    print("нулевое число")
elif (a%2 != 0) and ((a/2)<0):  print("отрицательное нечетное число")
elif ((a%2) != 0) and ((a/2)>0):  print ("положительное нечетное число")
elif (a%2 == 0) and ((a/2)>0):    print("положительное четное число")
