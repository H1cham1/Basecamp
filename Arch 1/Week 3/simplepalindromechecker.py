Text = input("Please enter a text: ").lower()

index = len(Text) - 1

Reversed_Text = ""

while index >= 0:
    Reversed_Text += Text[index]
    index -= 1

if Reversed_Text == Text: 
    print('"' + Text + '"', 'is a palindrome')

else: print('"'+ Text +'"','is not a palindrome')
