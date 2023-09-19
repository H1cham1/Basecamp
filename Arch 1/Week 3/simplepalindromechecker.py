Text = input("Please enter a text: ").lower()

for char in Text:
    if Text == Text[::-1]: print('"'+ Text +'"', 'is a palindrome')
    elif Text != Text[::-1]:
        print('"'+ Text +'"', 'is not a palindrome')
        break
else: print('"'+ Text +'"','is not a palindrome')
