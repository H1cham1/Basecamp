Horizontal_Label = "   1 2 3 4 5 6 7 8 9 10"
print(Horizontal_Label)
Calculateable_Numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

factors = range(1, 11)

for factor in factors:
    result = [int(num) * factor for num in Calculateable_Numbers]
    Real_Result = " ".join(map(str, result))
    print(f"{factor} {Real_Result}")
    




