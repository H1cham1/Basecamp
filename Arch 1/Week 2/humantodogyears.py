Human_Years = int(input("Please enter an amount of years: "))

if 0 <= Human_Years <= 2: print("Dog Years: " + str(Human_Years * 10.5))
elif Human_Years > 2: print("Dog Years: " + str(((Human_Years - 2) * 4) + 21))
elif Human_Years < 0: print("Only positive numbers are allowed")
                            
                            