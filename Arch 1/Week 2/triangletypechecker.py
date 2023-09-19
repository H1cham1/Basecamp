Length = input("Please enter the length of the sides a= , b= , c=: ")

Side_A = Length[2]

Side_B = Length[7]

Side_C = Length[12]

if Side_A == Side_B == Side_C: print("Equilateral triangle")
elif Side_A == Side_B or Side_A == Side_C or Side_B == Side_C: print("Isosceles triangle")
else: print("Scalene")