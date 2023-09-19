Cost = float(input("Cost of the meal: "))

Tip = Cost * 0.15

Tax = Cost * 0.210

Total = float(Tip) + float(Tax) + float(Cost)

print("Tax: ", format(Tax, '.3f') , ", Tip: ", format(Tip, '.3f') , ", Total: ", format(Total, '.3f'))
