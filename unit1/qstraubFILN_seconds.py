second = input("put in a number of seconds ")
second = int(second)
min = second / 60
sec = second % 60
hour = min / 60
min = min % 60
print ("This is " + str(hour) + " hours " + str(min) + " mintes and "+ str(sec) + " seconds")

