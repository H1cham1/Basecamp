Text = input("Please enter a text: ").lower()

Text2 = Text.replace(" ", "")

for char in Text2: 
    if Text2 == Text2[::-1]: 
        print('"'+ Text +'"', 'is a palindrome')
        break
else: print('"'+ Text +'"','is not a palindrome')