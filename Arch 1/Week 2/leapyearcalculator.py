Year = int(input("Enter a year: "))

if Year % 400 == 0: print("Leap year")
elif Year % 100 == 0:print("Not a Leap year")
elif Year % 4 == 0: print("Leap year")
else: print("Not a leap year")